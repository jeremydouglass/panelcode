import pyparsing as pp

digit           = pp.Regex(r"[0-9]")
digits          = pp.Regex(r"[0-9]*")
countingnums    = pp.Regex(r"[1-9]") # or support 10+... pp.Regex(r"[1-9][0-9]*")

group_add       = pp.Suppress(pp.Literal("_"))
group_start     = pp.Suppress(pp.Literal("("))
group_stop      = pp.Suppress(pp.Literal(")"))

newcol          = pp.Literal("+") # pp.Group(pp.Literal("+") + pp.NotAny("+")).setResultsName('newcol', listAllMatches=True)
newrow          = pp.Literal(",")

attr_word          = pp.Word(pp.alphanums) # https://pythonhosted.org/pyparsing/pyparsing.OneOrMore-class.html
attr_label         = attr_word + pp.Suppress(pp.FollowedBy('='))
attr_expr          = pp.Group(attr_label + pp.OneOrMore(attr_word, stopOn=attr_label).setParseAction(' '.join))
attr_list          = pp.ZeroOrMore(attr_word)

# options {}
panelopts         = (pp.Suppress(pp.Literal("{")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('panelopts', listAllMatches=True)
panelgroupopts    = (pp.Suppress(pp.Literal("{")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('panelgroupopts', listAllMatches=True)
layoutopts        = (pp.Suppress(pp.Literal("{:")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('layoutopts', listAllMatches=True)
spreadopts        = (pp.Suppress(pp.Literal("{::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('spreadopts', listAllMatches=True)
galleryopts       = (pp.Suppress(pp.Literal("{:::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('galleryopts', listAllMatches=True)
pcodeopts         = (pp.Suppress(pp.Literal("{::::")) + pp.Optional(attr_list) + pp.Suppress(pp.Literal("}"))).setResultsName('pcodeopts', listAllMatches=True)

# blankpanel      = pp.Literal("0")
# numrow          = ( digits | blankpanel ) # .setResultsName('panel', listAllMatches=True) # pp.Literal("3") # placeholder
# emptyrow        = pp.Literal("0").setResultsName('emptyrow', listAllMatches=True) # or...?  pp.Literal("E")
# uncodedrow      = pp.Group( group_start + pp.Literal("~").setResultsName('uncoded', listAllMatches=True) + group_stop )

numrow          = digits # .setResultsName('panel', listAllMatches=True) # pp.Literal("3") # placeholder
spanmodifier    = pp.Suppress(pp.Optional(pp.Literal("."))) + pp.Regex(r"[a-z]([1-9][0-9]*)?") # .setResultsName('spanmodifier', listAllMatches=True)

groupunit       = (numrow + pp.OneOrMore(spanmodifier) ^ numrow ^ spanmodifier) # .setResultsName('unit', listAllMatches=True)
groupseparator  = ( newcol ^ newrow ) # .setResultsName('groupseparator')
# groupterms    = pp.Suppress(pp.Optional(group_start)) + pp.Group(groupunit + pp.ZeroOrMore( groupseparator + groupunit )).setResultsName('terms', listAllMatches=True) + pp.Suppress(pp.Optional(group_stop))
groupterms      = pp.Suppress(pp.Optional(group_start)) + groupunit + pp.ZeroOrMore( groupseparator + groupunit ) + pp.Suppress(pp.Optional(group_stop))


# pgrouprow         = pp.Literal(" ");
# pgroupnum         = pp.Group(pp.Word(pp.nums) + pp.Suppress(pp.Optional(pp.Literal(".")))).setResultsName('panel', listAllMatches=True)
# panelgroup        = pp.Group(pp.Or(pgroupnum, pgrouprow) + pp.Optional(panelgroupopts)).setResultsName('panelgroup', listAllMatches=True)

panelgroup        = pp.Group((groupterms ^ groupunit) + pp.Optional(panelgroupopts)).setResultsName('panelgroup', listAllMatches=True)


layout            = pp.Group(pp.delimitedList(panelgroup, delim="_") + pp.Optional(layoutopts)).setResultsName('layout', listAllMatches=True)
spread            = pp.Group(pp.delimitedList(layout, delim="|") + pp.Optional(spreadopts)).setResultsName('spread', listAllMatches=True) # ++
gallery           = pp.Group(pp.delimitedList(spread, delim=";") + pp.Optional(galleryopts)).setResultsName('gallery', listAllMatches=True)
root              = pp.Group(pp.delimitedList(gallery, delim="@") + pp.Optional(pcodeopts)).setResultsName('pcode', listAllMatches=True) # ;;
