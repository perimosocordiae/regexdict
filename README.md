# regexdict.py
*A normal Python dict, with sugar for regex searching over string keys.*

**CJ Carey** - [perimosocordiae@github](https://github.com/perimosocordiae/)  
**Daryl Koopersmith** - [koop@github](https://github.com/koop/), [darylkoop.com](http://darylkoop.com)

## Create a new regexdict

	import regexdict as r

	redict = r.regexdict({
		'applesauce' : 10,
		'grapple' : 7,
		'happily' : 7
	});

## Use a regex
We use slice syntax as sugar: `redict[ (returnType) : regex ]`

	redict[:'app']		# Matches everything
	redict[:'.app']		# Matches 'grapple' and 'happily'
	redict[:'apple']	# Matches 'applesauce' and 'grapple'

## Specify the return type of the results
If you don't want to use the generator by default, specify another return type.

	redict[:'.app']				# Generator over (key, value) pairs
	redict[ r.list :'.app'] 	# List of (key, value) pairs
	redict[ r.dict :'.app'] 	# Dict of results
	redict[ r.keys :'.app'] 	# Sequence of keys (a list in python 2, a generator in python 3)
	redict[ r.values :'.app'] 	# Sequence of values (a list in python 2, a generator in python 3)


## Use compiled regexes
We also recognize pre-compiled regexes.

	import re
	
	app = re.compile('.app')
	redict[:app]
	
	redict[ r.list :app] == redict[ r.list :'.app'] # True

## The `in` keyword
The in keyword only recognizes compiled regexes and normal key values. No slice magic here, sorry!

	app in redict # True


	