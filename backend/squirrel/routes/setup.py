from squirrel.routes import app


@app.route('/setup.html', methods=['GET'])
def install(request):
    print request.args
    s = "Setuping your environment"
    s += ""

    return s
