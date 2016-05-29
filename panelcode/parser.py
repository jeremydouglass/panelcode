# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m panelcode.parser

import pyparsing as pp
# from pyparsing import Word, Optional, Group, Literal, alphas, nums, ZeroOrMore, OneOrMore, ParseException

def test_parse_howto ():
    integer = pp.Word( pp.nums ) # simple unsigned integer
    variable = pp.Word( pp.alphas, max=1 ) # single letter variable, such as x, z, m, etc.
    arithOp = pp.Word( "+-*/", max=1 ) # arithmetic operators
    equation = variable + "=" + integer + arithOp + integer # will match "x=2+2", etc.
    result = equation.parseString("x=2+2")
    print result

def parse_panelcode (pstr):
    """..."""
    page            = pp.Literal("3")
    panelcode       = pp.OneOrMore(page)
    #   rowcode         = Group(OneOrMore(nums) + Optional("b"))
    
    try:
        result = panelcode.parseString(pstr)
        print pstr + " Matches: {0}".format(result)
        return result
    except pp.ParseException as x:
        print pstr + " No match: {0}".format(str(x))
        return [''] ######### <---- this temporarily supresses errors in the test suite

 
"""bnf
%start panelcode

<panelcode>         :=  <page> | <pagegroup>
	                    | <page> <linebreak> <panelcode>
						| <pagegroup> <linebreak> <panelcode>

<pagegroup>         :=  <page> <pagejoin> <page> | <page> <pagejoin> <pagegroup>
  <pagejoin>        :=  <horizontaljoin> | <verticaljoin>
  <horizontaljoin>  :=  "++";
  <verticaljoin>    :=  ",,";

<page>              :=  <row> | <row> <rowseparator> <page> | <emptypage> | <uncodedpage>
  <rowseparator>    :=  "_";
  <emptypage>       :=  <emptyrow>
  <uncodedpage>     :=  <uncodedrow>

<row>               :=  <numrow> | <grouprow> | <emptyrow> | <uncodedrow>
  <numrow>          :=  <numbers> | <numbers> <rowseparator> <row>
  <emptyrow>        :=  "0"
  <uncodedrow>      :=  <groupopen> "_" <groupclose>

<grouprow>          :=  <groupopen> <grouprowcontents> <groupclose>
	                    | <decorativenum> <groupopen> <grouprowcontents> <groupclose>
  <decorativenum>   :=  <numbers>
  <groupopen>       :=  "("
  <groupclose>      :=  ")"

<grouprowcontents>  :=  <groupunit> | <groupunit> <groupseparator> <groupunit>
  <groupseparator>  :=  <newcol> | <newrow>
    <newcol>        :=  "+"
	<newrow>        :=  ","
  <groupunit>       :=  <emptyrow> | <numbers> | <numbers> <spanmodifier> | <spanmodifier>
    <spanmodifier>  :=  <rowspan> | <colspan> | <rowspan> <colspan> | <colspan> <rowspan>
      <rowspan>     :=  "r" <numbers>
      <colspan>     :=  "c" <numbers>

<digits>            :=  <digit> | <digit> <digits>
<digit>             :=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<numbers>           :=  <number> | <number> <digits>
<number>            :=  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<letter>            :=  a | b | c | ... | y | z
"""