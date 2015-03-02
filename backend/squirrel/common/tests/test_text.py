from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.common.text import dedent
from squirrel.common.unittest import TestCase


class TestText(TestCase):

    def testDedent(self):
        self.assertEqual(dedent("  1\n    2\n  3"), "1\n  2\n3")
        self.assertEqual(dedent("\n  1\n    2\n  3"), "1\n  2\n3")
