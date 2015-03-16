from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import logging.config as logging_config

from twisted.internet import defer

from squirrel.config.load_config import Config
from squirrel.config.load_config import initializeConfig
from squirrel.config.load_config import unloadConfig
from squirrel.model.ticker import Ticker
from squirrel.procedures.crawler import Crawler
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins

from crochet import run_in_reactor
from crochet import setup

# Uncomment this to true to debug unclean reactor
# from twisted.internet.base import DelayedCall
# DelayedCall.debug = True


log = logging.getLogger(__name__)


def setupLogger():
    logging_config.fileConfig(Config().frontend.logging_conf_full_path)
    logging.debug("Logger configured by: {}".format(Config().frontend.logging_conf_full_path))


@defer.inlineCallbacks
def runInlineCallbacks():
    initializeConfig()
    setupLogger()
    loadPlugins(["GoogleFinance"])

    crawler = Crawler()
    log.debug("refreshing stock list")
    yield crawler.refreshStockList()

    log.debug("requesting google finance AAPL + GOOG")
    yield crawler.refreshStockHistory([
        Ticker("AAPL", "NASDAQ"),
        Ticker("GOOG", "NASDAQ"),
    ])
    unloadConfig()
    unloadPlugins()


@run_in_reactor
def runCrochet():
    return runInlineCallbacks()


def run():
    setup()
    runCrochet()
