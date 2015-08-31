# regexdict
*A normal Python dict, with sugar for regex searching over string keys.*

**CJ Carey** - [perimosocordiae@github](https://github.com/perimosocordiae/)
**Daryl Koopersmith** - [koop@github](https://github.com/koop/), [darylkoop.com](http://darylkoop.com)

## Create a new regexdict

	from regexdict import regexdict

	redict = regexdict({
		'applesauce': 10,
		'grapple': 7,
		'happily': 7
	})

## Use a regex
We use slice syntax as sugar: `redict[ (returnType) : regex ]`

	redict[:'app']    # Matches everything
	redict[:'.app']   # Matches 'grapple' and 'happily'
	redict[:'apple']  # Matches 'applesauce' and 'grapple'

## Specify the return type of the results
If you don't want to use the generator by default, specify another return type.

	from regexdict import return_types as rt

	redict[:'.app']               # Generator over (key, value) pairs
	redict[list:'.app']           # List of (key, value) pairs
	redict[dict:'.app']           # Dict of results
	redict[rt.keys:'.app']        # Sequence of keys (list in python 2, generator in python 3)
	redict[rt.values:'.app']      # Sequence of values (list in python 2, generator in python 3)
	redict[rt.iterkeys:'.app']    # Generator of keys
	redict[rt.itervalues:'.app']  # Generator of values


## Use compiled regexes
We also recognize pre-compiled regexes.

	import re

	app = re.compile('.app')
	redict[:app]

	redict[list:app] == redict[list:'.app']  # ==> True

## The `in` operator
The `in` operator only recognizes compiled regexes and normal key values.
No slice magic here, sorry!

	app in redict  # ==> True
