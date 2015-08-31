import sys

if sys.version_info.major == 2:
  from regexdict import regexdict
else:
  from regexdict_py3k import regexdict
