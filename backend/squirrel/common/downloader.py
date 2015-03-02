from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests


def download(remote_url, local_path):
    r = requests.get(remote_url)
    f = open(local_path, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return
