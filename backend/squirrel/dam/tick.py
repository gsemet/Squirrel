import json

# namedtuple are used to handle data getting from csv or internet
TICK_FIELDS = ['time', 'open', 'high', 'low', 'close', 'volume']
# QUOTE_FIELDS = ['time', 'open', 'high', 'low', 'close', 'volume', 'adjClose']
QUOTE_FIELDS = ['time', 'close', 'volume', 'low', 'high']


class Tick(object):

    ''' tick class '''

    def __init__(self, time=None, open=None, high=None, low=None, close=None, volume=None):
        ''' constructor '''
        self.time = time
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)
        self.volume = int(volume)

    def __str__(self):
        ''' convert to string '''
        return "Tick" + json.dumps({"time": self.time,
                                    "open": self.open,
                                    "high": self.high,
                                    "low": self.low,
                                    "close": self.close,
                                    "volume": self.volume})

    def __repr__(self):
        return ("Tick(time={time}, open={open}, high={high}, low={low}, "
                "close={close}, volume={volume})"
                .format(time=self.time,
                        open=self.open,
                        high=self.high,
                        low=self.low,
                        close=self.close,
                        volume=self.volume,
                        ))

    @staticmethod
    def fromStr(string):
        ''' convert from string'''
        d = json.loads(string)
        return Tick(d['time'], d['open'], d['high'],
                    d['low'], d['close'], d['volume'], d['adjClose'])
