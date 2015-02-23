from squirrel.routes import app
from squirrel.routes import *


def run():
    print "Loading configuration"
    print "Connecting to DB"
    print "Starging web service on 8080"
    app.run("localhost", 8080)
