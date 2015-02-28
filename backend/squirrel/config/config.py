import yaml

from dictns import Namespace
from dictns import documentNamespace

from squirrel.common.singleton import singleton


@singleton
class Config(Namespace):

    def __init__(self, dic=None):
        if dic is None:
            dic = {}
        Namespace.__init__(self, dic)

    def _loadYaml(self, yamlPath):
        with open(yamlPath) as f:
            return yaml.load(f)

    def loadConfig(self, configPath):
        cfg = self._loadYaml(configPath)
        self.update(cfg)

    def unload(self):
        self .clear()

    def documentNamespace(self):
        return documentNamespace(self)
