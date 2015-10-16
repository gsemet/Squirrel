from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.model.tick import Tick
from squirrel.model.ticker import Ticker
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.plugin_loader import PluginRegistry
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins

# Uncomment this to true to debug unclean reactor
# from twisted.internet.base import DelayedCall
# DelayedCall.debug = True


log = logging.getLogger(__name__)


class IntegrationTestYahooFinance(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig("integ_tests")
        loadPlugins(["YahooFinance"])

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()
        unloadPlugins()

    @defer.inlineCallbacks
    def test_GoodTicker_DataIsNotEmpty(self):
        log.debug("requesting google finance AAPL")
        res = yield PluginRegistry().getByName("Yahoo Finance").getTicks(
            Ticker("AAPL", "NASDAQ"), "2015-01-01", "2015-01-30")
        self.assertNotEmpty(res)
        self.assertEqual(Tick(ticker=Ticker(symbol="AAPL", exchange="NASDAQ"),
                              date=1420153200,
                              open=111.39,
                              high=111.44,
                              low=107.35,
                              close=109.33,
                              volume=53204600,
                              cdays=True), res[0])
        for tick in res[:10]:
            self.assertNotEqual(tick.open, 0)
            self.assertNotEqual(tick.volume, 0)
        [log.debug("%r", r) for r in res[:10]]

    @defer.inlineCallbacks
    def test_BadTicker_ExceptionOccurs(self):
        yield self.assertInlineCallbacksRaises(
            Exception,
            PluginRegistry().getByName("Yahoo Finance").getTicks,
            Ticker("BAD_TICKER", "NASDAQ"), "2015-01-01", "2015-01-30")
