from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os
import sys
import yaml

from squirrel.common.i18n import _
from squirrel.config.config import Config

log = logging.getLogger(__name__)


def _loadYaml(yamlpath):
    with open(yamlpath) as f:
        return yaml.load(f)


def _loadConfig(configPath):
    log.debug(_("Loading configuration: {}").format(configPath))
    cfg = _loadYaml(configPath)
    Config().unload()
    Config(cfg)


def _makeFullPath(relPath):
    if os.path.isabs(relPath):
        return relPath
    if sys.platform.startswith("win32"):
        relPath = os.path.normpath(relPath)
    backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                os.pardir,
                                                os.pardir))
    return os.path.abspath(os.path.join(backend_root, relPath))


def _makeSqlLitePath(url):
    sqlite_proto = "sqlite:///"
    if url.startswith(sqlite_proto):
        return sqlite_proto + _makeFullPath(url[len(sqlite_proto):])
    return url


def updateFullPaths(c):
    c.frontend.root_full_path = _makeFullPath(c.frontend.root_path)
    c.frontend.doc_full_path = _makeFullPath(c.frontend.doc_path)
    c.frontend.logging_conf_full_path = _makeFullPath(c.frontend.logging_conf_path)
    c.backend.db.full_url = _makeSqlLitePath(c.backend.db.url)
    c.backend.db.full_workdir = _makeFullPath(c.backend.db.workdir)
    if sys.platform.startswith("win32"):
        c.backend.db.full_url = c.backend.db.full_url.replace("\\", "\\\\")
    c.plugins.full_default_path = _makeFullPath(c.plugins.default_path)


def _dumpConfig():
    c = Config()
    updateFullPaths(c)

    log.debug("")
    log.debug(_("Listing all available keys:"))
    log.debug(c.dumpFlat())


def initializeConfig():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    _loadConfig(config_path)
    _dumpConfig()


def unloadConfig():
    Config().unload()
