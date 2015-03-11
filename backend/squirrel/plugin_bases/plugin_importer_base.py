from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from dictns import Namespace
from twisted.internet import defer
from yapsy.IPlugin import IPlugin

from squirrel.common.downloader import get

from squirrel.common.text import dateTimeToEpoch
from squirrel.common.text import epochTimeStringToDatatime
from squirrel.common.text import getTodayEpoch
from squirrel.common.text import string2EpochTime
from squirrel.common.text import string2datetime
from squirrel.model.tick import Tick
from squirrel.model.ticker import Ticker


class PluginImporterBase(IPlugin):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    @defer.inlineCallbacks
    def httpRequest(self, url):
        self.log.debug("Requesting url:", url)
        code, content = yield get(url)
        if code != 200:
            raise Exception("Error received: code = {}".format(code))

        defer.returnValue(content)

    def getTodayEpoch(self):
        return getTodayEpoch()

    def dateTimeToEpoch(self, da):
        return dateTimeToEpoch(da)

    def epochTimeStringToDatatime(self, epochString):
        return epochTimeStringToDatatime(epochString)

    def string2EpochTime(self, stingTime, format='%Y-%m-%d'):
        return string2EpochTime(stingTime, format=format)

    def string2datetime(self, stringTime, format='%Y-%m-%d'):
        return string2datetime(stringTime, format=format)

    def createTick(self, *args, **kwargs):
        return Tick(*args, **kwargs)

    def createNamespace(self, data=None):
        if not data:
            data = {}
        return Namespace(data)

    def checkTicker(self, ticker):
        assert isinstance(ticker, Ticker), "ticker should be Ticker"

        # Plugin pattern:

        # ./your_plugin_file_name.py
        # class MyWonderfulImportPlugin(PluginImporterBase):
        #
        #     internal_name = "MyWonderfulImportPlugin"
        #     name = "Human readable wonderful name"
        #
        #    @defer.inlineCallbacks
        #    def getTicks(self, ticker, intervalMin, nbIntervals):
        #          ...
