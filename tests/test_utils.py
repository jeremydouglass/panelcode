# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_utils

from .context import panelcode
from panelcode import *
import unittest

class UtilTestSuite(unittest.TestCase):
    """Util test cases."""

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


    def test_string_to_list(self):
        expected = ['1','2','3']
        tests = []
        tests.append(  '1\n2\n3'            )
        tests.append(  '\n1\n\n2\n\n\n3\n'  )
        for i in tests:
            self.assertEqual( utils.string_to_list(i), expected )

        ## things that shouldn't work:
        # tests.append(  1                    )
        # tests.append(  ['1\n2\n3']          )
        # tests.append(  [1,2,3]              )


    def test_txtfile_to_list(self):
        files =  []
        values = []
        files.append(  'tests/testdata/utils--txtfile_to_list--test1.txt' )
        values.append( ['1', '2', '3'] )
        files.append(  'tests/testdata/utils--txtfile_to_list--test2.txt' )
        values.append( ['1,2,3', '2', '3,3'] )

        tests = zip(files,values)

        for i in tests:
            self.assertEqual( utils.txtfile_to_list(i[0]),i[1])
            ## tests for errors http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
            self.assertRaises(ValueError, utils.txtfile_to_list, '') ## func and args passed separately to assertRaises


    def test_list_to_txtfile(self):
        ## http://stackoverflow.com/questions/3942820/how-to-do-unit-testing-of-functions-writing-files-using-python-unittest
        ## http://stackoverflow.com/questions/2047459/unit-testing-file-write-in-python
        values = []
        files =  []
        values.append( ['1', '2', '3'] )
        files.append( 'tests/testdata/utils--list_to_txtfile--test1.txt' )

        tests = zip(values,files)

        for i in tests:
            list_to_txtfile(i[0], i[1])
            self.assertRaises(ValueError, list_to_txtfile, i[0], '') 
            self.assertRaises(ValueError, list_to_txtfile, '', i[1])


    def test_txttxtfile_to_string(self):
        expected =  '1\n2\n3'
        sourcename = 'tests/testdata/utils--txtfile_to_string--test1.txt'
        self.assertEqual( utils.txtfile_to_string(sourcename), expected )


    def test_jsonfile_to_list(self):
        expected =  ['1', '2', '3']
        sourcename = 'tests/testdata/utils--jsonfile_to_list--test1.json'
        self.assertEqual( utils.jsonfile_to_list(sourcename), expected )


    def test_list_to_jsonfile(self):
       mylist = ['1', '2', '3']
       filename = 'tests/testdata/utils--list_to_jsonfile--test1.json'
       list_to_jsonfile(mylist, filename)


    def test_list_to_picklefile(self):
       mylist = ['1', '2', '3']
       filename = 'tests/testdata/utils--list_to_picklefile--test1.pickle'
       list_to_picklefile(mylist, filename)


    def test_picklefile_to_list(self):
        expected =  ['1', '2', '3']
        sourcename = 'tests/testdata/utils--picklefile_to_list--test1.pickle'
        self.assertEqual( utils.picklefile_to_list(sourcename), expected )
       

if __name__ == '__main__':
    unittest.main()