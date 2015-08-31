# regexdict

[![PyPI version](https://badge.fury.io/py/bigO.svg)](http://badge.fury.io/py/bigO)
[![Build Status](https://travis-ci.org/perimosocordiae/bigO.svg?branch=master)](https://travis-ci.org/perimosocordiae/bigO)

*Python dicts with sugar for regular expression searches over keys.*

**CJ Carey** - [perimosocordiae@github](https://github.com/perimosocordiae/)

**Daryl Koopersmith** - [koop@github](https://github.com/koop/)

## Create a new regexdict

The constructor has the same semantics as a regular Python dict.

	from regexdict import regexdict

	redict = regexdict({
		'applesauce': 10,
		'grapple': 7,
		'happily': 7
	})

The resulting object behaves just like a normal dict,
so long as you if you index it with non-slice keys.

## Use a regex
Take advantage of the sugary slice syntax: `redict[:pattern:(flags)]`

	redict[:'app':]      # Matches everything
	redict[:'.app':]     # Matches 'grapple' and 'happily'
	redict[:'apple':]    # Matches 'applesauce' and 'grapple'
	redict[:'HAP':re.I]  # Matches 'happily' due to case insensitivity flag

Regex slice queries return a (possibly empty) iterator of (key, value) pairs.

Patterns may be strings or pre-compiled regex objects.

	import re
	app = re.compile('.app')

	# Same result as redict[:'.app':]
	redict[:app:]


## The `in` operator
The `in` operator only recognizes compiled regexes and normal key values.
No slice magic here, sorry!

	app in redict  # ==> True
