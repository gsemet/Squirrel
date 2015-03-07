from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests

from twisted.internet import defer
from txrequests import Session


def download(remote_url, local_path):
    r = requests.get(remote_url)
    f = open(local_path, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


@defer.inlineCallbacks
def get(url):
    with Session() as session:
        response = yield session.get(url)
        defer.returnValue((response.status_code, response.content))
