from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import defer

from squirrel.plugin_bases.plugin_importer_base import PluginImporterBase


class NasdaqList(PluginImporterBase):

    name = "Nasdaq List"

    def activate(self):
        pass

    def deactivate(self):
        pass

    @defer.inlineCallbacks
    def getList(self):
        # http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
        # http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download
        # ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt
        # http://stackoverflow.com/questions/5246843/how-to-get-a-complete-list-of-ticker-symbols-from-yahoo-finance

        print("ftp request")
        data = yield self.ftpRequest("ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt")
        self.log.info("data: {!r}".format(data))
        # Parse HTML page:
        # http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download
        # http://www.nasdaq.com/quotes/djia-stocks.aspx
