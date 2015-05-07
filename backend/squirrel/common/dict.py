from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def mergeDict(a, b, path=None, prefix=None, raiseOnConflict=False):
    '''
    http://stackoverflow.com/questions/7204805/dictionaries-of-dictionaries-merge
    merges b into a
    '''
    if path is None:
        path = []
    if prefix:
        r_prefix = prefix + "."
    else:
        r_prefix = ""
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                mergeDict(a[key], b[key], path + [str(key)],
                          prefix=prefix, raiseOnConflict=raiseOnConflict)
            elif a[key] == b[key]:
                pass  # same leaf value
            else:
                if raiseOnConflict:
                    raise Exception('Conflict at {}{}'.format(r_prefix,
                                                              '.'.join(path + [str(key)])))
                else:
                    a[key] = b[key]
        else:
            a[key] = b[key]
    return a
