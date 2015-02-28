import os

from squirrel.config.config import Config
from squirrel.config.config import loadConfig
from squirrel.routes import app

from squirrel.routes import *


def makeFullPath(relPath):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        os.pardir,
                                        os.pardir,
                                        relPath))


def dumpConfig():
    c = Config()
    print "c", type(c)
    print "c.frontend", type(c.frontend)

    print "Configuration: "
    print "  backend root dir: {}".format(c.frontend.root_path)
    c.frontend.root_full_path = makeFullPath(c.frontend.root_path)
    c.frontend.doc_full_path = makeFullPath(c.frontend.doc_path)

    print ""
    print "Listing all available keys:"
    print c.dumpFlat()


def initializeConfig():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    print "Loading configuration {}".format(config_path)
    loadConfig(config_path)
    dumpConfig()


def serveBackend():
    port = Config().frontend.port
    print "Starging web service on {}".format(port)
    print "Serving front end located at: {}".format(Config().frontend.root_full_path)
    app.run("localhost", port)


def connectDatabase():
    print "Connecting to DB"


def run():
    initializeConfig()
    connectDatabase()
    serveBackend()
