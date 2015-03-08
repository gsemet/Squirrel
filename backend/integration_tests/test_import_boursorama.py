from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.unittest import TestCase
from squirrel.model.ticker import Ticker
from squirrel.plugins.importers.boursorama.boursorama import Boursorama

log = logging.getLogger(__name__)


class IntegrationTestBoursorama(TestCase):

    @defer.inlineCallbacks
    def test_GoodTicker_DataIsNotEmpty(self):
        raise NotImplementedError
    test_GoodTicker_DataIsNotEmpty.skip = "not implemented"

    @defer.inlineCallbacks
    def test_BadTicker_ExceptionOccurs(self):
        yield self.assertInlineCallbacksRaises(Exception,
                                               Boursorama().getTicks,
                                               Ticker("BAD_TICKER", "NASDAQ"),
                                               intervalMin=60 * 24,
                                               nbIntervals=2)
    test_BadTicker_ExceptionOccurs.skip = "not implemented"
