from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.model.ticker import Ticker
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.plugin_loader import PluginRegistry
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


log = logging.getLogger(__name__)


class IntegrationTestBoursorama(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig("integ_tests")
        loadPlugins(["GoogleFinance"])

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()
        unloadPlugins()

    @defer.inlineCallbacks
    def test_GoodTicker_DataIsNotEmpty(self):
        raise NotImplementedError
    test_GoodTicker_DataIsNotEmpty.skip = "not implemented"

    @defer.inlineCallbacks
    def test_BadTicker_ExceptionOccurs(self):
        yield self.assertInlineCallbacksRaises(
            Exception,
            PluginRegistry().getByName("Boursorama").getTicks,
            Ticker("BAD_TICKER", "NASDAQ"), intervalMin=60 * 24, nbIntervals=2)
    test_BadTicker_ExceptionOccurs.skip = "not implemented"
