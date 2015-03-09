from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yapsy.PluginManager import PluginManager

from squirrel.common.singleton import singleton
from squirrel.config.config import Config


@singleton
class PluginRegistry(object):

    def __init__(self):
        self.loadedPlugins = {}

    def loadPlugin(self, pluginPath):
        # Build the manager
        # Tell it the default place(s) where to find plugins
        self.pluginManager = PluginManager()
        self.pluginManager.setPluginPlaces([pluginPath])
        self.pluginManager.setPluginInfoExtension("plugin")
        # Load all plugins
        self.pluginManager.collectPlugins()
        # Loop round the plugins and print their names.
        for plugin in self.pluginManager.getAllPlugins():
            print("Loading plugin {!r}".format(plugin.name))
            print("  Description: {}".format(plugin.description))
            print("  Author: {}".format(plugin.author))
            print("  Website: {}".format(plugin.website))
            print("  Version: {}".format(plugin.version))
            if plugin.plugin_object.name in self.loadedPlugins:
                raise Exception("Plugin {!r} already loaded".format(plugin.name))
            self.loadedPlugins[plugin.plugin_object.name] = plugin.plugin_object

    def get(self, name):
        return self.loadedPlugins[name]


def loadPlugins(forcePluginNames=None):
    plugin_root = Config().plugins.full_default_path
    print("Loading plugin located at: {!r}".format(plugin_root))
    PluginRegistry().loadPlugin(plugin_root)
    # print(glob.glob(os.path.join(plugin_root, "**", "*.py")))

    # for dirName, subdirList, fileList in os.walk(plugin_root, topdown=False):
    #     PluginRegistry().loadPlugin(dirName)


def unloadPlugins():
    PluginRegistry().unload()
