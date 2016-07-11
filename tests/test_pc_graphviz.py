# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_basic

from .context import panelcode
from panelcode import *
import unittest

class GraphvizTestSuite(unittest.TestCase):
    """Util test cases."""

    def test_li_to_gv(li):
        tests = []
        tests.append(  ['1','2','3']      )  ## strings
        tests.append(  ['1 ',' 2',' 3 ']  )  ## spaced
        tests.append(  [1,2,3]            )  ## ints
        tests.append(  [1,'2',' 3 ']      )  ## mixed

        tests.append(  [3,3,3]            )
        tests.append(  [1,2,3,4,5,6]      )
        tests.append(  [6,4,6,3,1,3]      )

        tests.append(  [1,0,'~']            )  ## blank and uncoded

        for t in tests:
            pgv = pc_graphviz.li_to_gv(t)
            filename = list_to_string(t, join=',') + '.gv'
            pgv.format = 'png'
            pgv.render(filename, view=True)


if __name__ == '__main__':
    unittest.main()



        # tests.append(  [('1+1+1+1+1+0+1+0+0+0+1+0+1+0+1+0'),
        #                 ('1+0+1+0+0+0+1+1+1+1+1+1+1+1+1+1'),
        #                 ('1+1+1+1+1+0+1+0+1+0+1+0+1+0+1+0'),
        #                 ('1+0+1+0+1+0+1+0+1+0+1+0+0+0+1+0'),
        #                 ('1+0+1+1+1+1+1+1+1+1+1+1+1+1+1+1'),
        #                 ('0+0+0+0+1+0+1+0+1+0+1+0+0+0+1+0'),
        #                 ('1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1'),
        #                 ('0+0+1+0+1+0+0+1+0+0+1+1+0+1+0+0'),
        #                 ('1+1+1+1+1+1+1+1+1+0+1+0+0+1+0+1'),
        #                 ('0+1+0+0+1+0+0+1+0+0+1+1+1+1+1+1'),
        #                 ('1+1+1+1+1+0+1+1+0+0+1+0+0+1+0+1'),
        #                 ('0+1+0+0+1+0+0+1+0+1+1+1+1+1+1+1')]  )
