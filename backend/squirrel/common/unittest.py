from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import defer
from twisted.trial.unittest import TestCase


class TestCase(TestCase):

    def assertNotEmpty(self, collec):
        self.assertNotEqual(len(collec), 0, msg="Collection unexpectedly empty")

    @defer.inlineCallbacks
    def assertInlineCallbacksRaises(self, exceptionClass, deferred, *args, **kwargs):
        yield self.assertFailure(deferred(*args, **kwargs), exceptionClass)
