from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.config.config import Config
from squirrel.db.model import Model
from squirrel.db.tables.symbols import TableSymbols
from squirrel.db.tables.ticks import TableTick
from squirrel.model.ticker import Ticker
from squirrel.services.plugin_loader import PluginRegistry

log = logging.getLogger(__name__)


class Crawler(object):

    def __init__(self, tickers):
        for t in tickers:
            assert isinstance(t, Ticker), "Crawler expect list of Ticker"
        self.tickers = tickers

    @defer.inlineCallbacks
    def run(self):
        with Model(Config().backend.db.full_url) as model:
            for ticker in self.tickers:
                ticks = yield PluginRegistry().get("Google Finance").getTicks(ticker,
                                                                              intervalMin=60 * 24,
                                                                              nbIntervals=10)
                log.debug("ticks: " + str(ticks[:20]))
                symbol_row = TableSymbols(None, ticker.symbol, ticker.exchange)
                symbol_id = symbol_row.addAndGetId(model)
                for tick in ticks:
                    model.session.add(TableTick(symbol_id=symbol_id,
                                                date=tick.date,
                                                open=tick.open,
                                                high=tick.high,
                                                low=tick.low,
                                                close=tick.close,
                                                volume=tick.volume))
                model.session.commit()
