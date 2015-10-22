# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import zope.interface

from squirrel.interfaces.plugin import IPlugin


class IPluginImporter(IPlugin):

    name = zope.interface.Attribute("""name of your plugin""")
