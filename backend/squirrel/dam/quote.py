from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

from collections import namedtuple

"""
class Quote(object):
    ''' tick class '''
    def __init__(self, time, open, high, low, close, volume, adjClose):
        ''' constructor '''
        self.time = time
        self.close = float(close)
    def __str__(self):
        ''' convert to string '''
        return json.dumps({"time": self.time,
                           "close": self.close})
    @staticmethod
    def fromStr(string):
        ''' convert from string'''
        d = json.loads(string)
        return Quote(d['time'], d.get('open'), d.get('high'),
                     d.get('low'), d['close'], d.get('volume'), d.get('adjClose'))
"""


class Quote(object):

    ''' tick class '''

    def __init__(self, time, open, high, low, close, volume, adjClose):
        ''' constructor '''
        self.time = time
        self.open = 0 if ("-" == open) else float(open)
        self.high = 0 if ("-" == high) else float(high)
        self.low = 0 if ("-" == low) else float(low)
        self.close = 0 if ("-" == close) else float(close)
        self.volume = int(volume)
        self.adjClose = adjClose

    def __str__(self):
        ''' convert to string '''
        return json.dumps({"time": self.time,
                           "open": self.open,
                           "high": self.high,
                           "low": self.low,
                           "close": self.close,
                           "volume": self.volume,
                           "adjClose": self.adjClose})

    @staticmethod
    def fromStr(string):
        ''' convert from string'''
        d = json.loads(string)
        return Quote(d['time'], d['open'], d['high'],
                     d['low'], d['close'], d['volume'], d['adjClose'])

#Tick = namedtuple('Tick', ' '.join(TICK_FIELDS))
TupleQuote = namedtuple('Quote', ' '.join(QUOTE_FIELDS))
#DateValue = namedtuple('DateValue', 'date, value')
