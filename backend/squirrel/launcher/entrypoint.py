from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import logging.config as logging_config

from squirrel.common.i18n import setupI18n
from squirrel.config.load_config import Config
from squirrel.config.load_config import initializeConfig
from squirrel.services.db import connectDatabase
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.serve_backend import serveBackend

log = logging.getLogger(__name__)


def setupLogger():
    logging_config.fileConfig(Config().frontend.logging_conf_full_path)
    logging.debug("Logger configured by: {}".format(Config().frontend.logging_conf_full_path))


def run():
    initializeConfig()
    setupLogger()
    setupI18n()
    loadPlugins()
    connectDatabase()
    serveBackend()
