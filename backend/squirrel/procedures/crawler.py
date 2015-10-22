# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from twisted.internet import defer

from squirrel.db.model import Model
from squirrel.db.tables.table_currencies import TableCurrencies
from squirrel.db.tables.table_plugin_importers import TablePluginImporters
from squirrel.services.config import Config
from squirrel.services.plugin_loader import PluginRegistry

log = logging.getLogger(__name__)


class Crawler(object):

    @defer.inlineCallbacks
    def refreshStockList(self, importerName,  wantedPlaces=None, number=None):
        with Model(Config().backend.db.full_url) as model:
            importer = TablePluginImporters(id=None,
                                            name=importerName)
            importer.ensureHasId(model)
            if number is None:
                log.debug("Getting list of all stocks")
            else:
                log.debug("Getting %s first stocks", number)
            log.debug("Wanted places: %s", wantedPlaces if wantedPlaces is not None else "All")
            stocks = yield PluginRegistry().getByName(importer.name).getList(
                number=number,
                wantedPlaces=wantedPlaces)
            for stock in stocks:
                print("TODO: store in mongo")

    @defer.inlineCallbacks
    def refreshStockHistory(self, importerName, tickers):
        with Model(Config().backend.db.full_url) as model:
            importer = TablePluginImporters(id=None,
                                            name=importerName)
            importer.ensureHasId(model)
            for ticker in tickers:
                ticks = yield PluginRegistry().getByName(importer.name).getTicks(
                    ticker, intervalMin=60 * 24, nbIntervals=10)
                log.debug("ticks: " + str(ticks[:20]))

                currency = TableCurrencies(id=None,
                                           name="dollar")
                currency.ensureHasId(model)
                print("TODO: store in mongo")

    @defer.inlineCallbacks
    def refreshAllStockList(self):
        yield self.refreshStockList(importerName="GoogleFinance")
