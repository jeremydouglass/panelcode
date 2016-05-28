# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_advanced

from .context import panelcode

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

#    def test_thoughts(self):
#        sample.hmm()


if __name__ == '__main__':
    unittest.main()