from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json

from squirrel.routes import app
from squirrel.services.plugin_loader import PluginRegistry


@app.route("/api/plugins", methods=['GET'])
def route_plugins(request):
    request.setHeader('Content-Type', 'application/json')

    data = []
    for plugin in PluginRegistry().getAllPlugins():
        data.append({
            "name": plugin.name,
            "author": plugin.author,
            "version": str(plugin.version),
            "description": plugin.description,
            "website": plugin.website,
        })
    return json.dumps(data)
