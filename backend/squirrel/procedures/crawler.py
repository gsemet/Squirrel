from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.db.model import Model

from squirrel.config.config import Config
from squirrel.db.tables.currencies import TableCurrencies
from squirrel.db.tables.plugin_importers import TablePluginImporters
from squirrel.db.tables.stocks import TableStocks
from squirrel.db.tables.ticks import TableTicks
from squirrel.model.ticker import Ticker
from squirrel.services.plugin_loader import PluginRegistry

log = logging.getLogger(__name__)


class Crawler(object):

    @defer.inlineCallbacks
    def refreshStockList(self, number=None):
        importer_name = "Google Finance"
        with Model(Config().backend.db.full_url) as model:
            importer = TablePluginImporters(id=None,
                                            name=importer_name)
            importer.ensureHasId(model)
            log.debug("Getting {} first stocks".format(number))
            stocks = yield PluginRegistry().getByName(importer.name).getList(number=number)
            for stock in stocks:
                currency = TableCurrencies(id=None,
                                           name=stock.currency)
                currency.ensureHasId(model)

                stock = TableStocks(id=None,
                                    symbol=stock.symbol,
                                    exchange=stock.exchange,
                                    importer_id=importer.id,
                                    title=stock.title,
                                    currency_id=currency.id)
                stock.ensureHasId(model)
                model.session.commit()

    @defer.inlineCallbacks
    def refreshStockHistory(self, tickers):
        for t in tickers:
            assert isinstance(t, Ticker), "Crawler expect list of Ticker"
        importer_name = "Google Finance"
        with Model(Config().backend.db.full_url) as model:
            importer = TablePluginImporters(id=None,
                                            name=importer_name)
            importer.ensureHasId(model)
            for ticker in tickers:
                ticks = yield PluginRegistry().getByName(importer.name).getTicks(
                    ticker, intervalMin=60 * 24, nbIntervals=10)
                log.debug("ticks: " + str(ticks[:20]))

                currency = TableCurrencies(id=None,
                                           name="dollar")
                currency.ensureHasId(model)

                stock = TableStocks(id=None,
                                    symbol=ticker.symbol,
                                    exchange=ticker.exchange,
                                    importer_id=importer.id,
                                    title="",
                                    currency_id=currency.id)
                stock.ensureHasId(model)
                for tick in ticks:
                    model.session.add(TableTicks(stock_id=stock.id,
                                                 date=tick.date,
                                                 open=tick.open,
                                                 high=tick.high,
                                                 low=tick.low,
                                                 close=tick.close,
                                                 volume=tick.volume))
                model.session.commit()

    @defer.inlineCallbacks
    def refreshAllStockList(self):
        yield self.refreshStockList()
