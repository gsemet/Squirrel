from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Error code matches HTTP error code

# request is successful
SUCCESS = 200
# request failed normally
FAILURE = 401
# an unexpected event occured
EXCEPTION = 501


def resultToString(result):
    if result == SUCCESS:
        return "success"
    elif result == FAILURE:
        return "failure"
    elif result == EXCEPTION:
        return "exception"
    else:
        raise Exception("Invalid result: {!r}".format(result))


def resultToDetail(result):
    if result == SUCCESS:
        return "request successfully received"
    elif result == FAILURE:
        return "error occured during request"
    elif result == EXCEPTION:
        return "unexpected event occured"
    else:
        raise Exception("Invalid result: {!r}".format(result))
