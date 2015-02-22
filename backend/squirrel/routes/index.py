from squirrel.routes import app


@app.route('/', methods=['GET'])
def get_index(request):
    return "Installation not performed: <a href='/install'>click here to install</a>"
