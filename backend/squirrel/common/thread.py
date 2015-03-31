from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from twisted.internet import threads
from twisted.internet.threads import deferToThread


InThread = deferToThread.__get__


def deferToThread(f):
    '''
    Convert a long-running blocking function into an asynchronous function running in a thread,
    without blocking all other deferreds of the system.

    The calling deferred function can receive the return value of the decorated function.

    Example:

    .. code-block:: python

        @inThread
        def blockingFunction(self):
            ...
            return val

        @defer.inlineCallbacks
        def deferredFunction(self):
            ...
            res = yield blockingFunction()
            ...
    '''
    def decorated(*args, **kwargs):
        return threads.deferToThread(f, *args, **kwargs)
    return decorated

__all__ = ['InThread', 'deferToThread']
