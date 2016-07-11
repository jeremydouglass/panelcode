# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_panelcode

from .context import panelcode
from panelcode import *
import unittest

# fileobj = file_to_text(file)

pc_series = PanelCodeSeries("(1,2,3)\n(1,1)\n(2,2,2,2)")
# print str(pc_series.code_strings)
# print pc_series.to_html_tables
print "pc_series.get_pcs(): "
print pc_series.pcs
print "pc_series.to_html_tables(): "
print pc_series.to_html_tables()
output=""
for i in pc_series.to_html_tables():
    output += str(i)
core.text_to_file("test_html_table.html", output)
core.text_to_file("test_html_css_display_table.html", pc_series.to_html_css_display_tables)
# text_to_file(pc_series.to_html_css_flexbox, "filename")
# text_to_file(pc_series.to_html_css_grid, "filename")


# pc_series = PanelCodeSeries("(1,2,3)\n(1,1)\n(2,2,2,2)")
# print str(pc_series.code_strings)
# output=""
# print pc_series.to_html_table
# for i in pc_series.to_html_table:
#     output += str(i)
# core.text_to_file("test_html_table.html", output)
# core.text_to_file("test_html_css_display_table.html", pc_series.to_html_css_display_table)
# # text_to_file(pc_series.to_html_css_flexbox, "filename")
# # text_to_file(pc_series.to_html_css_grid, "filename")