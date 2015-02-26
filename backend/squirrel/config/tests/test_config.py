from squirrel.config.config import Config
from squirrel.common.unittest import TestCase


class TestConfig(TestCase):

    def testSingleton(self):
        Config()
        Config().unload()
