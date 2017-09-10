# -*- coding: utf-8 -*-

from os import linesep

def load_file (pc_filename):
    """..."""
    filecontents = []
    # return '...'

def plist_to_array (plist_string):
    """..."""
    # return '...'

def pstr_parse (filename):
    """..."""
    # return '...'


### CLEANERS

def pstr_clean (pstr):
    """run all cleaning functions on a panelcode string"""
    pstr = pstr_strip_comments(pstr)
    pstr = pstr_remove_empty_lines(pstr)
    pstr = pstr_remove_empty_rowgroups(pstr)
    pstr = pstr_collapse_row_separators(pstr)
    pstr = pstr_fill_row_gaps(pstr)
    pstr = shorthand_groups(pstr)
    
    return pstr

def pstr_strip_comments (pstr):
    """strip comments from a panelcode string"""
    pstr = pstr.split('#', 1)[0] # remove comments
    pstr = pstr.strip()          # remove whitespace from both ends
    return pstr

def pstr_remove_empty_lines (pstr):
    """remove empty lines from string""" 
    pstr = linesep.join([s for s in pstr.splitlines() if s.strip()])
    return pstr

def pstr_remove_empty_rowgroups (pstr):
    """remove empty rowgroups: () from string""" 
    pstr = pstr.replace("()", "") # collapse empty rowgroups
    return pstr
    
def pstr_collapse_row_separators (pstr):
    """collapse row separators: _ to one character""" 
    pstr = pstr.replace("__", "_") # collapse empty rowgroups
    return pstr
    
def pstr_fill_row_gaps (pstr):
    """fill row gaps, especially at beginning and end of line"""
    pstr = pstr.replace(" _", "0_") # collapse empty rowgroups
    pstr = pstr.replace("_ ", "_0") # collapse empty rowgroups
    pstr = pstr.replace("\n_", "\n0_") # fix row separator at line begin
    pstr = pstr.replace("_\n", "_0\n") # fix row separator at line end
    return pstr
    
def pstr_decomposite_pages (pstr):
    """split up pages"""
    pstr = pstr.replace("++", "\n")
    pstr = pstr.replace(",,", "\n")
    return pstr


def pstr_minify (pstr):
    pstr = pstr_clean(pstr)
    pstr = pstr.replace("\n", "; ")
    return pstr


### SHORTHANDS

def shorthand_groups (pstr):
    """run all cleaning functions on a panelcode string"""
    pstr = pstr.replace("3C", "3(r2+1,1)")
    pstr = pstr.replace("3D", "3(1+r2,1)")
    pstr = pstr.replace("4E", "4(r3+1,1,1)")
    pstr = pstr.replace("4C", "4(r3+1,1,1)") # same thing
    pstr = pstr.replace("4D", "4(1+r3,1,1)") # ...?
    pstr = pstr.replace("5H", "5(r2+1+r2,1)") # ...?
    return pstr


### ANALYZERS

def pstr_rowcount (pstr):
    """count the rows in a panelcode string"""
    rowcount = 0
    rowarray = pstr.split('_')
    row_marker = '_'
    tgroup_start = '('
    tgroup_end = ')'
    # rowarray = re.split("\()|_", pghtmlstring)' # http://stackoverflow.com/questions/1059559/python-split-strings-with-multiple-delimiters
    tables = [x.strip() for x in pstr.split(row_marker)] # http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
    rowheight = 'rowheight' # slug for replacing last, since we count rows as we go.
    for table in tables:
        if "(" not in table: # http://stackoverflow.com/questions/5473014/test-a-string-for-a-substring
            rowcount += 1 # increment
        elif tgroup_start in table: # http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
            tbgroup = ((table.split(tgroup_start))[1].split(tgroup_end)[0]) #http://stackoverflow.com/questions/3368969/find-string-between-two-substrings
            tbgroup_rows = [x.strip() for x in tbgroup.split(',')]
            rowmax = 1 # starting value
            for row in tbgroup_rows:
                rowgroup_cells = [x.strip() for x in row.split('+')]
                for cellgroup in rowgroup_cells:
                    cellgroup = cellgroup.replace("r", ".r")
                    cellgroup = cellgroup.replace("c", ".c")
                    if cellgroup.startswith('.'): # http://stackoverflow.com/questions/19954593/python-checking-a-strings-first-and-last-character
                        cellgroup = '1' + cellgroup
                    cellgroup_attribs = [x.strip() for x in cellgroup.split('.')]
                    for cellcount in range(0,int(cellgroup_attribs[0])):
                        try: # http://stackoverflow.com/questions/8570606/check-element-exists-in-array
                            for attrib in cellgroup_attribs[1:]: # skip the count, just check attrib(s)
                                if attrib.startswith('r'):
                                    rowmax = max(rowmax,int(attrib[1:])) # update with tallest panel
                                elif attrib.startswith('c'):
                                    rowmax = rowmax
                                else:
                                    print 'ERROR: Bad attribute (no r/c prefix): ' + attrib
                        except IndexError:
                            pass
            rowcount = rowcount + rowmax
    return rowcount


