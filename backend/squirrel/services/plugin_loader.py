from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from yapsy.PluginManager import PluginManager

from squirrel.common.singleton import singleton
from squirrel.config.config import Config
from squirrel.plugin_bases.plugin_importer_base import PluginImporterBase


log = logging.getLogger(__name__)


@singleton
class PluginRegistry(object):

    CATEGORIES_BASECLASS = {
        "Import": PluginImporterBase,
        "Visualisation": None,
    }

    def __init__(self):
        self.loadedPlugins = {}
        self.pluginManager = PluginManager()
        self.pluginManager.setPluginInfoExtension("plugin")
        # Define the various categories corresponding to the different
        # kinds of plugins you have defined
        self.pluginManager.setCategoriesFilter(self.CATEGORIES_BASECLASS)

    def loadPlugin(self, pluginPaths):
        assert isinstance(pluginPaths, list), "pluginPaths should be a list!"
        # Build the manager
        # Tell it the default place(s) where to find plugins
        self.pluginManager.setPluginPlaces(pluginPaths)
        # Load all plugins
        self.pluginManager.collectPlugins()
        # Loop round the plugins and print their names.
        for plugin_info in self.pluginManager.getAllPlugins():
            log.info("Loading plugin {!r}".format(plugin_info.name))
            log.info("  Description: {}".format(plugin_info.description))
            log.info("  Author: {}".format(plugin_info.author))
            log.info("  Website: {}".format(plugin_info.website))
            log.info("  Version: {}".format(plugin_info.version))
            if plugin_info.plugin_object.name in self.loadedPlugins:
                raise Exception("Plugin {!r} already loaded".format(plugin_info.name))
            plugin_info.plugin_object.description = plugin_info.description
            plugin_info.plugin_object.author = plugin_info.author
            plugin_info.plugin_object.website = plugin_info.website
            plugin_info.plugin_object.version = plugin_info.version
            plugin_info.plugin_object.category = plugin_info.category
            self.loadedPlugins[plugin_info.plugin_object.name] = plugin_info.plugin_object

    def getByName(self, name):
        return self.loadedPlugins[name]

    def getPluginNamesByCategory(self, category):
        if category not in self.CATEGORIES_BASECLASS.keys():
            raise ValueError("Invalid category: {!r}. Available: {!r}"
                             .format(category, self.CATEGORIES_BASECLASS.keys()))
        return [plugin_info.name for plugin_info
                in self.pluginManager.getPluginsOfCategory(category)]

    def getAllPlugins(self):
        return self.loadedPlugins.values()


def loadPlugins(forcePluginNames=None):
    plugin_root = Config().plugins.full_default_path
    log.info("Loading plugin located at: {!r}".format([plugin_root]))
    PluginRegistry().loadPlugin([plugin_root])


def unloadPlugins():
    PluginRegistry().unload()
