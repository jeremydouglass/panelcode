# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_basic

from .context import panelcode

import unittest


batchstring = """1
0
0_(2+0+2)_0
0_1_(0+1)
0_1_(1+0)
0_2_0
0_3_0
1_2_3_4_5_6
1_3_2_4
2_(1,0)
2_2
2_2++3_3
2_2_2_1_1_2_1
2_3
2_3_2
2_3_3(1+r2,1)
2_3_5
2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)
3C
3D
3(r2+0,1)
3(r2+1,1)
3_3_3_3_3
3_3_3++2_5(r2+2,2)
4(r3+1,1,1)
4(1+r3,1,1)
5(1+r2+1,2)
5(r2+1+r2,1)
5(r2+2,2)
5(2+r2,2)
1"""

batchstring2 = """3x5            # grid shorthand
	0_1_(0_1)      # zero panels
	2_3_2++        # page-compositing
	2_2++3+3       #"""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

#    def test_absolute_truth_and_meaning(self):
#        print 'absolute truth'
#        assert True

    def test_app_batch_svg(self):
    	panelcode.app_batch_svg(batchstring)
        assert True

if __name__ == '__main__':
    unittest.main()