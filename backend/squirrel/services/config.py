from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import os
import sys
import yaml

from dictns import Namespace
from dictns import _appendToParent

from squirrel.common.dict import mergeDict
from squirrel.common.i18n import _
from squirrel.common.singleton import singleton
from squirrel.common.text import indent


log = logging.getLogger(__name__)


def _dumpFlat(n, parent=None):
    s = ""
    for k, v in n.items():
        me = _appendToParent(parent, k)

        def do_item(me, v):
            t = type(v).__name__
            if t == "Namespace":
                t = "dict"
            if isinstance(v, dict):
                v = Namespace(v)
                s = _dumpFlat(v, me)
            elif type(v) == list:
                s = me + " = " + repr(v).replace('\n', '\\n') + "\n"
                if len(v) > 0:
                    v = v[0]
                    s += do_item(me + "[i]", v)
            else:
                s = me + " = " + repr(v).replace('\n', '\\n') + "\n"
            return s
        s += do_item(me, v)
    return s


@singleton
class Config(object):

    def __init__(self, *args, **kwargs):
        self.cfg = Namespace(*args, **kwargs)

    def dumpFlat(self, parent=None):
        return _dumpFlat(self)

    def merge(self, other):
        self.cfg = mergeDict(self.cfg, other)

    def __getattr__(self, name):
        return getattr(self.cfg, name)


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


def _resolveSqlPath(url):

    sqlite_proto = "sqlite:///"
    if url.startswith(sqlite_proto):
        url = sqlite_proto + _makeFullPath(url[len(sqlite_proto):])
    elif url.startswith('$'):
        url = url[1:]
        log.info("Resolving SQL Url using the environment variable '{}'".format(url))
        url = os.environ[url]

    if sys.platform.startswith("win32"):
        url = url.replace("\\", "\\\\")

    return url


def _resolveEnv(var):
    if var.startswith('$'):
        var = var[1:]
        log.info("Resolving setting '{}' using the environment variables to: {}"
                 .format(var, os.environ[var]))
        var = os.environ[var]
    return var


def updateFullPaths():
    c = Config()
    c.frontend.root_fullpath = _makeFullPath(c.frontend.root_path)
    c.frontend.homepage_fullpath = _makeFullPath(c.frontend.homepage_path)
    c.frontend.doc_fullpath = _makeFullPath(c.frontend.doc_path)
    c.logging.config_file_fullpath = _makeFullPath(c.logging.config_file)
    c.backend.db.full_url = _resolveSqlPath(c.backend.db.url)
    c.backend.backend.mongodb.full_url = _resolveEnv(c.backend.mongodb.url)
    c.backend.db.workdir_fullpath = _makeFullPath(c.backend.db.workdir)
    c.plugins.default_path_fullpath = _makeFullPath(c.plugins.default_path)


def dumpConfigToLogger(level="info"):
    """
    Args:
        level (str, optional): log level. info/debug/warning
    """
    assert level in {'info', 'debug', 'warning'}
    c = Config()
    getattr(log, level)("")
    getattr(log, level)(_("Listing all available keys:"))
    getattr(log, level)(indent(c.dumpFlat()))


def configureFlavor(config_path, flavour):
    if not flavour:
        flavour = "dev"
    log.info("Loading flavor configuration: '{}'".format(flavour))
    config_dir = os.path.dirname(config_path)
    flavour_config_file = os.path.join(config_dir, Config().flavour.config_file.format(flavour=flavour))
    log.info("Configuration file: '{}'".format(flavour_config_file))
    if os.path.exists(flavour_config_file):
        cfg = _loadYaml(flavour_config_file)
        log.info("Loaded flavour data: {}".format(cfg))
        Config().merge(cfg)
    else:
        log.info("No configuration file found")


def initializeConfig(flavour):
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                               os.pardir,
                                               "config.yaml"))
    log.debug("Loading configuration: {}".format(config_path))
    _loadConfig(config_path)
    configureFlavor(config_path, flavour)
    updateFullPaths()
    dumpConfigToLogger()


def unloadConfig():
    Config().unload()
