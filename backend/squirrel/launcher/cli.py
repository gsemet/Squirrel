from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import logging.config as logging_config
import sys

from crochet import setup
from crochet import wait_for

from squirrel.config.load_config import Config
from squirrel.config.load_config import initializeConfig
from squirrel.config.load_config import unloadConfig
from squirrel.procedures.crawler import Crawler
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


# Uncomment this to true to debug unclean reactor
# from twisted.internet.base import DelayedCall
# DelayedCall.debug = True


log = logging.getLogger(__name__)


def setupLogger():
    logging_config.fileConfig(Config().frontend.logging_conf_full_path)
    logging.debug("Logger configured by: {}".format(Config().frontend.logging_conf_full_path))


# Do not write it in inlinecallback or we will lose traceback in case of exception
def crawlAllStocks():
    crawler = Crawler()
    log.debug("refreshing stock list")
    wanted_places = None

    d = crawler.refreshStockList(wantedPlaces=wanted_places)

    @d.addCallback
    def d1(c):
        log.debug("c {!r}".format(c))
    #    log.debug("requesting google finance AAPL + GOOG")
    #     return crawler.refreshStockHistory([
    #         Ticker("AAPL", "NASDAQ"),
    #         Ticker("GOOG", "NASDAQ"),
    #     ])

    return d


# wait_for ensure correct exception to be display
@wait_for(24 * 60 * 60)
def runCrochet():
    initializeConfig()
    setupLogger()
    loadPlugins(["GoogleFinance"])
    d = crawlAllStocks()

    @d.addCallback
    def d2(_):
        unloadConfig()
        unloadPlugins()

    @d.addErrback
    def err(failure):
        log.exception("Exception received: {}".format(failure))
        sys.exit(1)

    return d


def run():
    setup()
    runCrochet()
