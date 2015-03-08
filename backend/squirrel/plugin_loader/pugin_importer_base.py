from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from twisted.internet import defer

from squirrel.common.downloader import get


class PluginImporterBase(object):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    @defer.inlineCallbacks
    def httpRequest(self, url):
        self.log.debug("Requesting url:", url)
        code, content = yield get(url)
        if code != 200:
            raise Exception("Error received: code = {}".format(code))

        defer.returnValue(content)
