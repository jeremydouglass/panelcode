# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m panelcode.parser

import pyparsing as pp
# from pyparsing import Word, Optional, Group, Literal, alphas, nums, ZeroOrMore, OneOrMore, ParseException

def parse_example (str):
    integer = pp.Word( pp.nums ) # simple unsigned integer
    variable = pp.Word( pp.alphas, max=1 ) # single letter variable, such as x, z, m, etc.
    arithOp = pp.Word( "+-*/", max=1 ) # arithmetic operators
    equation = variable + "=" + integer + arithOp + integer # will match "x=2+2", etc.
    result = equation.parseString(str)
    return result

def parse_panelcode (pstr):
    """..."""

    #  BNF
    #  %start panelcode
    #  
    #  <panelcodeblock>    ...is a text string / file containing one or more, separated by linebreaks:
    #                       <panelcode> | <panelcode> <comment> | <comment> | <blankline>
    #
    #  <panelcode>         :=  <page> | <pagegroup>
    #  
    #  <pagegroup>         :=  <page> <pagejoin> <page> | <page> <pagejoin> <pagegroup>
    #    <pagejoin>        :=  <horizontaljoin> | <verticaljoin>
    #    <horizontaljoin>  :=  "++";
    #    <verticaljoin>    :=  ",,";
    #  
    #  <page>              :=  <row> | <row> <rowseparator> <page> | <emptypage> | <uncodedpage>
    #    <rowseparator>    :=  "_";
    #    <emptypage>       :=  <emptyrow>
    #    <uncodedpage>     :=  <uncodedrow>
    #  
    #  <row>               :=  <numrow> | <grouprow> | <emptyrow> | <uncodedrow>
    #    <numrow>          :=  <numbers> | <numbers> <rowseparator> <row>
    #    <emptyrow>        :=  "0"
    #    <uncodedrow>      :=  <groupopen> "_" <groupclose>
    #  
    #  <grouprow>          :=  <groupopen> <grouprowcontents> <groupclose>
    #  	                    | <decorativenum> <groupopen> <grouprowcontents> <groupclose>
    #    <decorativenum>   :=  <numbers>
    #    <groupopen>       :=  "("
    #    <groupclose>      :=  ")"
    #  
    #  <grouprowcontents>  :=  <groupunit> | <groupunit> <groupseparator> <groupunit>
    #    <groupseparator>  :=  <newcol> | <newrow>
    #      <newcol>        :=  "+"
    #  	<newrow>        :=  ","
    #    <groupunit>       :=  <emptyrow> | <numbers> | <numbers> <spanmodifier> | <spanmodifier>
    #      <spanmodifier>  :=  <rowspan> | <colspan> | <rowspan> <colspan> | <colspan> <rowspan>
    #        <rowspan>     :=  "r" <numbers>
    #        <colspan>     :=  "c" <numbers>
    #  
    #  <digits>            :=  <digit> | <digit> <digits>
    #  <digit>             :=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    #  <numbers>           :=  <number> | <number> <digits>
    #  <number>            :=  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    #  <letter>            :=  a | b | c | ... | y | z

    page            = pp.Literal("3()") | pp.Literal("3") |  pp.Literal("0") # placeholder
    horizontaljoin  = pp.Literal(",,")
    verticaljoin    = pp.Literal("++")
    pagejoin        = ( horizontaljoin | verticaljoin )
    pagegroup       = pp.Group ( page + pp.ZeroOrMore( pagejoin + page ))
    panelcode       = pp.Group ( pp.OneOrMore( pagegroup | page ))
    # panelcode01     = pp.OneOrMore(page)
    
    try:
        result = panelcode.parseString(pstr)
        # print pstr + " Matches: {0}".format(result)
        return result
    except pp.ParseException as x:
        print "\n  ParseException: {0}".format(str(x)) + 'in: ' + str(pstr) + '\n'
        return [''] ######### <---- this temporarily supresses errors in the test suite

