from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from squirrel.config.load_config import initializeConfig
from squirrel.services.db import connectDatabase
from squirrel.services.serve_backend import serveBackend


def run():
    initializeConfig()
    connectDatabase()
    serveBackend()
