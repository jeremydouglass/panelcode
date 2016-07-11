# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m panelcode.panelcode

def html_wrap(html_string):
    """Add an html-head-body wrapper around an html string."""
    html_prefix="""<html>
        <head>
            <title>HTML CSS TESTS</title>
            <link rel="stylesheet" type="text/css" href="tests/manual html-css tests/html-css.css">
        </head>
        <body>"""
    html_postfix="""
    </body></html>
    """    
    return html_prefix + html_string + html_postfix


class PanelCode:
    """ this """
    def __init__(self, string):
        self.comment = "comment text"
        self.str = string
        self.code = (1,2,3)
    
    def to_html_table(self):
        str = """
<table class="table layout"><tr><td>
  <table class="table group">
    <tr class="row r3">
      <td class="cell panel">1</td>
    </tr>
  </table>
  <table class="table group">
    <tr class="row r3">
      <td class="cell panel">2</td>
      <td class="cell panel">3</td>
    </tr>
  </table>
  <table class="table group">
    <tr class="row r3">
      <td class="cell panel blank">4</td>
      <td class="cell panel uncoded">5</td>
      <td class="cell panel marked">6</td>
    </tr>
  </table>
</td></tr></table>
"""
        return str;
    
    def to_html_css_display_table(self):
        str = """
<div class="table layout">
  <div class="table group">
    <div class="row r3">
      <div class="cell panel">1</div>
    </div>
  </div>
  <div class="table group">
    <div class="row r3">
      <div class="cell panel">2</div>
      <div class="cell panel marked">3</div>
    </div>
  </div>
  <div class="table group">
    <div class="row r3">
      <div class="cell panel">4</div>
      <div class="cell panel blank">5</div>
      <div class="cell panel">6</div>
    </div>
  </div>
</div>
"""
        return str;
    
    def to_html_css_grid(self):
        return True;
    
    def to_html_css_flexbox(self):
        return True;

class PanelCodeSeries:
    """ this """

    def __init__(self,batchstring):
        """ """
        self.pcs=[x.strip() for x in batchstring.splitlines()]
        self.code_strings=' '.join(self.pcs)
        #for pstr in self.pcs:
        #     pstr = PanelCode(pstr).str
        #     print pstr

    def pcs(self):
        return self.pcs

    def code_strings(self):
        return self.code_strings
    
    def to_html_tables(self):
        tables = ""
        for i in self.pcs:
            j = i.to_html_table
            tables += str(i)
        return tables;
    
    def to_html_css_display_tables(self):
        str = ""
        for i in self.pcs:
            str += i.to_html_css_display_table
            return True;
    
    def to_html_css_grid(self):
        return True;
    
    def to_html_css_flexbox(self):
        return True;


def text_to_file (filename, content_string):
    """write text to a file"""    
    # text_to_file(page_output_dir + codestring + '.svg', pstr_to_svg(codestring))
    with open(filename, "w") as text_file:
        text_file.write(content_string)
