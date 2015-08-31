import unittest
import re
import types

from regexdict import regexdict


class TestRegexDict(unittest.TestCase):
  def setUp(self):
    self.base_dict = {
        'applesauce': 10,
        'grapple': 7,
        'happily': 7
    }

  def test_construction(self):
    redict = regexdict(self.base_dict)
    self.assertEqual(len(redict), 3)
    self.assertDictEqual(redict, self.base_dict)

  def test_slice_syntax(self):
    redict = regexdict(self.base_dict)
    self.assertListEqual(sorted(redict[:'app']),
                         [('applesauce', 10), ('grapple', 7), ('happily', 7)])
    self.assertListEqual(sorted(redict[:'.app']),
                         [('grapple', 7), ('happily', 7)])
    self.assertListEqual(sorted(redict[:'apple']),
                         [('applesauce', 10), ('grapple', 7)])

  def test_return_type(self):
    redict = regexdict(self.base_dict)
    # Generator over (key, value) pairs
    self.assertIsInstance(redict[:'.app'], types.GeneratorType)
    # List of (key, value) pairs
    self.assertIsInstance(redict[list:'.app'], list)
    # Dict of results
    self.assertIsInstance(redict[dict:'.app'], dict)
    # # Sequence of keys (a list in python 2, a generator in python 3)
    # redict[r.keys :'.app']
    # # Sequence of values (a list in python 2, a generator in python 3)
    # redict[r.values :'.app']

  def test_re_compiled(self):
    redict = regexdict(self.base_dict)
    app = re.compile('.app')
    self.assertListEqual(redict[list:app], redict[list:'.app'])

  def test_in_operator(self):
    redict = regexdict(self.base_dict)
    # Non-regex string keys
    self.assertIn('grapple', redict)
    # Pre-compiled re objects
    app = re.compile('.app')
    self.assertIn(app, redict)
    bad = re.compile('ba+d')
    self.assertNotIn(bad, redict)


if __name__ == '__main__':
  unittest.main()
