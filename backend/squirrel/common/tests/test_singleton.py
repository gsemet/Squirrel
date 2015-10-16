from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from squirrel.common.singleton import singleton
from squirrel.common.unittest import TestCase


class TestSingleton(TestCase):

    def testSingleton(self):
        @singleton
        class AClass(object):
            data = "old value"

        ref = id(AClass())
        self.assertEqual(AClass().data, "old value")
        self.assertEqual(AClass().data, "old value")
        self.assertEqual(id(AClass()), ref)
        AClass().data = "new value"
        self.assertEqual(AClass().data, "new value")
        self.assertEqual(AClass().data, "new value")

        # new reference uses the changed data
        self.assertEqual(AClass().data, "new value")

        AClass().unload()
        # Second time call should be transparent
        AClass().unload()

        # The next call will create a new instance, should have a different adress
        self.assertEqual(AClass().data, "old value")
        self.assertNotEqual(id(AClass()), ref)

        AClass().unload()

        # New reference create a new instance of AClass
        self.assertEqual(AClass().data, "old value")
        AClass().unload()
