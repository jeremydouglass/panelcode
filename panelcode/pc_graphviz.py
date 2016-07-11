# -*- coding: utf-8 -*-

from graphviz import Digraph
from .utils import *

## NOTES
## -  .gv suffix is preferred over .dot http://marc.info/?l=graphviz-devel&m=129418103126092
## -  graphviz record labels cannot accept style formatting (e.g. for blank, uncoded) -- instead use graphviz html labels
## -  graphviz node (layout) size is set with fixedsize + height, width
## -  li_to_gv doesn't yet support compositing of two pages or more layouts into a single layout.
## -  svg output...?


def li_to_gv(li):
    """Convert list into graphviz record label for rendering."""
    ## name 
    gvcomment = list_to_string(li, join=',')
    gv = Digraph(comment=gvcomment, graph_attr={'rankdir': 'LR'}, node_attr={'shape': 'record', 'fixedsize': 'true', 'height': '1.025', 'width': '.675'})
    gv.rankdir = 'LR'
    layoutstring = ''

    ## translate list into gv record label
    for i in li:
        rowstring=''
        if i=='~':
            rowstring = '~'
        elif int(i)>0:
            rowstring = '|'*int(i)        ## multiply panels -- to label with 1, use '1|'
            rowstring = rowstring[:-1]    ## strip trailing |
        elif int(i)==0:
            rowstring = '0'
        layoutstring += '{' + rowstring + '} |'  ## mark as gv record label row
    layoutstring = layoutstring[:-1]            ## strip trailing |

    # print "layoutstring: " + layoutstring

    ## create node with layout label
    # gv.node('A', '{1} | {1|1} | {1|1|1}')
    gv.node('A', layoutstring)

    return gv

    ## to render, e.g. by default bot a gv file and a PDF, with launched viewer:
    # gv.render('record-label-test.gv', view=True)


def pc_to_gv(li):
    """Convert list into graphviz record label for rendering."""
    