from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import defer
from squirrel.plugin_bases.plugin_importer_base import PluginImporterBase


class YahooFinance(PluginImporterBase):

    name = "Yahoo Finance"

    def activate(self):
        pass

    def deactivate(self):
        pass

    @defer.inlineCallbacks
    def getTicks(self, ticker, stateData, endData):
        """
        Get historical prices for the given ticker symbol.
        Date format is 'YYYY-MM-DD'

        Returns a list or Tick.
        """
        start = str(stateData).replace('-', '')
        end = str(endData).replace('-', '')
        symbol = ticker.symbol
        request = self.createNamespace({
            'symbol': symbol,
            "from_month": str(int(start[4:6]) - 1),
            "from_day":  str(int(start[6:8])),
            "from_year": str(int(start[0:4])),
            "to_month": str(int(end[4:6]) - 1),
            "to_day": str(int(end[6:8])),
            "to_year": str(int(end[0:4])),
        })

        url = ('http://ichart.yahoo.com/table.csv?s={request.symbol}&'
               'a={request.from_month}&'
               'b={request.from_day}&'
               'c={request.from_year}&'
               'g=d&'
               'd={request.to_month}&'
               'e={request.to_day}&'
               'f={request.to_year}&'
               'ignore=.csv').format(request=request)
        days = yield self.httpRequest(url)
        days = days.split("\n")
        self.log.debug("days", days)
        # sample values:[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Clos'], \
        #              ['2009-12-31', '112.77', '112.80', '111.39', '111.44', '90637900', '109.7']...]
        data = []
        for values in days[1:]:
            splitted_value = values.split(",")
            if len(splitted_value) != 7:
                continue
            data.append(self.createTick(ticker=ticker,
                                        date=self.string2EpochTime(splitted_value[0]),
                                        open=splitted_value[1],
                                        high=splitted_value[2],
                                        low=splitted_value[3],
                                        close=splitted_value[4],
                                        volume=splitted_value[5],
                                        cdays=splitted_value[6]))

        dateValues = sorted(data, key=lambda q: q.date)
        defer.returnValue(dateValues)
