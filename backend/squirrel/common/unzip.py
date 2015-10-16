from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import zipfile


def unzip(local_zip, extract_dir):
    with zipfile.ZipFile(local_zip, "r") as z:
        z.extractall(extract_dir)
