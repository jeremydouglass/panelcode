import pyparsing as pp



def parse_panelcode (pstr):
    """..."""

    # num # 0-9, built-in   
    # nums
    # alphanum
    # alphanums
    # alpha
    # alphas
    # restOfLine
    digit           = pp.Regex(r"[0-9]")
    countingnums    = pp.Regex(r"[1-9]") # or support 10+... pp.Regex(r"[1-9][0-9]*")
    rowseparator    = pp.Suppress(pp.Literal("_"))
    groupopen       = pp.Suppress(pp.Literal("("))
    groupclose      = pp.Suppress(pp.Literal(")"))
    newcol          = pp.Literal("+")
    newrow          = pp.Literal(",")
    layoutseparator = pp.Suppress(pp.Literal(";"))
    horizontaljoin  = pp.Literal("++")
    verticaljoin    = pp.Literal(",,")

    # one             = pp.Literal("1").setResultsName('one')
    # ones            = pp.Group(pp.delimitedList(one, delim="_")).setResultsName('ones')
    # two             = pp.Group(ones).setResultsName('two')
    # twos            = pp.Group(pp.OneOrMore(two)).setResultsName('twos')
    # three           = pp.Group(twos).setResultsName('three')
    # threes          = pp.Group(pp.OneOrMore(three)).setResultsName('threes')
    # four            = pp.Group(threes).setResultsName('four')
    # fours           = pp.Group(pp.OneOrMore(four)).setResultsName('fours')
    
    # ## WORKS
    # one             = digit.setResultsName('one', listAllMatches=True)
    # ones            = pp.Group(pp.OneOrMore(one)).setResultsName('ones', listAllMatches=True)
    # twos            = pp.Group(pp.OneOrMore(ones)).setResultsName('twos', listAllMatches=True)
    # threes          = pp.Group(pp.OneOrMore(twos)).setResultsName('threes', listAllMatches=True)
    # fours           = pp.Group(pp.delimitedList(threes, delim="_")).setResultsName('fours', listAllMatches=True)
    # pcode           = pp.Group(fours).setResultsName('pcode')
    # try:
    #     result = pcode.parseString(pstr) # parseAll=True
    #     # result = panelcode.parseString(pstr)
    #     # print pstr + " Matches: {0}".format(result)
    #     return result
    # except pp.ParseException as x:
    #     # print "\n  ParseException: {0}".format(str(x)) + 'in: ' + str(pstr) + '\n'
    #     raise x
    #     # return [''] ######### <---- this temporarily supresses errors in the test suite

    ## WORKS
    # one             = digit.setResultsName('panelc', listAllMatches=True)
    # ones            = pp.Group(pp.OneOrMore(one)).setResultsName('panelgroup', listAllMatches=True)
    # twos            = pp.Group(pp.delimitedList(ones, delim="_")).setResultsName('layout', listAllMatches=True)
    # threes          = pp.Group(pp.delimitedList(twos, delim="++")).setResultsName('spread', listAllMatches=True)
    # fours           = pp.Group(pp.delimitedList(threes, delim=";")).setResultsName('gallery', listAllMatches=True)
    # pcode           = pp.Group(pp.delimitedList(fours, delim=";;")).setResultsName('pcode')

    ## WORKS 3
    # panelc            = digit.setResultsName('panelc', listAllMatches=True)
    # panelgroup        = pp.Group(pp.OneOrMore(panelc)).setResultsName('panelgroup', listAllMatches=True)
    # layout            = pp.Group(pp.delimitedList(panelgroup, delim="_")).setResultsName('layout', listAllMatches=True)
    # spread            = pp.Group(pp.delimitedList(layout, delim="++")).setResultsName('spread', listAllMatches=True)
    # gallery           = pp.Group(pp.delimitedList(spread, delim=";")).setResultsName('gallery', listAllMatches=True)
    # pcode             = pp.Group(pp.delimitedList(gallery, delim=";;")).setResultsName('pcode')

    ## WORKS 4
    # panelopts         = pp.Literal("{}").setResultsName('panelopts', listAllMatches=True)
    # panelgroupopts    = pp.Literal("{}").setResultsName('panelgroupopts', listAllMatches=True)
    # layoutopts        = pp.Literal("{:}").setResultsName('layoutopts', listAllMatches=True)
    # spreadopts        = pp.Literal("{::}").setResultsName('spreadopts', listAllMatches=True)
    # galleryopts       = pp.Literal("{:::}").setResultsName('galleryopts', listAllMatches=True)
    # pcodeopts         = pp.Literal("{::::}").setResultsName('pcodeopts')
    # panelc            = digit.setResultsName('panelc', listAllMatches=True)
    # panelgroup        = pp.Group(pp.OneOrMore(panelc) + pp.Optional(panelopts)).setResultsName('panelgroup', listAllMatches=True)
    # layout            = pp.Group(pp.delimitedList(panelgroup, delim="_") + pp.Optional(panelgroupopts)).setResultsName('layout', listAllMatches=True)
    # spread            = pp.Group(pp.delimitedList(layout, delim="++") + pp.Optional(layoutopts)).setResultsName('spread', listAllMatches=True)
    # gallery           = pp.Group(pp.delimitedList(spread, delim=";") + pp.Optional(spreadopts)).setResultsName('gallery', listAllMatches=True)
    # root              = pp.Group(pp.delimitedList(gallery, delim=";;") + pp.Optional(galleryopts)).setResultsName('pcode', listAllMatches=True) + pp.Optional(pcodeopts).setResultsName('pcodeopts')

    # ## WORKS 5
    # attr_word          = pp.Word(pp.alphanums) # https://pythonhosted.org/pyparsing/pyparsing.OneOrMore-class.html
    # attr_label         = attr_word + pp.FollowedBy(':')
    # attr_expr          = pp.Group(attr_label + pp.Suppress(':') + pp.OneOrMore(attr_word, stopOn=attr_label).setParseAction(' '.join))
    # attr_list          = attr_expr # (pp.OneOrMore(pp.Word(pp.alphas))).setResultsName('arg', listAllMatches=True)
                                   
    # panelopts          = (pp.Suppress(pp.Literal("{")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('panelopts', listAllMatches=True)
    # # panelopts         = pp.nestedExpr('{', '}').setResultsName('panelopts', listAllMatches=True) # never nested, so skip a heirarchy level by doing it manually instead
    # panelgroupopts    = (pp.Suppress(pp.Literal("{")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('panelgroupopts', listAllMatches=True)
    # layoutopts        = (pp.Suppress(pp.Literal("{:")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('layoutopts', listAllMatches=True)
    # spreadopts        = (pp.Suppress(pp.Literal("{::")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('spreadopts', listAllMatches=True)
    # galleryopts       = (pp.Suppress(pp.Literal("{:::")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('galleryopts', listAllMatches=True)
    # pcodeopts         = (pp.Suppress(pp.Literal("{::::")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('pcodeopts', listAllMatches=True)
    # panelc            = digit.setResultsName('panelc', listAllMatches=True)
    # panelgroup        = pp.Group(pp.OneOrMore(panelc) + pp.Optional(panelgroupopts)).setResultsName('panelgroup', listAllMatches=True)
    # layout            = pp.Group(pp.delimitedList(panelgroup, delim="_") + pp.Optional(layoutopts)).setResultsName('layout', listAllMatches=True)
    # spread            = pp.Group(pp.delimitedList(layout, delim="++") + pp.Optional(spreadopts)).setResultsName('spread', listAllMatches=True)
    # gallery           = pp.Group(pp.delimitedList(spread, delim=";") + pp.Optional(galleryopts)).setResultsName('gallery', listAllMatches=True)
    # root              = pp.Group(pp.delimitedList(gallery, delim=";;") + pp.Optional(pcodeopts)).setResultsName('pcode', listAllMatches=True)

    ## WORKS 6
    attr_word          = pp.Word(pp.alphanums) # https://pythonhosted.org/pyparsing/pyparsing.OneOrMore-class.html
    attr_label         = attr_word + pp.FollowedBy(':')
    attr_expr          = pp.Group(attr_label + pp.Suppress(':') + pp.OneOrMore(attr_word, stopOn=attr_label).setParseAction(' '.join))
    attr_list          = attr_expr # (pp.OneOrMore(pp.Word(pp.alphas))).setResultsName('arg', listAllMatches=True)
                                   
    panelopts          = (pp.Suppress(pp.Literal("{")) + attr_list + pp.Suppress(pp.Literal("}"))).setResultsName('panelopts', listAllMatches=True)
    # panelopts         = pp.nestedExpr('{', '}').setResultsName('panelopts', listAllMatches=True) # never nested, so skip a heirarchy level by doing it manually instead
    panelgroupopts    = (pp.Suppress(pp.Literal("{")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('panelgroupopts', listAllMatches=True)
    layoutopts        = (pp.Suppress(pp.Literal("{:")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('layoutopts', listAllMatches=True)
    spreadopts        = (pp.Suppress(pp.Literal("{::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('spreadopts', listAllMatches=True)
    galleryopts       = (pp.Suppress(pp.Literal("{:::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('galleryopts', listAllMatches=True)
    pcodeopts         = (pp.Suppress(pp.Literal("{::::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('pcodeopts', listAllMatches=True)
    panelc            = digit.setResultsName('panelc', listAllMatches=True)
    panelrg           = pp.Literal("()").setResultsName('panelrg', listAllMatches=True)
    panelgroup        = pp.Group(pp.Or(panelc, panelrg) + pp.Optional(panelgroupopts)).setResultsName('panelgroup', listAllMatches=True)
    layout            = pp.Group(pp.delimitedList(panelgroup, delim="_") + pp.Optional(layoutopts)).setResultsName('layout', listAllMatches=True)
    spread            = pp.Group(pp.delimitedList(layout, delim="++") + pp.Optional(spreadopts)).setResultsName('spread', listAllMatches=True)
    gallery           = pp.Group(pp.delimitedList(spread, delim=";") + pp.Optional(galleryopts)).setResultsName('gallery', listAllMatches=True)
    root              = pp.Group(pp.delimitedList(gallery, delim=";;") + pp.Optional(pcodeopts)).setResultsName('pcode', listAllMatches=True)



    # numrow          = countingnums # pp.Literal("3") # placeholder
    # emptyrow        = pp.Literal("0").setResultsName('emptyrow') # or...?  pp.Literal("E")
    # uncodedrow      = pp.Group( groupopen + pp.Literal("~").setResultsName('uncoded') + groupclose )
    # spanmodifier    = pp.Regex(r"[rc][1-9][0-9]*").setResultsName('spanmodifier')

    # groupunit       = pp.Group( emptyrow | numrow | numrow + spanmodifier | spanmodifier )
    # groupseparator  = ( newcol | newrow )
    # grouprowcontents = pp.Group( groupunit + pp.ZeroOrMore( groupseparator + groupunit ) )
    # grouprow        = pp.Group( groupopen + grouprowcontents + groupclose )# pp.Literal("3()") # placeholder

    # row             = ( grouprow | numrow | emptyrow | uncodedrow ).setResultsName('rowgroup')
    # emptylayout     = emptyrow
    # uncodedlayout   = uncodedrow
    # layout          = pp.Group( emptylayout | uncodedlayout | pp.Group(row + pp.ZeroOrMore( pp.Optional(rowseparator) + row ))).setResultsName('layout')
 
    # layoutjoin      = ( horizontaljoin | verticaljoin ).setResultsName('layoutjoin')
    # spread          = pp.Group( layout + pp.ZeroOrMore( layoutjoin + layout ) + pp.Optional(layoutseparator)).setResultsName('spread')

    # panelcode       = countingnums
    
    try:
        result = root.parseString(pstr) # parseAll=True
        # result = panelcode.parseString(pstr)
        # print pstr + " Matches: {0}".format(result)
        return result
    except pp.ParseException as x:
        # print "\n  ParseException: {0}".format(str(x)) + 'in: ' + str(pstr) + '\n'
        raise x
        # return [''] ######### <---- this temporarily supresses errors in the test suite
