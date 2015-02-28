from mock import Mock
from mock import patch

from squirrel.common.unittest import TestCase
from squirrel.launcher.entrypoint import run


class TestEntryPoint(TestCase):

    @patch("squirrel.launcher.entrypoint.app", new=Mock())
    def testRun(self):
        run()
