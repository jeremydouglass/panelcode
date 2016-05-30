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
    #  <panelcodeblock>    ...a text string / file, with one or more separated by linebreaks:
    #                       <panelcode> | <panelcode> <comment> | <comment> | <blankline>
    #
    #+ <panelcode>         :=  <page> | <pagegroup>
    #  
    #+ <pagegroup>         :=  <page> <pagejoin> <page> | <page> <pagejoin> <pagegroup>
    #+   <pagejoin>        :=  <horizontaljoin> | <verticaljoin>
    #+   <horizontaljoin>  :=  "++";
    #+   <verticaljoin>    :=  ",,";
    #  
    #+ <page>              :=  <row> | <row> <rowseparator> <row> | <emptypage> | <uncodedpage>
    #+   <rowseparator>    :=  "_";
    #+   <emptypage>       :=  <emptyrow>
    #+   <uncodedpage>     :=  <uncodedrow>
    #  
    #+ <grouprow>          :=  <groupopen> <grouprowcontents> <groupclose>
    #  	                    | <decorativenum> <groupopen> <grouprowcontents> <groupclose>
    #    <decorativenum>   :=  <numbers>
    #+   <groupopen>       :=  "("
    #+   <groupclose>      :=  ")"
    #  
    #+ <grouprowcontents>  :=  <groupunit> | <groupunit> <groupseparator> <groupunit>
    #+   <groupseparator>  :=  <newcol> | <newrow>
    #+     <newcol>        :=  "+"
    #+     <newrow>        :=  ","
    #+   <groupunit>       :=  <emptyrow> | <numrow> | <numrow> <spanmodifier> | <spanmodifier>
    #+     <spanmodifier>  :=  <rowspan> | <colspan> | <rowspan> <colspan> | <colspan> <rowspan>
    #        <rowspan>     :=  "r" <numbers>
    #        <colspan>     :=  "c" <numbers>
    #  
    #+ <row>               :=  <grouprow> | <numrow> | <emptyrow> | <uncodedrow>
    #+   <emptyrow>        :=  "0"
    #+   <uncodedrow>      :=  <groupopen> "_" <groupclose>
    #  
    #+ <numrow>            :=  <countingnums>
    #  
    #  <digits>            :=  <digit> | <digit> <digits>
    #  <digit>             :=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    #  <numbers>           :=  <countingnums> | <countingnums> <digits>
    #+ <countingnums>      :=  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

    countingnums    = pp.Regex(r"[1-9]") # or support 10+... pp.Regex(r"[1-9][0-9]*")
    rowseparator    = pp.Suppress(pp.Literal("_"))
    groupopen       = pp.Suppress(pp.Literal("("))
    groupclose      = pp.Suppress(pp.Literal(")"))
    newcol          = pp.Literal("+")
    newrow          = pp.Literal(",")
    pageseparator   = pp.Suppress(pp.Literal(";"))
    verticaljoin    = pp.Literal("++")
    horizontaljoin  = pp.Literal(",,")

    numrow          = countingnums # pp.Literal("3") # placeholder
    emptyrow        = pp.Literal("0").setResultsName('emptyrow') # or...?  pp.Literal("E")
    uncodedrow      = pp.Group( groupopen + pp.Literal("~").setResultsName('uncoded') + groupclose )
    spanmodifier    = pp.Regex(r"[rc][1-9][0-9]*").setResultsName('spanmodifier')

    groupunit       = pp.Group( emptyrow | numrow | numrow + spanmodifier | spanmodifier ).setResultsName('unit')
    groupseparator  = ( newcol | newrow )
    grouprowcontents = pp.Group( groupunit + pp.ZeroOrMore( groupseparator + groupunit ) )
    grouprow        = pp.Group( groupopen + grouprowcontents + groupclose )# pp.Literal("3()") # placeholder

    row             = grouprow | numrow | emptyrow | uncodedrow
    emptypage       = emptyrow
    uncodedpage     = uncodedrow
    page            = pp.Group( emptypage | uncodedpage | pp.Group(row + pp.ZeroOrMore( pp.Optional(rowseparator) + row )).setResultsName('rows') ).setResultsName('page')
    pagejoin        = ( horizontaljoin | verticaljoin ).setResultsName('pagejoin')
    pagegroup       = pp.Group( page + pp.ZeroOrMore( pagejoin + page ) + pp.Optional(pageseparator)).setResultsName('pagegroup')
    panelcode       = pp.Group( pp.OneOrMore( pagegroup | page ) ).setResultsName('panelcode')
    
    try:
        result = panelcode.parseString(pstr)
        # result = panelcode.parseString(pstr)
        # print pstr + " Matches: {0}".format(result)
        return result
    except pp.ParseException as x:
        # print "\n  ParseException: {0}".format(str(x)) + 'in: ' + str(pstr) + '\n'
        raise x
        # return [''] ######### <---- this temporarily supresses errors in the test suite
