from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from treq import get
from twisted.internet import defer

from squirrel.dam.tick import Tick


class GoogleFinance(object):

    @defer.inlineCallbacks
    def _request(self, url):
        print("Requesting url:", url)
        r = yield get(url)
        c = yield r.content()
        defer.returnValue(c)

    @defer.inlineCallbacks
    def getTicks(self, symbol, start, end):
        """
        Get tick prices for the given ticker symbol.
        @symbol: stock symbol
        @interval: interval in mins(google finance only support query till 1 min)
        @start: start date(YYYYMMDD)
        @end: end date(YYYYMMDD)
        start and end is disabled since only 15 days data will show
        @Returns a nested list.
        """
        # TODO, parameter checking
        try:
            #start = string2EpochTime(start)
            #end = string2EpochTime(end)
            #period = end - start
            period = 15
            url = ('http://www.google.com/finance/getprices?'
                   'q={symbol}&i=61&p={period}d&f=d,o,h,l,c,v'.format(symbol=symbol,
                                                                      period=period))
            try:
                page = yield self._request(url)
                print("page", page)
            except Exception:
                raise

            days = page.readlines()[7:]  # first 7 line is document
            # sample values:'a1316784600,31.41,31.5,31.4,31.43,150911'
            values = [day.split(',') for day in days]

            data = []
            for value in values:
                data.append(Tick(value[0][1:].strip(),
                                 value[4].strip(),
                                 value[2].strip(),
                                 value[3].strip(),
                                 value[1].strip(),
                                 value[5].strip()))
            defer.returnValue(data)
        except Exception:
            raise
