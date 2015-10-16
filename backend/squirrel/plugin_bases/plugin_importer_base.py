from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import re
import sys

from dictns import Namespace
from six.moves.urllib.parse import urlencode
from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet.interfaces import IProtocol
from twisted.internet.protocol import ClientCreator
from twisted.protocols.ftp import FTPClient
from twisted.protocols.ftp import FileConsumer
from yapsy.IPlugin import IPlugin as YapsyIPlugin
from zope.interface import implements

from squirrel.common.downloader import get
from squirrel.common.text import dateTimeToEpoch
from squirrel.common.text import epochTimeStringToDatatime
from squirrel.common.text import getTodayEpoch
from squirrel.common.text import string2EpochTime
from squirrel.common.text import string2datetime
from squirrel.model.stock import Stock
from squirrel.model.tick import Tick
from squirrel.model.ticker import Ticker

log = logging.getLogger(__name__)


class PluginImporterBase(YapsyIPlugin):

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

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    @defer.inlineCallbacks
    def httpRequest(self, url):
        self.log.debug("Requesting url: %s", url)
        code, content = yield get(url)
        self.log.debug("Received response: %s", code)
        if code != 200:
            raise Exception("Error received: code = {}".format(code))

        defer.returnValue(content)

    @defer.inlineCallbacks
    def ftpRequest(self, url):
        log.debug("creating ftpclient")
        ftpClient = FTPClient()
        log.debug("opening file aaa")

        FTPClient.debug = True
        log.debug("creating ClientCreator")
        creator = ClientCreator(reactor, FTPClient)
        log.debug("creating ftpclient")
        ftpClient = yield creator.connectTCP("ftp.nasdaqtrader.com", 21)

        class FTPFile(object):

            """
            A consumer for FTP input that writes data to a file.

            @ivar filename: a filename to be opened for writing.
            """

            implements(IProtocol)

            def __init__(self, filename):
                self.fObj = None
                self.filename = filename

            def makeConnection(self, transport):
                self.fObj = open(self.filename, 'wb')
                log.info('Opened %s for writing', self.filename)

            def connectionLost(self, reason):
                self.fObj.close()
                log.info('Closed %s', self.filename)

            def dataReceived(self, bytes):
                self.fObj.write(bytes)

        with open("aaaa", "w") as f:
            log.debug("retrieveFile")
            yield defer.succeed(0)
            fc = FileConsumer(f)
            yield ftpClient.retrieveFile(url, fc)
            fc.close()
        ftpClient.close()

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

    def createStock(self, *args, **kwargs):
        return Stock(*args, **kwargs)

    def createNamespace(self, data=None):
        if not data:
            data = {}
        return Namespace(data)

    def checkTicker(self, ticker):
        assert isinstance(ticker, Ticker), "ticker should be Ticker"

    def jsonDecode(self, data):
        return json.loads(data)

    def fixHexEscapeString(self, data):
        '''
        Use this method if the data you received contains invalid sequence such as "\\x22"
        that fails json parsing.
        '''
        invalid_escape = re.compile(r"\\x([0-9a-zA-Z]{2})")  # up to 3 digits for byte values up to FF

        def replace_with_byte(match):
            return "%0x" + match.group(1)

        def repair(brokenjson):
            return invalid_escape.sub(replace_with_byte, brokenjson)
        data = repair(data)
        return data

    def flushStd(self):
        '''
        Force flush on standard output and error output.
        Can help debugging
        '''
        sys.stdout.flush()
        sys.stderr.flush()

    def urlencode(self, query):
        """Encode a sequence of two-element tuples or dictionary into a URL query string.

        If any values in the query arg are sequences and doseq is true, each
        sequence element is converted to a separate parameter.

        If the query arg is a sequence of two-element tuples, the order of the
        parameters in the output will match the order of parameters in the
        input.
        """
        return urlencode(query)
