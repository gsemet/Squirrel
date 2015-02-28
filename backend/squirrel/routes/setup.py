from squirrel.routes import app


@app.route('/setup.html', methods=['GET'])
def setup(request):
    print request.args
    s = "Setuping your environment"
    s += ""

    return s
