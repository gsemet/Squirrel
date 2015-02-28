import os

from squirrel.config.config import Config
from squirrel.routes import app

from squirrel.routes import *


def makeFullPath(relPath):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        os.pardir,
                                        os.pardir,
                                        relPath))


def dumpConfig():
    c = Config()
    print "Configuration: "
    print "  backend root dir: {}".format(c.frontend['root_path'])
    c.frontend['root_full_path'] = makeFullPath(c.frontend['root_path'])
    c.frontend['doc_full_path'] = makeFullPath(c.frontend['doc_path'])

    print ""
    print "Listing all available keys:"
    print c.documentNamespace()


def run():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    print "Loading configuration {}".format(config_path)
    c = Config()
    c.loadConfig(config_path)
    dumpConfig()
    print "Connecting to DB"
    print "Starging web service on 8080"
    print "Serving : {}".format(Config().frontend['root_full_path'])
    app.run("localhost", 8080)
