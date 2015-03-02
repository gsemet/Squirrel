
from squirrel.config.load_config import initializeConfig
from squirrel.services.db import connectDatabase
from squirrel.services.serve_backend import serveBackend


def run():
    initializeConfig()
    connectDatabase()
    serveBackend()
