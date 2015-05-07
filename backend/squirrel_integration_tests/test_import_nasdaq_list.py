from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.unittest import TestCase
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.plugin_loader import PluginRegistry
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins

# Uncomment this to true to debug unclean reactor
# from twisted.internet.base import DelayedCall
# DelayedCall.debug = True


log = logging.getLogger(__name__)


class IntegrationTestNasdaqList(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)
        initializeConfig("integ_tests")
        loadPlugins(["NasdaqList"])

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()
        unloadPlugins()

    @defer.inlineCallbacks
    def test_GetList(self):
        print("Requesting nasdaq list")
        log.debug("requesting Nasdaq AAPL")
        res = yield PluginRegistry().getByName("Nasdaq List").getList()
        self.assertNotEmpty(res)
    test_GetList.skip = "not implemented"
