"""regexdict_py3k.py : Python3-compatible version of regexdict.py

CJ Carey - perimosocordiae@github
Daryl Koopersmith - koop@github, darylkoop.com
"""

import re

keys = lambda seq: (k for k,v in seq)
values = lambda seq: (v for k,v in seq)
# >_>
list = list
dict = dict
# <_<
rtype = type(re.compile(''))

class regexdict(dict):

    @staticmethod
    def _unslice(key):
        if type(key) is slice:
            # re.compile won't re-compile a regex :-)
            return key.start, re.compile(key.stop) # omg hax
        return None, None

    @staticmethod
    def _search(regex,s):
        try:
            return regex.search(s)
        except TypeError:
            return None

    def __contains__(self,key):
        if type(key) == rtype:
            return any(True for k in self.keys() \
                        if regexdict._search(key,k))
        else:
            return dict.__contains__(self,key)

    def __getitem__(self,key):
        rettype, regex = regexdict._unslice(key)
        if regex:
            kv_iter = ((k,v) for k,v in self.items() \
                        if regexdict._search(regex,k))
            return rettype(kv_iter) if rettype else kv_iter
        else:
            return dict.__getitem__(self,key)

    def __apply_to_matches(self,func,*args):
        _, regex = regexdict._unslice(args[0])
        if regex:
            for k in self.keys():
                if regexdict._search(regex,k):
                    func(self,*args)
        else:
            if type(args[0]) is str:
                func(self,*args)
    
    def __setitem__(self,key,value):
        self.__apply_to_matches(dict.__setitem__,key,value)

    def __delitem__(self,key):
        self.__apply_to_matches(dict.__delitem__,key)

