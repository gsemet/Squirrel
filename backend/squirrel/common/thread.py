from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet.threads import deferToThread

InThread = deferToThread.__get__

__all__ = ['InThread']
