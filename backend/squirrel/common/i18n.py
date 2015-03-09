from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Documentation:
# http://www.wefearchange.org/2012/06/the-right-way-to-internationalize-your.html

import gettext
import sys


def setupI18n():
    kwargs = {}
    if sys.version_info[0] < 3:
        # In Python 2, ensure that the _() that gets installed into built-ins
        # always returns unicodes.  This matches the default behavior under Python
        # 3, although that keyword argument is not present in the Python 3 API.
        kwargs['unicode'] = True

    gettext.install("Squirrel", unicode=True)

from gettext import gettext as _

__all__ = ["_"]
