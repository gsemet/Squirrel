from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum as libenum


class Enum(libenum.Enum):
    # I return the literal representation on str()
    # Doc:
    # http://stackoverflow.com/questions/24487405/python-enum-getting-value-of-enum-on-string-conversion

    def __str__(self):
        return str(self.value)

__all__ = ['Enum']
