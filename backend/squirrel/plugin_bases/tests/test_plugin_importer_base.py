import unittest

from squirrel.plugin_bases.plugin_importer_base import PluginImporterBase


class TestPluginImporterBase(unittest.TestCase):

    def testRepairString(self):
        PluginImporterBase()
        s = u'Brookfield Incorpora\xe7\xf5es SA'
        # Cannot convert directory to str
        self.assertRaises(UnicodeError, str, s)
        self.assertEqual("Brookfield Incorpora??es SA", s.encode('ascii', 'replace'))
        self.assertEqual("Brookfield Incorporaes SA", s.encode('ascii', 'ignore'))

    def testEncode(self):
        s = u'"[(exchange == \x22EPA\x22) \x26'
        self.assertEqual('"[(exchange == "EPA") &', s.encode('ascii', 'replace'))

    def testTransformEncode(self):
        s = '\n"num_all_results" : "",\n"original_query" : "[(exchange == \\x22EPA\\x22)'
        self.assertEqual(
            u'\n"num_all_results" : "",\n"original_query" : "[(exchange == \\x22EPA\\x22)',
            unicode(s, 'utf8'))
