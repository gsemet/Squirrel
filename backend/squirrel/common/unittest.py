from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import sys

from functools import wraps
from twisted.internet import defer
from twisted.trial import unittest


log = logging.getLogger(__name__)


class TestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.disableLogToStdout()

    def assertNotEmpty(self, collec):
        self.assertNotEqual(len(collec), 0, msg="Collection unexpectedly empty")

    @defer.inlineCallbacks
    def assertInlineCallbacksRaises(self, exceptionClass, deferred, *args, **kwargs):
        yield self.assertFailure(deferred(*args, **kwargs), exceptionClass)

    def assertLengthEquals(self, collection, length):
        self.assertEqual(len(collection), length, msg="Invalid lenght. Expecting: {}. Got: {}"
                         .format(length, len(collection)))

    def enableLogging(self, level=logging.DEBUG):
        self.rootLogger = logging.getLogger()
        self.oldLoggingLevel = self.rootLogger.getEffectiveLevel()
        self.rootLogger.setLevel(level)

        self.streamHandler = logging.StreamHandler(sys.stdout)
        self.streamHandler.setLevel(level)
        # Complete format <date> - <module name> - <level> - <message>:
        #   '%(asctime)s - %(name)-40s - %(levelname)-7s - %(message)s'
        formatter = logging.Formatter('%(name)-45s - %(levelname)-7s - %(message)s')
        self.streamHandler.setFormatter(formatter)
        self.rootLogger.addHandler(self.streamHandler)

        # Simply write an empty string, in order to be sure the first line starts at the
        # beginning of the line
        sys.stdout.write("\n")

    def disableLogging(self):
        self.rootLogger.removeHandler(self.streamHandler)
        self.rootLogger.setLevel(self.oldLoggingLevel)

    @classmethod
    def verboseLogging(cls, level=logging.DEBUG):
        # Overwrite XTestCase.verboseLogging with deferred support
        '''
        I enable full logging for the given function or methods. This is extremely useful in order
        to enable full log only for a simple test case during debugging, and don't display them
        during normal execution.

        Simply comment in or out the decorator in order to enable or disable the log display

        Example:

        .. code-block:: python

            class TestClass(TxTestCase):

                @TxTestCase.verboseLogging()
                def testNormalTest(self):
                    ...

                @TxTestCase.verboseLogging()
                @defer.inlineCallbacks
                def testInlineCallbacksTest(self):
                    ...


                @TxTestCase.verboseLogging()
                @patch("patch.this.object")
                @defer.inlineCallbacks
                def testWithPatchAndInlineCallbacksTest(self):
                    ...
        '''

        def decorator(func):
            @wraps(func)
            def impl(*args, **kwargs):
                # In order to reuse the enableLogging, we need a self to store some values in it,
                # but we are in a classmethod (verboseLogging is a method decorator). I don't want
                # to store the value in the class object, so I create a temporary object named self,
                # used in order to execute the enableLogging method.
                self = TestCase()
                TestCase.enableLogging(self)
                log.info("Log to stdout enabled")

                try:
                    res = func(*args, **kwargs)
                finally:
                    log.info("Log to stdout disabled")
                    TestCase.disableLogging(self)
                return res
            return impl
        return decorator

    def disableLogToStdout(self):
        '''
        I disable the output of the loggings to the console by filtering all logs out.
        '''
        root = logging.getLogger()
        root.setLevel(logging.CRITICAL + 1)
