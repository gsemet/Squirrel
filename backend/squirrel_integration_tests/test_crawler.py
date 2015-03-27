from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.config.load_config import Config
from squirrel.config.load_config import initializeConfig
from squirrel.config.load_config import unloadConfig
from squirrel.config.load_config import updateFullPaths
from squirrel.model.ticker import Ticker
from squirrel.procedures.crawler import Crawler
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


log = logging.getLogger(__name__)


class IntegrationTestCrawler(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig()
        Config().backend.db.url = "sqlite:///{workdir}/db-for-integ-tests.sqlite".format(
            workdir=Config().backend.db.workdir)
        updateFullPaths(Config())
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
        yield self.crawler.refreshStockHistory([
            Ticker("AAPL", "NASDAQ"),
            Ticker("GOOG", "NASDAQ"),
        ])
