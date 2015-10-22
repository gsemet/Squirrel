# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json


class Stock(object):

    '''
    Stock description
    '''

    def __init__(self,
                 title=None,
                 symbol=None,
                 exchange=None,
                 currency=None
                 ):
        self.title = title
        self.symbol = symbol
        self.exchange = exchange
        self.currency = currency

    def __str__(self):
        return "Stock" + json.dumps({
                                    "title": self.title,
                                    "symbol": self.symbol,
                                    "exchange": self.exchange,
                                    "currency": self.currency,
                                    })

    def __repr__(self):
        return ("Stock(title={title}, symbol={symbol}, exchange={exchange}, currency={currency})"
                .format(
                    title=self.title,
                    symbol=self.symbol,
                    exchange=self.exchange,
                    currency=self.currency,
                ))

    def __cmp__(self, other):
        return (
            self.title == other.title and
            self.symbol == other.symbol and
            self.exchange == other.exchange and
            self.currency == other.currency
        )
