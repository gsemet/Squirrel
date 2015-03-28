from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from collections import namedtuple
from enum import Enum
from twisted.application.service import Service

from squirrel.common.singleton import singleton
from squirrel.config.config import Config
from squirrel.services.plugin_loader import PluginRegistry

log = logging.getLogger(__name__)

CrawerStatus = namedtuple("CrawerStatus", ["name",
                                           "description",
                                           "status",
                                           ],
                          verbose=False)


class CRAWER_STATUS(Enum):
    STARTED = "started"
    NOT_STARTED = "not started"


@singleton
class CrawlerConfig(Service):

    enabled_crawlers = []

    def reconfigure(self):
        plugins = PluginRegistry().getPluginNamesByCategory("Import")
        log.info("plugins: {}".format(plugins))
        self.enabled_crawlers = []
        for crawler_config_name, crawler_config in Config().crawlers.items():
            if crawler_config.plugin_name in plugins:
                log.info("Plugin found: {}".format(crawler_config.plugin_name))
                self.enabled_crawlers.append(CrawerStatus(name=crawler_config.plugin_name,
                                                          description=crawler_config.description,
                                                          status=CRAWER_STATUS.NOT_STARTED))

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
        return self.enabled_crawlers[:]

    def getAllCrawlerDescriptions(self):
        # return a copy of crawlers
        r = []
        for c in self.enabled_crawlers:
            r.append({
                'name': c.name,
                'description': c.description,
                'status': c.status,
            })
        return r

    def start(self, name):
        log.info("Order received: start crawler {!r}".format(name))
        pass

    def stop(self, name):
        log.info("Order received: stop crawler {!r}".format(name))
        pass

    def getProgress(self, name):
        log.info("Order received: get crawler progress {!r}".format(name))
        pass


def configureCrawlers():
    log.info("Configuring crawlers")
    CrawlerConfig().reconfigure()


def deconfigureCrawlers():
    CrawlerConfig().unload()
