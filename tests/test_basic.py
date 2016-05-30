# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_basic

from .context import panelcode

import unittest

panelcode_test_string = """
1
2_2
2_3
2_3_2
2_3_5

1_3_2_4
1_2_3_4_5_6
3_3_3_3_3
2_2_2_1_1_2_1

3
3_3
3_3_3

33
333

0
0_0_0
0_3_0

00
03
30
303

3()
3()3()
3()3()3()

33()
3()3

3++3
3++3++3
3,,3
3,,3,,3

3++3;3,,3
3_3;3_3

2_(1,0)
2_2++3_3
2_3_3(1+r2,1)
2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)
3(r2+0,1)
3(r2+1,1)
3_3_3++2_5(r2+2,2)
4(r3+1,1,1)
4(1+r3,1,1)
5(1+r2+1,2)
5(r2+1+r2,1)
5(r2+2,2)
5(2+r2,2)

0_(2+0+2)_0
0_1_(0+1)
0_1_(1+0)

3C
3D

3\n3
3\n\n\n3

3;3
3;3;

3_
_3

3 3

3++3(),,3
3++(),,3

()
()_()
()()

(_)
(_)_(_)
(_)(_)

3_(_)_3
(_)_3_(_)

(_)++(_)
(_),,(_)
(_);(_)
"""

bad_strings = """
3(
3)
3;
;3

3(\n)3()

(())
((_))
"""

panelcode_test_string_3 = """3x5            # grid shorthand
	0_1_(0_1)      # zero panels
	2_3_2++        # page-compositing
	2_2++3+3       #"""

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

#    def test_absolute_truth_and_meaning(self):
#        print 'absolute truth'
#        assert True

    def test_app_batch_svg(self):
        test_string = panelcode.pstr_clean(panelcode_test_string) # strip all kinds of bad behavior

        ## this function needs to be replaced with pyparser output,
        ## but temporarily cleaning the input in-place during testing
        test_string = test_string.replace("(_)", "0") # replace uncoded page markers as empty pages
        test_string = test_string.replace(";", "\n") # split pages into lines

    	panelcode.app_batch_svg(test_string)
        assert True

###  currently already cascade tested by test_app_batch_svg
#    def test_app_svg_preview_page(self):
#        panelcode.app_svg_preview_page(svg_file_list,'script/output/','index.html')
#        assert True


class CleanTestSuite(unittest.TestCase):
    """Clean test cases."""

    def test_pstr_clean(self):
        self.assertTrue('#' not in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))

        # note that clean DOES NOT do page decompositing
        self.assertTrue('++' in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))
        self.assertTrue(',,' in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))

    def test_pstr_strip_comments(self):
        self.assertTrue('#' not in panelcode.pstr_strip_comments('1++2'))
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 #comment') ,'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 # comment'),'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 # comment #comment'),'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('#comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('# comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('#### comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('############'),'')

    def test_pstr_decomposite_pages(self):
        self.assertTrue('++' not in panelcode.pstr_decomposite_pages('1_2_3++4_5_6'))
        self.assertTrue(',,' not in panelcode.pstr_decomposite_pages('1_2_3,,4_5_6'))        
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1++2++3_4++5').split('\n'))==4)
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1,,2,,3_4,,5').split('\n'))==4)
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1++2,,3_4++5').split('\n'))==4)


class ParseTestSuite(unittest.TestCase):
    """Parser test cases."""

    def test_parse_example (self):
        self.assertEqual(panelcode.parse_example("x=2+2")[0], 'x')
        self.assertEqual(panelcode.parse_example("x=2+2")[1], '=')
        self.assertEqual(panelcode.parse_example("x=2+2")[2], '2')
        self.assertEqual(panelcode.parse_example("x=2+2")[3], '+')
        self.assertEqual(panelcode.parse_example("x=2+2")[4], '2')
        
    def test_parse_panelcode (self):
        print "\n\n-----TEST parse_panelcode-----\n"
        test_string = panelcode_test_string.split()
        print test_string
        for s in test_string:
            print "        In: " + str(s) 
            try:  
              result = panelcode.parse_panelcode(s)
              self.assertTrue(len(result)>0) # returns parsed objects, not nothing
              print "...matches: {0}".format(result)
              print result.asDict()
              try:
                print result['panelcode']
                print result['panelcode']['pagegroup']
                print result['panelcode']['pagegroup']['page']
                print result['panelcode']['pagegroup']['page']['row']
              except: ## some pages have no rows -- empty an uncoded. could force them to have rows. might help for css and html / svg rendering.
                pass              
            except panelcode.pp.ParseException as x:
                print "...ParseException" + '\n'
                print "...ParseException: {0}".format(str(x)) + '\n'

if __name__ == '__main__':
    unittest.main()