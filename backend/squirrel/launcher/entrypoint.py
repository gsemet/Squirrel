from crochet import setup, run_in_reactor
from twisted.internet import defer

setup()


@defer.inlineCallbacks
def mainEntryPoint():
    print "I run from a deferred"
    yield defer.succeed(0)


@run_in_reactor
def runInCrochet():
    return mainEntryPoint()


def run():
    runInCrochet()
    return 0
