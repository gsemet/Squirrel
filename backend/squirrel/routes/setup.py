from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import i18n

from squirrel.routes import app

_ = i18n.language.gettext


@app.route('/setup', methods=['GET'])
def setup(request):
    print(request.args)
    s = _("Setuping your environment")
    s += ""

    return s
