from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.common.i18n import _

from squirrel.routes import app


@app.route('/setup', methods=['GET'])
def setup(request):
    print(request.args)
    s = _("Setuping your environment")
    s += ""

    return s
