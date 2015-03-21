from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import requests
import treq

from twisted.internet import defer
from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.internet.tcp import Client
from twisted.web.client import HTTPConnectionPool
from txrequests import Session


enable_txrequest = True

log = logging.getLogger(__name__)


def download(remote_url, local_path):
    r = requests.get(remote_url)
    f = open(local_path, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


def prepareReactorForUnitTest_txrequest(test):
    pass


def prepareReactorForUnitTest_treq(test):

    def _check_fds(_):
        # This appears to only be necessary for HTTPS tests.
        # For the normal HTTP tests then closeCachedConnections is
        # sufficient.
        fds = set(reactor.getReaders() + reactor.getReaders())
        if not [fd for fd in fds if isinstance(fd, Client)]:
            return

        return deferLater(reactor, 0, _check_fds, None)

    return test.pool.closeCachedConnections().addBoth(_check_fds)


def cleanupReactorForUnitTest_txrequest(test):
    pass


def cleanupReactorForUnitTest_treq(test):
    test.pool = HTTPConnectionPool(reactor, False)


def get_treq(url):
    log.debug("treq: {}".format(url))
    d = treq.get(url)

    @d.addCallback
    def cb(r):
        log.debug("Callback :{!r}".format(r))
        return treq.text_content(r)

    return d


@defer.inlineCallbacks
def get_txrequest(url):
    with Session() as session:
        response = yield session.get(url)
        defer.returnValue((response.status_code, response.content))

if enable_txrequest:
    get = get_txrequest
    prepareReactorForUnitTest = prepareReactorForUnitTest_txrequest
    cleanupReactorForUnitTest = cleanupReactorForUnitTest_txrequest
else:
    get = get_treq
    prepareReactorForUnitTest = prepareReactorForUnitTest_treq
    cleanupReactorForUnitTest = cleanupReactorForUnitTest_treq
