import sys
from collections import namedtuple

if sys.version_info.major == 2:
  from regexdict import regexdict, keys, values, iterkeys, itervalues
else:
  from regexdict_py3k import regexdict, keys, values
  iterkeys, itervalues = keys, values

__all__ = ['regexdict', 'return_types']

_RT = namedtuple('ReturnType', ('list', 'dict', 'keys', 'values',
                                'iterkeys', 'itervalues'))

return_types = _RT(list, dict, keys, values, iterkeys, itervalues)
