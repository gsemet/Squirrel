from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from mock import Mock
from mock import patch

from squirrel.common.unittest import TestCase
from squirrel.config.config import Config
from squirrel.launcher.entrypoint import run


class TestEntryPoint(TestCase):

    @patch("squirrel.services.serve_backend.app", new=Mock())
    @patch("squirrel.launcher.entrypoint.initializeConfig", new=Mock())
    def testRun(self):
        Config().unload()
        Config({
            'frontend': {
                'root_full_path': 'full/path',
                'port': 'port',
            }
        })
        self.assertEqual(Config().frontend.root_full_path, "full/path")
        run()
