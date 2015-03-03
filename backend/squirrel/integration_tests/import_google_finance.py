from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import defer

from squirrel.common.unittest import TestCase
from squirrel.dam.google_finance import GoogleFinance


class IntegrationTest(TestCase):

    @defer.inlineCallbacks
    def testGoogleFinance(self):
        r = yield GoogleFinance().getTicks("AAPL", 1, 1)
        print(r)
