from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from dictns import Namespace
from twisted.internet import defer

from squirrel.common.text import dateTimeToEpoch
from squirrel.common.text import epochTimeStringToDatatime
from squirrel.common.text import getTodayEpoch
from squirrel.model.tick import Tick
from squirrel.model.ticker import Ticker
from squirrel.plugin_bases.plugin_importer_base import PluginImporterBase


class GoogleFinance(PluginImporterBase):

    name = "Google Finance"

    def activate(self):
        pass

    def deactivate(self):
        pass

    @defer.inlineCallbacks
    def getTicks(self, ticker, intervalMin, nbIntervals):
        """
        Get tick prices for the given ticker ticker.

        @param ticker: stock google ticker (ex: 'GOOG:NASDAQS')
        @param intervalMin: interval in mins(google finance only support query till 1 min)
        @param nbIntervals: nb of intervals to retrieve, starting today

        @return a list of tick
        """
        assert isinstance(ticker, Ticker), "ticker should be Ticker"

        DATE = 'd'
        CLOSE = 'c'
        VOLUME = 'v'
        OPEN = 'o'
        CDAYS = 'k'
        HIGH = 'h'
        LOW = 'l'
        interval_sec = intervalMin * 60
        request = Namespace({
            'ticker': ticker.symbol,
            'exchange': ticker.exchange,
            'interval': interval_sec,
            'period': '10Y',
            'format': ",".join([
                DATE,
                OPEN,
                CLOSE,
                VOLUME,
                CDAYS,
                HIGH,
                LOW,
            ]),
            'today': str(getTodayEpoch())
        })

        # Seem like we are only able to retrieve the data from now to a certain interval
        # back in time.
        # GET http://www.google.com/finance/getprices?q=AAPL&x=NASD&i=61&p=10d&f=d,o,h,l,c,v
        # Reference:
        # http://www.google.com/finance/getprices?q=GOOG&x=NASD&i=86400&p=40Y&f=d,o,c,vh&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg
        # https://www.google.com/finance/getprices?q=ARCP&x=NASD&i=604800&p=40Y&f=d,c,v,k,o,h,l&df=cpct&auto=1&ts=1425743161740&ei=QB37VJDLAceCwgOA64CYDA
        # Test:
        # http://www.google.com/finance/getprices?q=AAPL&x=NASD&i=86400&p=40Y&f=d,o,c,v,k,h,l&ts=1425510000
        # Bad ticker
        # http://www.google.com/finance/getprices?q=BADTICKER&x=NASD&i=86400&p=40Y&f=d,o,c,vh&df=cpct&auto=0&ei=Ef6XUYDfCqSTiAKEMg
        #
        # q - Stock symbol
        # x - Stock exchange symbol on which stock is traded (ex: NASD)
        # i - Interval size in seconds (86400 = 1 day intervals)
        # p - Period. (A number followed by a "d" or "Y", eg. Days or years. Ex: 40Y = 40 years.)
        # f - What data do you want? d (date - timestamp/interval, c - close, v - volume, etc...)
        #     Note: Column order may not match what you specify here
        # df - ??
        # auto - ??
        # ei - ??
        # ts - Starting timestamp (Unix format). If blank, it uses today.
        #
        # One tricky bit with the first column (the date column) is the full and partial timestamps.
        # The full timestamps are denoted by the leading 'a'. Like this: a1092945600 The number
        # after the 'a' is a Unix timestamp. (Google it if you're not sure what it is.) The numbers
        # without a leading 'a' are "intervals". So, for example, the second row in the data set
        # below has an interval of 1. You can multiply this number by our interval size (a day, in
        # this example) and add it to the last Unix Timestamp. That gives you the date for the
        # current row. (So our second row is 1 day after the first row. Easy.)

        url = ('http://www.google.com/finance/getprices?'
               'q={request.ticker}&'
               'x={request.exchange}&'
               'i={request.interval}&'
               'p={request.period}&'
               'f={request.format}&'
               'ts={request.today}'
               .format(request=request))
        page = yield self.httpRequest(url)
        page = page.split("\n")

        self.log.debug("len=", len(page))
        if len(page) <= 7:
            self.log.debug("No data, raising")
            raise Exception("No data!")

        column_order = {}
        data = []

        def parse_column_order(line):
            _, _, columns = line.partition('=')
            for i, column_name in enumerate(columns.split(",")):
                column_order[column_name] = i
            self.log.debug("column_order", column_order)
        # using a mutable here or else we cannot set cur_epoch_time from within parse_data
        cur_epoch_time = [0]

        def parse_data(line):
            line = line.strip()
            if len(line) == 0:
                return
            sd = line.split(",")
            self.log.debug("parsing data:", sd)
            t = sd[column_order["DATE"]]
            if t.startswith("a"):
                t = epochTimeStringToDatatime(t[1:])
                cur_epoch_time[0] = dateTimeToEpoch(t)
            else:
                if cur_epoch_time[0] is None:
                    raise Exception("cur_epoch_time[0] is none!")
                t = epochTimeStringToDatatime(cur_epoch_time[0] + int(t) * interval_sec)
            try:
                data.append(Tick(
                    ticker=ticker,
                    date=t,
                    open=sd[column_order["OPEN"]],
                    high=sd[column_order["HIGH"]],
                    low=sd[column_order["LOW"]],
                    close=sd[column_order["CLOSE"]],
                    volume=sd[column_order["VOLUME"]],
                    cdays=sd[column_order["CDAYS"]],
                ))
            except IndexError as e:
                raise IndexError("Cannot parse line: {!r}. Exception: {}".format(line, e))

        in_data = False
        for line in page:
            if line.startswith("COLUMNS"):
                parse_column_order(line)
            if in_data and not line.startswith("TIMEZONE_OFFSET"):
                parse_data(line)
            elif line.startswith("TIMEZONE_OFFSET"):
                in_data = True

        defer.returnValue(data)
