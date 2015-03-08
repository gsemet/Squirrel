from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import logging

from twisted.internet import defer


log = logging.getLogger(__name__)


class Boursorama(object):

    @defer.inlineCallbacks
    def getTicks(self, ticker, exchange, intervalMin, nbIntervals):
        """
        Get tick prices for the given ticker ticker.

        @param ticker: stock google ticker (ex: 'GOOG')
        @param exchnage: stock exchnage (ex: 'NASD')
        @param intervalMin: interval in mins(google finance only support query till 1 min)
        @param nbIntervals: nb of intervals to retrieve, starting today

        @return a list of tick
        """
        raise NotImplementedError
