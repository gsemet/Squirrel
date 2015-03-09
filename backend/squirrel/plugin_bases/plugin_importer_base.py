from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import yapsy

from twisted.internet import defer

from squirrel.common.downloader import get


class PluginImporterBase(yapsy.IPlugin.IPlugin):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    @defer.inlineCallbacks
    def httpRequest(self, url):
        self.log.debug("Requesting url:", url)
        code, content = yield get(url)
        if code != 200:
            raise Exception("Error received: code = {}".format(code))

        defer.returnValue(content)

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
