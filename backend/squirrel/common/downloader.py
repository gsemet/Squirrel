from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests

import treq

from twisted.internet import defer
from txrequests import Session

enable_txrequest = False


def download(remote_url, local_path):
    r = requests.get(remote_url)
    f = open(local_path, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


@defer.inlineCallbacks
def get_treq(url):
    r = yield treq.get(url)
    c = yield treq.text_content(r)
    defer.returnValue((r.code, c))


@defer.inlineCallbacks
def get_txrequest(url):
    with Session() as session:
        response = yield session.get(url)
        defer.returnValue((response.status_code, response.content))

if enable_txrequest:
    get = get_txrequest
else:
    get = get_treq
