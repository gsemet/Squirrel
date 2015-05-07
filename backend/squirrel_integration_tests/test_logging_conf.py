from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from squirrel.common.downloader import cleanupReactorForUnitTest
from squirrel.common.downloader import prepareReactorForUnitTest
from squirrel.common.logging import setupLogger
from squirrel.common.unittest import TestCase
from squirrel.services.config import initializeConfig
from squirrel.services.config import unloadConfig
from squirrel.services.config import updateFullPaths


log = logging.getLogger(__name__)


class IntegrationTestLonggingConf(TestCase):

    def setUp(self):
        prepareReactorForUnitTest(self)

    def tearDown(self):
        cleanupReactorForUnitTest(self)
        unloadConfig()

    def testHerokuLogging(self):
        initializeConfig("integ_tests")
        updateFullPaths()
        setupLogger()

    def testDevLogging(self):
        initializeConfig("dev")
        updateFullPaths()
        setupLogger()

    def testProdLogging(self):
        initializeConfig("prod")
        updateFullPaths()
        setupLogger()
