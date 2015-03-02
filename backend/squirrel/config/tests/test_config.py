from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from dictns import Namespace

from squirrel.common.unittest import TestCase
from squirrel.config.config import Config


class TestConfig(TestCase):

    def testSingleton(self):
        Config()
        # Config().unload()

    def testNamespace(self):
        s = Namespace({'a': {'b': {'c': 'd'}}})
        self.assertEqual(s.a.b.c, 'd')
