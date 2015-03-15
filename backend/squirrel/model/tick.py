from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

from squirrel.model.ticker import Ticker

# namedtuple are used to handle data getting from csv or internet
TICK_FIELDS = ['date', 'open', 'high', 'low', 'close', 'volume']
# QUOTE_FIELDS = ['date', 'open', 'high', 'low', 'close', 'volume', 'cdays']
QUOTE_FIELDS = ['date', 'close', 'volume', 'low', 'high']


class Tick(object):

    '''
    Given stock value at a given date
    '''

    def __init__(self, ticker=None, date=None, open=None, high=None, low=None,
                 close=None, volume=None, cdays=None):
        ''' constructor '''
        assert isinstance(ticker, Ticker), "ticker should be Ticker"
        self.ticker = ticker
        self.date = date
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = int(volume)
        self.cdays = bool(cdays)

    def __str__(self):
        ''' convert to string '''
        return "Tick" + json.dumps({"ticker": self.ticker,
                                    "date": self.date,
                                    "open": self.open,
                                    "high": self.high,
                                    "low": self.low,
                                    "close": self.close,
                                    "volume": self.volume,
                                    "cdays": self.cdays,
                                    })

    def __repr__(self):
        return ("Tick(ticker={ticker}, date={date}, open={open}, high={high}, low={low}, "
                "close={close}, volume={volume}, cdays={cdays})"
                .format(ticker=self.ticker,
                        date=self.date,
                        open=self.open,
                        high=self.high,
                        low=self.low,
                        close=self.close,
                        volume=self.volume,
                        cdays=self.cdays,
                        ))

    def __cmp__(self, other):
        return (self.ticker == other.ticker and
                self.date == other.date and
                self.open == other.open and
                self.high == other.high and
                self.low == other.low and
                self.close == other.close and
                self.volume == other.volume and
                self.cdays == other.cdays)

    @staticmethod
    def fromStr(string):
        ''' convert from string'''
        d = json.loads(string)
        return Tick(d['date'], d['open'], d['high'],
                    d['low'], d['close'], d['volume'], d['cdays'])

    @property
    def symbol(self):
        return self.ticker.symbol

    @property
    def exchange(self):
        return self.ticker.exchange
