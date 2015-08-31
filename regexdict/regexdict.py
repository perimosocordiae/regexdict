"""regexdict.py - Dictionary with support for regular expression searching.

CJ Carey - perimosocordiae@github
Daryl Koopersmith - koop@github
"""
import re
import sys
from collections import namedtuple

iterkeys = lambda seq: (k for k, v in seq)
itervalues = lambda seq: (v for k, v in seq)
if sys.version_info[0] == 2:
    keys = lambda seq: list(iterkeys(seq))
    values = lambda seq: list(itervalues(seq))
else:
    keys, values = iterkeys, itervalues

_RT = namedtuple('ReturnType', ('list', 'dict', 'keys', 'values',
                                'iterkeys', 'itervalues'))
return_types = _RT(list, dict, keys, values, iterkeys, itervalues)


class regexdict(dict):

    def __filter_matches(self, regex):
        return (k for k in self if _is_match(regex, k))

    def __contains__(self, key):
        if not hasattr(key, 'search'):
            return dict.__contains__(self, key)
        return any(True for _ in self.__filter_matches(key))

    def __getitem__(self, key):
        rettype, regex = _unslice(key)
        if regex is None:
            return dict.__getitem__(self, key)
        kv_iter = ((k, dict.__getitem__(self, k))
                   for k in self.__filter_matches(regex))
        return rettype(kv_iter) if rettype else kv_iter

    def __setitem__(self, key, value):
        _, regex = _unslice(key)
        if regex is None:
            return dict.__setitem__(self, key, value)
        for k in self.__filter_matches(regex):
            dict.__setitem__(self, k, value)

    def __delitem__(self, key):
        _, regex = _unslice(key)
        if regex is None:
            return dict.__delitem__(self, key)
        for k in self.__filter_matches(regex):
            dict.__delitem__(self, k)

    # Python2 compatibility functions
    def __getslice__(self, start, stop):
        return self.__getitem__(slice(start, stop))

    def __setslice__(self, start, stop):
        return self.__setitem__(slice(start, stop))

    def __delslice__(self, start, stop):
        return self.__delitem__(slice(start, stop))


def _unslice(key):
    if isinstance(key, slice):
        # slices have the form ret_type:regex
        return key.start, re.compile(key.stop)
    return None, None


def _is_match(regex, s):
    try:
        return regex.search(s) is not None
    except TypeError:
        return False
