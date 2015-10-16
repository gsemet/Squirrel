from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Receipe:
# http://code.activestate.com/recipes/131499-observer-pattern/
#
# This is a Python implementation of the observer pattern described by Gamma et. al. It defines a
# one-to many dependency between objects so that when one object changes state, all its dependents
# are notified and updated automatically.
#
# The example should output: Setting Data 1 = 10 DecimalViewer: Subject Data 1 has data 10
# HexViewer: Subject Data 1 has data 0xa Setting Data 2 = 15 HexViewer: Subject Data 2 has data 0xf
# DecimalViewer: Subject Data 2 has data 15 Setting Data 1 = 3 DecimalViewer: Subject Data 1 has
# data 3 HexViewer: Subject Data 1 has data 0x3 Setting Data 2 = 5 HexViewer: Subject Data 2 has
# data 0x5 DecimalViewer: Subject Data 2 has data 5 Detach HexViewer from data1 and data2. Setting
# Data 1 = 10 DecimalViewer: Subject Data 1 has data 10 Setting Data 2 = 15 DecimalViewer: Subject
# Data 2 has data 15


class Observer(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
