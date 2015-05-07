from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def mergeDict(a, b, path=None):
    '''
    http://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
    merges b into a
    '''
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                mergeDict(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a
