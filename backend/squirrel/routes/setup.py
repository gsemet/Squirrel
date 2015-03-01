from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from squirrel.routes import app


@app.route('/setup.html', methods=['GET'])
def setup(request):
    print(request.args)
    s = "Setuping your environment"
    s += ""

    return s
