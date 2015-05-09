from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from mock import Mock
from mock import patch

from squirrel.common.unittest import TestCase
from squirrel.launcher.squirrel_dev import run as run_dev
from squirrel.launcher.squirrel_prod import run as run_prod
from squirrel.services.config import Config


class TestEntryPoint(TestCase):

    @patch("squirrel.services.serve_backend.app", new=Mock())
    @patch("squirrel.launcher.common.initializeConfig", new=Mock())
    @patch("squirrel.launcher.common.setupLogger", new=Mock())
    @patch("squirrel.launcher.common.loadPlugins", new=Mock())
    @patch("squirrel.launcher.common.createWorkdirs", new=Mock())
    def testRunProd(self):
        Config().unload()
        Config({
            'frontend': {
                'root_fullpath': 'full/path',
                'port': '1234',
            },
            'crawlers': {},
        })
        self.assertEqual(Config().frontend.root_fullpath, "full/path")
        run_prod()

    @patch("squirrel.services.serve_backend.app", new=Mock())
    @patch("squirrel.launcher.common.initializeConfig", new=Mock())
    @patch("squirrel.launcher.common.setupLogger", new=Mock())
    @patch("squirrel.launcher.common.loadPlugins", new=Mock())
    @patch("squirrel.launcher.common.createWorkdirs", new=Mock())
    def testRunDev(self):
        Config().unload()
        Config({
            'frontend': {
                'root_fullpath': 'full/path',
                'port': '1234',
            },
            'crawlers': {},
        })
        self.assertEqual(Config().frontend.root_fullpath, "full/path")
        run_dev()
