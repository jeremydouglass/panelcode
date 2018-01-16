# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m panelcode.parser

import pyparsing as pp
# from pyparsing import Word, Optional, Group, Literal, alphas, nums, ZeroOrMore, OneOrMore, ParseException

# def parse_example (str):
#     integer = pp.Word( pp.nums ) # simple unsigned integer
#     variable = pp.Word( pp.alphas, max=1 ) # single letter variable, such as x, z, m, etc.
#     arithOp = pp.Word( "+-*/", max=1 ) # arithmetic operators
#     equation = variable + "=" + integer + arithOp + integer # will match "x=2+2", etc.
#     result = equation.parseString(str)
#     return result

def parse_panelcode (pstr):
    """..."""

    countingnums    = pp.Regex(r"[1-9]").setResultsName('simplerow', listAllMatches=True)
    numpage         = pp.Group( pp.OneOrMore( countingnums ) ).setResultsName('numpage')
    
    rowseparator    = pp.Suppress(pp.Literal("_"))
    groupopen       = pp.Suppress(pp.Literal("("))
    groupclose      = pp.Suppress(pp.Literal(")"))
    newcol          = pp.Literal("+")
    newrow          = pp.Literal(",")
    pageseparator   = pp.Suppress(pp.Literal(";"))
    verticaljoin    = pp.Literal("++")
    horizontaljoin  = pp.Literal(",,")

    blankpanel      = pp.Literal("0")
    numrow          = ( countingnums | blankpanel ).setResultsName('panel', listAllMatches=True) # pp.Literal("3") # placeholder
    emptyrow        = pp.Literal("0").setResultsName('emptyrow', listAllMatches=True) # or...?  pp.Literal("E")
    uncodedrow      = pp.Group( groupopen + pp.Literal("~").setResultsName('uncoded', listAllMatches=True) + groupclose )
    spanmodifier    = pp.Regex(r"[rc][1-9][0-9]*").setResultsName('spanmodifier', listAllMatches=True)

    groupunit       = pp.Group( emptyrow | numrow | numrow + spanmodifier | spanmodifier ).setResultsName('groupunit', listAllMatches=True)
    groupseparator  = ( newcol | newrow ).setResultsName('groupseparator')
    grouprowcontents = pp.Group( groupunit + pp.ZeroOrMore( groupseparator + groupunit ) )
    grouprow        = pp.Group( groupopen + grouprowcontents + groupclose )# pp.Literal("3()") # placeholder

    row             = ( grouprow | numrow ).setResultsName('rows', listAllMatches=True)
    page            = pp.Group( pp.Group(row + pp.ZeroOrMore( pp.Optional(rowseparator) + row )) ).setResultsName('page', listAllMatches=True)
    pagejoin        = ( horizontaljoin | verticaljoin ).setResultsName('pagejoin', listAllMatches=True)
    pagegroup       = pp.Group( page + pp.ZeroOrMore( pagejoin + page ) + pageseparator).setResultsName('pagegroup', listAllMatches=True)
    panelcode       = pp.Group( pp.OneOrMore( pagegroup ) ).setResultsName('panelcode', listAllMatches=True)
    
    try:
        result = panelcode.parseString(pstr)
        # print pstr + " Matches: {0}".format(result)
        return result
    except pp.ParseException as x:
        # print "\n  ParseException: {0}".format(str(x)) + 'in: ' + str(pstr) + '\n'
        raise x
        # return [''] ######### <---- this temporarily supresses errors in the test suite