### RENDERERS

def pstr_to_html (pstr):
    """render a panelcode string as HTML"""
    pghtmlstring = ''
    tgroup_start = '('
    tgroup_end = ')'
    # print '\n----------------------------------------'
    # print '\npstr: ' + pstr
    tables = [x.strip() for x in pstr.split('_')] # http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
    rowheight_slug = """{rowheight}""" # slug for replacing last, since we count rows as we go.
    for table in tables:
        print '     table: ' + str(table)
        tstring = ''
        tstring = '<table class=\'row\'>\n'
        colcount = 0 ; print '          colcount = 0'
        colrowmax = 0; print '          colrowmax = 0'
        colcount_slug = """{colcount}"""
        tstring += '  <tr class="colspacer">' + colcount_slug + '</tr>\n' # placeholder until columns are counted
        if "(" not in table: # http://stackoverflow.com/questions/5473014/test-a-string-for-a-substring
            tstring += '  <tr height=\''+str(rowheight_slug)+'\'>\n'
            # tstring += '  <tr>\n'
            tstring += '    '
            try:
                for cellcount in range(0,int(table)):
                    tstring += '<td></td>'
                    colcount = colcount+1 # ; print '          colcount +1'
            except ValueError:
                tstring += '<td class="empty"></td>'
                colcount = colcount+1 # ; print '          colcount +1'
            tstring += '\n'
            tstring += '  </tr>\n'
        elif "(" in table: # http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
            tbgroup = ((table.split(tgroup_start))[1].split(tgroup_end)[0]) #http://stackoverflow.com/questions/3368969/find-string-between-two-substrings
            print '       tbgroup: ' + tbgroup
            tbgroup_rows = [x.strip() for x in tbgroup.split(',')]
            print tbgroup_rows
            colrowmax = 0
            for row in tbgroup_rows:
                print '         row: ' + row
                tstring += '  <tr height=\''+str(rowheight_slug)+'\'>\n'
                # tstring += '  <tr>\n'
                rowgroup_cells = [x.strip() for x in row.split('+')]
                for cellgroup in rowgroup_cells:
                    print '         cellgroup: ' + cellgroup
                    cellgroup = cellgroup.replace("r", ".r")
                    cellgroup = cellgroup.replace("c", ".c")
                    if cellgroup.startswith('.'): # http://stackoverflow.com/questions/19954593/python-checking-a-strings-first-and-last-character
                        cellgroup = '1' + cellgroup
                    cellgroup_attribs = [x.strip() for x in cellgroup.split('.')]
                    print '           cells: ' + cellgroup_attribs[0]
                    tstring += '    '
                    for cellcount in range(0,int(cellgroup_attribs[0])):
                        # tstring += '<td height=\''+str(rowheight_slug)+'\''
                        tstring += '<td'
                        cellcols = 1
                        try: # http://stackoverflow.com/questions/8570606/check-element-exists-in-array
                            for attrib in cellgroup_attribs[1:]: # skip the count, just check attrib(s)                                
                                if attrib.startswith('r'):
                                    tstring += ' rowspan=\'' + attrib[1:] + '\'' # value minus 'r' prefix
                                    print '           ---r attrib:' + attrib[1:]
                                elif attrib.startswith('c'):
                                    print '           ---c attrib:' + attrib[1:]
                                    tstring += ' colspan=\'' + attrib[1:] + '\'' # value minus 'c' prefix
                                    cellcols = int(attrib[1:]) ;  print '            colcells: ' + str(attrib[1:])
                                else:
                                    print 'ERROR: Bad attribute (no r/c prefix): ' + attrib
                        except IndexError:
                            pass
                        tstring += '></td>'
                        colcount = colcount + cellcols ; print '          colcount = ' + str(colcount)
                    tstring += '\n'
                    if colrowmax < colcount:
                        colrowmax = colcount
                    
                tstring += '  </tr>\n'
                colcount = 0
        tstring += '</table>\n'
        tstring = tstring.replace(colcount_slug, "<td></td>"*colrowmax)
        pghtmlstring += tstring # add latest table html to page html
        # print '\ntstring:\n' + tstring + '\n'            

    rowcount = pstr_rowcount(pstr)
    rowheight = 60/rowcount
    pghtmlstring = pghtmlstring.replace(rowheight_slug, str(rowheight))
    
    return pghtmlstring

