from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.application.service import Service

from squirrel.common.enum import Enum
from squirrel.common.result import FAILURE
from squirrel.common.result import SUCCESS
from squirrel.common.singleton import singleton
from squirrel.services.config import Config
from squirrel.services.plugin_loader import PluginRegistry

log = logging.getLogger(__name__)


class CrawerStatus(object):
    name = None
    description = None
    status = None

    def __init__(self, name=None, description=None, status=None):
        self.name = name
        self.description = description
        self.status = status


class CRAWLER_STATUS(Enum):
    STOPPED = "stopped"
    PENDING_START = "pending start"
    STARTED = "started"
    PENDING_STOP = "pending stop"


@singleton
class CrawlerConfig(Service):

    crawlers = {}

    def reconfigure(self):
        plugins = PluginRegistry().getPluginNamesByCategory("Import")
        log.info("plugins: {}".format(plugins))
        self.crawlers = {}
        for crawler_config_name, crawler_config in Config().crawlers.items():
            if crawler_config.plugin_name in plugins:
                log.info("Plugin found: {}".format(crawler_config.plugin_name))
                self.crawlers[crawler_config.plugin_name] = (CrawerStatus(
                    name=crawler_config.plugin_name,
                    description=crawler_config.description,
                    status=CRAWLER_STATUS.STOPPED))

        # 'GoogleFinance':
        #     plugin_name: GoogleFinance
        #     refresh_list:
        #         manual: enabled
        #     refresh:
        #         exchanges:
        #             wanted: all
        #             group_by: 60
        #         stocks:
        #             'NASDAQ':
        #                 - "AAPL"
        #                 - "GOOG"
    def getAllCrawlers(self):
        # return a copy of crawlers
        return self.crawlers.values()

    def getAllCrawlerDescriptions(self):
        # return a copy of crawlers
        r = []
        for c in self.crawlers.values():
            r.append({
                'name': c.name,
                'description': c.description,
                'status': c.status,
            })
        return r

    def getStatus(self, name):
        if not self.crawlers:
            return (FAILURE, "no crawler initialized")
        if name not in self.crawlers:
            return (FAILURE, "invalid crawler name: {}. Available: {}".format(name,
                                                                              self.crawlers.keys()))
        crawler = self.crawlers[name]
        return (SUCCESS, crawler.status)

    def start(self, name):
        log.info("Order received: start crawler {!r}".format(name))
        if not self.crawlers:
            return (FAILURE, "no crawler initialized")
        if name not in self.crawlers:
            return (FAILURE, "invalid crawler name: {}. Available: {}".format(name,
                                                                              self.crawlers.keys()))
        crawler = self.crawlers[name]
        if crawler.status == CRAWLER_STATUS.PENDING_START:
            return (FAILURE, "already pending start")
        elif crawler.status == CRAWLER_STATUS.STARTED:
            return (FAILURE, "already started")
        elif crawler.status == CRAWLER_STATUS.PENDING_STOP:
            return (FAILURE, "unable to start, stop pending")
        elif crawler.status == CRAWLER_STATUS.STOPPED:
            crawler.status = CRAWLER_STATUS.PENDING_START
            return (SUCCESS, "crawler start request sent")
        else:
            raise Exception("Invalid state: {}".format(crawler.status))

    def stop(self, name):
        log.info("Order received: stop crawler {!r}".format(name))
        if not self.crawlers:
            return (FAILURE, "no crawler initialized")
        if name not in self.crawlers:
            return (FAILURE, "invalid crawler name: {}. Available: {}".format(name,
                                                                              self.crawlers.keys()))
        crawler = self.crawlers[name]
        if crawler.status == CRAWLER_STATUS.PENDING_STOP:
            return (FAILURE, "already pending stop")
        elif crawler.status == CRAWLER_STATUS.STOPPED:
            return (FAILURE, "already stopped")
        elif crawler.status == CRAWLER_STATUS.PENDING_START:
            return (FAILURE, "unable to stop, start pending")
        elif crawler.status == CRAWLER_STATUS.STARTED:
            crawler.status = CRAWLER_STATUS.PENDING_STOP
            return (SUCCESS, "crawler stop request sent")
        else:
            raise Exception("Invalid state: {}".format(crawler.status))

    def getProgress(self, name):
        log.info("Order received: get crawler progress {!r}".format(name))
        if not self.crawlers:
            return (FAILURE, "no crawler initialized")
        if name not in self.crawlers:
            return (FAILURE, "invalid crawler name: {}. Available: {}".format(name,
                                                                              self.crawlers.keys()))
        crawler = self.crawlers[name]
        if crawler.status != CRAWLER_STATUS.STARTED:
            return (FAILURE, "Invalid state: {}".format(crawler.status))
        return (SUCCESS, 666)


def configureCrawlers():
    log.info("Configuring crawlers")
    CrawlerConfig().reconfigure()


def deconfigureCrawlers():
    CrawlerConfig().unload()
