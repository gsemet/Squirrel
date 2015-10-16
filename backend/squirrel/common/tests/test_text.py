from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from squirrel.common.text import dedent
from squirrel.common.text import indent
from squirrel.common.unittest import TestCase


class TestText(TestCase):

    def testDedent(self):
        self.assertEqual("1\n  2\n3", dedent("  1\n    2\n  3"))
        self.assertEqual("1\n  2\n3", dedent("\n  1\n    2\n  3"))

    def testIndent(self):
        self.assertEqual("  indented text", indent("indented text"))
        self.assertEqual("  indented text\n  indented second line",
                         indent("indented text\nindented second line"))

    def testIndentButFirstLine(self):
        self.assertEqual("indented text", indent("indented text", firstLine=False))
        self.assertEqual("indented text\n  indented second line",
                         indent("indented text\nindented second line", firstLine=False))
