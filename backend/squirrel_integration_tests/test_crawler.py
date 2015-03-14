from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.config.load_config import initializeConfig
from squirrel.config.load_config import unloadConfig
from squirrel.model.ticker import Ticker
from squirrel.procedures.crawler import Crawler
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


log = logging.getLogger(__name__)


class IntegrationTestCrawler(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig()
        loadPlugins(["GoogleFinance"])

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()
        unloadPlugins()

    @defer.inlineCallbacks
    def testCrawler(self):
        initializeConfig()
        log.debug("requesting google finance AAPL + GOOG")
        crawler = Crawler([
            Ticker("AAPL", "NASDAQ"),
            Ticker("GOOG", "NASDAQ"),
        ])
        yield crawler.run()
