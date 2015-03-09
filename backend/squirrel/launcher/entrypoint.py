from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from squirrel.common.i18n import setupI18n
from squirrel.config.load_config import initializeConfig
from squirrel.services.db import connectDatabase
from squirrel.services.serve_backend import serveBackend


def run():
    setupI18n()
    initializeConfig()
    connectDatabase()
    serveBackend()
