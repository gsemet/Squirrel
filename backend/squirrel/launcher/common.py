from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.common.i18n import setupI18n
from squirrel.common.logging import setupLogger
from squirrel.config.load_config import initializeConfig
from squirrel.config.load_config import unloadConfig
from squirrel.services.db import connectDatabase
from squirrel.services.plugin_loader import loadPlugins
from squirrel.services.plugin_loader import unloadPlugins


def serverSetup():
    initializeConfig()
    setupLogger()
    setupI18n()
    loadPlugins()
    connectDatabase()


def serverStop():
    unloadConfig()
    unloadPlugins()
