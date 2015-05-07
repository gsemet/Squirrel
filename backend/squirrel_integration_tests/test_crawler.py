from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.model.ticker import Ticker
from squirrel.procedures.crawler import Crawler
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.config import updateFullPaths
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


log = logging.getLogger(__name__)


class IntegrationTestCrawler(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig("integ_tests")
        updateFullPaths()
        loadPlugins(["GoogleFinance"])
        self.crawler = Crawler()

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()
        unloadPlugins()

    @defer.inlineCallbacks
    def testRefreshStockList(self):
        log.debug("refreshing stock list")
        yield self.crawler.refreshStockList(importerName="GoogleFinance",
                                            number=60)

    @defer.inlineCallbacks
    def testRefreshStockHistory(self):
        log.debug("requesting google finance AAPL + GOOG")
        yield self.crawler.refreshStockHistory("GoogleFinance",
                                               [
                                                   Ticker("AAPL", "NASDAQ"),
                                                   Ticker("GOOG", "NASDAQ"),
                                               ])
