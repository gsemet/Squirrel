from squirrel.common.unittest import TestCase
from squirrel.config.config import Config


class TestConfig(TestCase):

    def testSingleton(self):
        Config()
        Config().unload()