#def pcode_to_html (panelcode):
#    """..."""
#    html_string = ''
#    html_string = '<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>'
#    return html_string

def pstr_to_svg (code_string):
    """render a panelcode string as an SVG image"""
    # svg+html template
    svg_xml1 = """<?xml version="1.0" standalone="yes"?>
<svg xmlns="http://www.w3.org/2000/svg" width="75" height="156" viewBox="0 0 75 156">
	<foreignObject x="10" y="10" width="60" height="48">
		<body xmlns="http://www.w3.org/1999/xhtml">
			<div style="font-size: 6pt">"""

    svg_xml2 = """</div>
		</body>
	</foreignObject>
	<foreignObject x="5" y="20" width="60" height="126">
		<body xmlns="http://www.w3.org/1999/xhtml">
			<style>
				table.page {
					layout: fixed;
					border: 1px solid black;
					width: 50px;
					padding: 0px;
					border-spacing: 0px 1px;
					background-color: #aaa;
				}
				table.page &gt; tr, table.page &gt; tr &gt; td {
					border: 0px solid red;
					border-collapse: collapse;
					padding: 0px;
					border-spacing: 0px;
				}
				table.row {
					layout: fixed;
					border: 0px solid black;
					width: 100%;
					height: 100%;
					padding: 0px;
					border-spacing: 2px 1px;
				}
				table.row &gt; tr &gt; td {
					# height: 10px;
					border: 1px solid black;
					padding: 0px;
					background-color: #fff;
				}
				tr.colspacer { visibility: hidden; height: 0px; }
				tr.colspacer > td { visibility: hidden; height: 0px; }
			</style>
			<table class="page">
				<tr>
					<td>
"""

    svg_xml3 = """
					</td>
				</tr>
			</table>
		</body>
	</foreignObject>
</svg>"""

    # convert panelcode to html and embed in template
    svg_text = svg_xml1 + str(code_string) + svg_xml2 + pstr_to_html(code_string) + svg_xml3

    return svg_text

#def pcode_to_svg (panelcode):
#    """..."""
    # return '...'


### FILE OUTPUT

def text_to_file (filename, content_string):
    """write text to a file"""    
    # text_to_file(page_output_dir + codestring + '.svg', pstr_to_svg(codestring))
    with open(filename, "w") as text_file:
        text_file.write(content_string)

def app_batch_svg (batchstring):
    """write a series of SVG files based on a string of many panelcodes"""
    svg_file_list = []
    batchstring = pstr_decomposite_pages(batchstring)
    print 'batchstring: '
    print batchstring
    pstrings = [x.strip() for x in batchstring.splitlines()]
    print 'pstrings: '
    print pstrings
    for pstr in pstrings:
        pstr=pstr_clean(pstr)
        if len(pstr)>0:
            text_to_file('../script/output/'+pstr+'.svg', pstr_to_svg(pstr))
            svg_file_list.append(str(pstr)+'.svg')

    app_svg_preview_page(svg_file_list,'../script/output/','index.html')
    # return '...'

def app_batch_html ():
    """..."""
    # return '...'

def app_svg_preview_page (filelist,outpath,outfilename):
    """..."""
    # app_svg_preview_page(svg_file_list,'script/output/','index.html')    
    preview_html1 = """<html>\n  <body>\n    <h1>Panelcode SVG output preview</h1>\n"""
    preview_html2 = """  </body>\n</html>"""
    with open('../script/output/index.html', "w") as index_file:
        index_file.write(preview_html1)
        for pgfile in filelist:
            index_file.write('    <img src="' + pgfile + '"/>\n')
        index_file.write(preview_html2)
