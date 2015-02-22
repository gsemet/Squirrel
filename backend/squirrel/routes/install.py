from squirrel.routes import app


@app.route('/install', methods=['GET'])
def install(request):
    print request.args
    s = "Installing"
    s += ""

    return s
