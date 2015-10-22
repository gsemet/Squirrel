# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json


class Ticker(object):

    '''
    Stock identifier
    '''

    def __init__(self, symbol, exchange):
        self.exchange = exchange
        self.symbol = symbol

    def __str__(self):
        return "Ticker" + json.dumps({"symbol": self.symbol,
                                      "exchange": self.exchange,
                                      })

    def __repr__(self):
        return ("Ticker(symbol={symbol}, exchange={exchange})"
                .format(symbol=self.symbol,
                        exchange=self.exchange,
                        ))

    def __cmp__(self, other):
        return (self.symbol == other.symbol and
                self.exchange == other.exchange)
