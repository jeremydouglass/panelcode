# -*- coding: utf-8 -*-

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

def pstr_rowcount (pgstring):
    """..."""
    rowcount = 0
    rowarray = pgstring.split('_')
    row_marker = '_'
    tgroup_start = '('
    tgroup_end = ')'
    # rowarray = re.split("\()|_", pghtmlstring)' # http://stackoverflow.com/questions/1059559/python-split-strings-with-multiple-delimiters
    tables = [x.strip() for x in pgstring.split(row_marker)] # http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
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

def pstr_to_svg (code_string):
    """..."""
    # svg+html template
    svg_xml1 = """<?xml version="1.0" standalone="yes"?><svg width="75" height="126" viewBox="0 0 75 126" xmlns="http://www.w3.org/2000/svg"><foreignObject x="5" y="10" width="60" height="75"><body xmlns="http://www.w3.org/1999/xhtml"> <style> table.page{ layout: fixed; border: 1px solid black; width: 50px; padding: 0px; border-spacing: 0px 1px; background-color: #aaa; } table.page > tr, table.page > tr > td { border: 0px solid red; border-collapse: collapse; padding: 0px; border-spacing: 0px; } table.row { layout: fixed; border: 0px solid black; width: 100%; height: 100%; padding: 0px; border-spacing: 2px 1px; } table.row > tr > td { # height: 10px; border: 1px solid black; padding: 0px; background-color: #fff; } </style><table class='page'><tr><td>"""
    svg_xml2 = """</td></tr></table></body></foreignObject><foreignObject x="10" y="85" width="60" height="48"><body xmlns="http://www.w3.org/1999/xhtml"><div style='font-size: 6pt'>"""
    svg_xml3 = """</div></body></foreignObject></svg>"""

    # convert panelcode to html and embed in template
    svg_text = svg_xml1 + pstr_to_html(code_string) + svg_xml2 + str(code_string) + svg_xml3

    return svg_text

#def pcode_to_svg (panelcode):
#    """..."""
    # return '...'

def pstr_to_html (pgstring):
    """..."""
    pghtmlstring = ''
    pghtmlstring = '<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>'

    tgroup_start = '('
    tgroup_end = ')'
    # print '\n----------------------------------------'
    # print '\npgstring: ' + pgstring
    tables = [x.strip() for x in pgstring.split('_')] # http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
    rowheight = 'rowheight' # slug for replacing last, since we count rows as we go.
    rowcount = 0
    for table in tables:
        print '     table: ' + str(table)
        tstring = ''
        tstring = '<table class=\'row\' height=\''+str(rowheight)+'\'>\n'
        if "(" not in table: # http://stackoverflow.com/questions/5473014/test-a-string-for-a-substring
            rowcount += 1 # increment
            tstring += '  <tr height=\''+str(rowheight)+'\'>\n'
            # tstring += '  <tr>\n'
            tstring += '    '
            for cellcount in range(0,int(table)):
                tstring += '<td></td>'
            tstring += '\n'
            tstring += '  </tr>\n'
        elif "(" in table: # http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
            tbgroup = ((table.split(tgroup_start))[1].split(tgroup_end)[0]) #http://stackoverflow.com/questions/3368969/find-string-between-two-substrings
            print '       tbgroup: ' + tbgroup
            tbgroup_rows = [x.strip() for x in tbgroup.split(',')]
            rowmax = 1 # starting value
            for row in tbgroup_rows:
                print '         row: ' + row
                tstring += '  <tr height=\''+str(rowheight)+'\'>\n'
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
                        # tstring += '<td height=\''+str(rowheight)+'\''
                        tstring += '<td'
                        try: # http://stackoverflow.com/questions/8570606/check-element-exists-in-array
                            for attrib in cellgroup_attribs[1:]: # skip the count, just check attrib(s)
                                if attrib.startswith('r'):
                                    tstring += ' rowspan=\'' + attrib[1:] + '\'' # value minus 'r' prefix
                                    print '---r attrib:' + attrib[1:]
                                    rowmax = max(rowmax,int(attrib[1:])) # update with tallest panel
                                elif attrib.startswith('c'):
                                    tstring += ' colspan=\'' + attrib[1:] + '\'' # value minus 'c' prefix
                                else:
                                    print 'ERROR: Bad attribute (no r/c prefix): ' + attrib
                        except IndexError:
                            pass
                        tstring += '></td>'
                    tstring += '\n'
                tstring += '  </tr>\n'
            rowcount = rowcount + rowmax
            print '   rowmax:   ' + str(rowmax)
            print '   rowcount: ' + str(rowcount)
        tstring += '</table>\n'
        pghtmlstring += tstring # add latest table html to page html
        # print '\ntstring:\n' + tstring + '\n'

    print 'OLD rowcount check: ' + str(rowcount)
    rowcount = pstr_rowcount(pghtmlstring)
    print 'NEW rowcount check: ' + str(rowcount)
    rowheight = 60/rowcount
    pghtmlstring = pghtmlstring.replace("rowheight", str(rowheight))
    
    return pghtmlstring

#def pcode_to_html (panelcode):
#    """..."""
#    html_string = ''
#    html_string = '<table><tr><td></td><td></td></tr><tr><td></td><td></td></tr></table>'
#    return html_string

def text_to_file (filename, content_string):
    """..."""    
    # text_to_file(page_output_dir + codestring + '.svg', pstr_to_svg(codestring))
    with open(filename, "w") as text_file:
        text_file.write(svgfile)

def app_batch_svg ():
    """..."""
    # return '...'

def app_batch_html ():
    """..."""
    # return '...'

def app_svg_preview_page (filelist,outpath,outfilename):
    """..."""
    # app_svg_preview_page(svg_file_list,'script/output/','index.html')    
    preview_html1 = """<html>\n  <body>\n    <h1>Panelcode SVG output preview</h1>\n"""
    preview_html2 = """  </body>\n</html>"""
    with open('script/output/index.html', "w") as index_file:
        index_file.write(preview_html1)
        for pgfile in filelist:
            index_file.write('    <img src="' + pgfile + '"/>\n')
        index_file.write(preview_html2)
