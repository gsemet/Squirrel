from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import yaml

from squirrel.config.config import Config


def _loadYaml(yamlpath):
    with open(yamlpath) as f:
        return yaml.load(f)


def _loadConfig(configPath):
    cfg = _loadYaml(configPath)
    Config().unload()
    Config(cfg)


def _makeFullPath(relPath):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        os.pardir,
                                        os.pardir,
                                        relPath))


def _makeSqlLitePath(url):
    sqlite_proto = "sqlite:///"
    if url.startswith(sqlite_proto):
        return sqlite_proto + _makeFullPath(url[len(sqlite_proto):])
    return url


def _dumpConfig():
    c = Config()
    print("c", type(c))
    print("c.frontend", type(c.frontend))

    print("Configuration: ")
    print("  backend root dir: {}".format(c.frontend.root_path))
    c.frontend.root_full_path = _makeFullPath(c.frontend.root_path)
    c.frontend.doc_full_path = _makeFullPath(c.frontend.doc_path)
    c.backend.db.full_url = _makeSqlLitePath(c.backend.db.url)
    if sys.platform == "win32":
        c.backend.db.full_url = c.backend.db.full_url.replace("\\", "\\\\")

    print("")
    print("Listing all available keys:")
    print(c.dumpFlat())


def initializeConfig():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    print("Loading configuration {}".format(config_path))
    _loadConfig(config_path)
    _dumpConfig()
