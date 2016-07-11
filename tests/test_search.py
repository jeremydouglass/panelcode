# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_search

from .context import panelcode
from panelcode import *
import unittest

class SearchTestSuite(unittest.TestCase):
    """Search test cases."""
   
    def test_list_to_string(self):
        expected = '1\n2\n3'
        tests = []
        tests.append(  ['1','2','3']      )  ## strings
        tests.append(  ['1 ',' 2',' 3 ']  )  ## spaced
        tests.append(  [1,2,3]            )  ## ints
        tests.append(  [1,'2',' 3 ']      )  ## mixed
        for i in tests:
            self.assertEqual( utils.list_to_string(i), expected )
        ## test 'join' kwarg
        self.assertEqual( utils.list_to_string(['1','2','3'], join=';'), '1;2;3' )
        self.assertEqual( utils.list_to_string(['1 ',' 2',' 3 '], join=' '), '1 2 3' )
        self.assertEqual( utils.list_to_string([1,2,3], join='\n'), '1\n2\n3' )
        self.assertEqual( utils.list_to_string([1,'2',' 3 '], join=','), '1,2,3' )

    def test_list_counter(self):        
        """ """
        ## https://docs.python.org/2.7/library/collections.html#collections.Counter
        test_list_ = ['1','2','3','4','5','6']
        c = search.list_counter(test_list_)
        ## inspect counters
        # self.counter_stats(c)

    def test_list_of_lists_counter(self):        
        """ """
        test_list_of_lists = [['1','2','3'],['4','5','6']]
        c = search.list_of_lists_counter(test_list_of_lists)
        ## inspect counters
        # self.counter_stats(c)

    def test_list_contains(self):
        """ """
        test_list_ = ['1','2','3','4','5','6']
        self.assertTrue (search.list_contains(test_list_, '1'))
        self.assertFalse(search.list_contains(test_list_, '7'))

    def test_list_of_lists_contains(self):
        """ """
        test_list_of_lists = [['1','2','3'],['4','5','6']]
        self.assertTrue (search.list_of_lists_contains(test_list_of_lists, '1'))
        self.assertFalse(search.list_of_lists_contains(test_list_of_lists, '7'))

    def counter_stats(self, c):
        """test function for inspecting counters"""
        print c
        print '  most common:'
        print c.most_common(3)
        print '  least common:'
        print c.most_common()[:-4:-1]         # n least common elements (:-n-1:-1)
        print '  total of counts:'
        print sum(c.values())                 # total of all counts
        print '  unique elements:'
        print list(c)                         # list unique elements
        print '  set:'
        print set(c)                          # convert to a set
        print '  dict:'
        print dict(c)                         # convert to a regular dictionary
        print '  list of pairs:'
        print c.items()                       # convert to a list of (elem, cnt) pairs
        c += Counter(); print c               # remove zero and negative counts
        c.clear(); print c                    # reset all counts
 


if __name__ == '__main__':
    unittest.main()