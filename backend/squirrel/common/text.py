from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from textwrap import dedent as textwrap_dedent

__all__ = ['dedent']


def dedent(text):
    return textwrap_dedent(text).lstrip()
