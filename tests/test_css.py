# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_basic

from .context import panelcode
import unittest

def html_wrap(html_string):
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

class CSSTestSuite(unittest.TestCase):
    """CSS test cases."""

    def test_html_css_display_table(self):
         
        testpcodestring = "(1,2)"
        # testpcode = (1,2)
        testpcode_list = ((1,2),(1,2,3),(1,2,3,4))
        output = "<h1>css display:table</h1>\n"

        for testpcode in testpcode_list:
            counter = 1
            output += """<div class="table layout">""" + '\n'
            for i in testpcode:
                output += """  <div class="table group">""" + '\n'
                output += """    <div class="row r""" + str(len(testpcode)) +  """">""" + '\n'
                for j in range(0,int(i),1):
                   output += """      <div class="cell panel">""" + str(counter) + """</div>""" + '\n'
                   counter += 1
                output += """    </div>""" + '\n'
                output += """  </div>""" + '\n'
            output += """</div>""" + '\n\n'
        output = html_wrap(output)
        print output
        
        core.text_to_file("temp-css.html", filename, output)
        
        # needs to be paired with `test/manual html-css tests/html-css.css`
        
        assert True

    # <h2>(1,2)</h2>
    # <div class="table layout">
    #   <!-- row of 1 -->
    #   <div class="table group">
    #     <div class="row r2">
    #       <div class="cell panel">1</div>
    #     </div>
    #   </div>
    #   <!-- row of 1 -->
    #   <div class="table group">
    #     <div class="row r2">
    #       <div class="cell panel">1</div>
    #       <div class="cell panel">1</div>
    #     </div>
    #   </div>
    # </div>

    def test_html_table(self):

        testpcodestring = "(1,2)"
        # testpcode = (1,2)
        testpcode_list = ((1,2),(1,2,3),(1,2,3,4))
        output = "<h1>html table</h1>\n"

        for testpcode in testpcode_list:
            counter = 1
            output += """<table class="table layout"><tr><td>""" + '\n'
            for i in testpcode:
                output += """  <table class="table group">""" + '\n'
                output += """    <tr class="row r""" + str(len(testpcode)) + """">""" + '\n'
                for j in range(0,int(i),1):
                   output += """      <td class="cell panel">""" + str(counter) + """</td>""" + '\n'
                   counter += 1
                output += """    </tr>""" + '\n'
                output += """  </table>""" + '\n'
            output += """</td></tr></table>""" + '\n'
        output = html_wrap(output)
        print output
        
        core.text_to_file("temp-html.html", filename, output)
        
        # needs to be paired with `test/manual html-css tests/html-css.css`
        
        assert True
    
    def test_html_css_display_flex(self):
        
        assert True

    def test_html_css_display_grid(self):
        
        assert True

    def test_svg(self):
        
        assert True



if __name__ == '__main__':
    unittest.main()


#   
#   class PanelCode:
#   	""" """
#   	def to_html_table(self):
#   		return True;
#   
#   	def to_html_css_display_table(self):
#   		return True;
#   
#   	def to_html_css_grid(self):
#   		return True;
#   
#   	def to_html_css_flexbox(self):
#   		return True;
#   
#   class PanelCodeSeries:
#   	""" """
#   	def to_html_table(self):
#   		return True;
#   
#   	def to_html_css_display_table(self):
#   		return True;
#   
#   	def to_html_css_grid(self):
#   		return True;
#   
#   	def to_html_css_flexbox(self):
#   		return True;
#   
#   
#   def text_to_file(text, filepath)
#   		return True;
#   
#   
#   fileobj = file_to_text(file)
#   pc_series = PanelCodeSeries( file or text)
#   print pc_series.code_strings
#   text_to_file(pc_series.to_html_tables, "filename")
#   text_to_file(pc_series.to_html_css_display_tables, "filename")
#   # text_to_file(pc_series.to_html_css_flexbox, "filename")
#   # text_to_file(pc_series.to_html_css_grid, "filename")


