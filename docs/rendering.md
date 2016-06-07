## Rendering

-  renderers:
	- [x]  html tables -- note on rendering https://css-tricks.com/complete-guide-table-element/
	- [ ]  html [divs](http://alistapart.com/article/holygrail
	- [ ]  html css [display:table](http://colintoh.com/blog/display-table-anti-hero)
	       -  http://www.w3schools.com/css/css_combinators.asp
	- [ ]  html css [flexbox grid system](http://philipwalton.github.io/solved-by-flexbox/demos/grids/) -- NOTE see http://www.slideshare.net/DavideDiPumpo/understanding-flex-box-css-day-2016  --  http://codepen.io/MakhBeth/pen/oxZMjM -- see slide 33-on Flex basis (33), flex-direction (column reverse) (42), browser compat (59), (65) "Flexbox is basically designed for: 1. content driven layout 2. component 3. not for grid (take a look at [css grid](https://www.w3.org/TR/css-grid-1/)"
	- [ ]  html [css grid](https://www.w3.org/TR/css-grid-1/) !!!!
	- [_]  html css...? PANEL SHAPES (e.g. trapezoid and parallelograms panels, circle, etc. see https://sarasoueidan.com/blog/css-shapes/ -- https://css-tricks.com/examples/ShapesOfCSS/
	- [x]  SVG images
	- [ ]  XML + XSLT
	- [ ]  TEI CBML 
	- [ ]  ComicsML
	- [ ]  CBZ and CBR embedding of a .panelcode file?
	- [ ]  ...?
	- [ ]  Process? [*](http://www.amazon.com/Algorithms-Visual-Design-Processing-Language/dp/0470375485)
-  syntax highlighter (Prism / regex)



### strategies


#### highlighting

provide a specific panel index number to highlight in a layout


#### populating

Following ASCIIdoc, bind a panelcode to a CSV file of content files -- or bind a series of panelcodes to a CSV file.


## Renderers


##### HTML CSS display:table

-  [The Anti-hero of CSS Layout - "display:table"](http://colintoh.com/blog/display-table-anti-hero)

html:
```
<div class="layout">
  <div class="group">
    <div class="panel"></div>
    <div class="panel"></div>
  </div>
</div>
```

css:
```

```



##### HTML rendering template -- first draft

panelcode-style-scratch:

`html_start`:

html/css:
```
    <html>
      <head>
        <style>
    		table.page{
    			layout: fixed;
    		    border: 1px solid black;
    			width: 50px;
    			padding: 0px;
                border-spacing: 0px 1px;
                background-color: #aaa;
    		}
    		table.page > tr, table.page > tr > td {
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
    		table.row > tr > td {
    			# height: 10px;
    			border: 1px solid black;
                padding: 0px;
                background-color: #fff;
    		}
        </style>
      </head>
      <body>
```


`html_page_start`:

html:
```
	<table class='page'>
	  <tr><td>
```


`html_page_stop`:

html:
```
          </td></tr>
        </table>
```


`html_stop`:

html:
```
        </td></tr></table>
      </body>
    </html>
```


##### HTML templating in Python

Two overviews of (html) templating (in Python):  

-   https://wiki.python.org/moin/Templating
	-   note in particular the section "HTML Shorthand Processors"
-   https://www.fullstackpython.com/template-engines.html

Discussion and examples:  

-   http://stackoverflow.com/questions/11646948/simple-html-template-in-python
-   http://www.makotemplates.org/
-   http://jinja.pocoo.org/
-   http://pwp.stevecassidy.net/bottle/templating.html


css:
```
	table.page{
	    border: 1px solid black;
		width: 50px;
		height: 65px;
		padding: 3px;
	}
	table.row > tr, table.row > tr > td {
	    border: 1px solid black;
	    width: 100%;
	    height: 10px;
	}
```

##### HTML parse-as-you-go

-   [Set cellpadding and cellspacing in CSS?](http://stackoverflow.com/questions/339923/set-cellpadding-and-cellspacing-in-css)

-  http://ansciath.tumblr.com/post/8535845053/simulating-colspan-1-plus
-  http://www.rachaelarnold.com/dev/archive/advanced-html-tables-columns
-  http://stackoverflow.com/questions/19402189/how-to-make-a-table-in-html-with-variable-and-fixed-column-widths-and-grouping-h

-  [HTML.py](http://www.decalage.info/en/python/html) - " a Python module to easily generate HTML tables and lists"
-  Python > Structured Markup Processing Tools
	-  HTMLParser https://docs.python.org/2/library/htmlparser.html


early draft ideas parsing and expansion / compression / shorthand

as follows:

	  _ = add row in page (`table`)
	  , = add row group row (`tr`)
	  + = add row group row cell (`td`)

	 ++ = add page in horizontal pagegroup (`tr`)
	 ,, = add page in vertical pagegroup (`td`)

	1-9 = cell series (e.g. 3 = `td td td`)
	  0 = placeholder cell not outlined or counted towards layout (`td`)
	 r# = rowspan
	 c# = colspan

	{#} = for numbers over 9 in shorthand code only

Parens `(` `)` aid readability, but don't actually do anything.

	333 = 3x3
	3_3_3 = (3)_(3)_(3)
	1+1+1_1+1+1_1+1+1 = (1+1+1)_(1+1+1)_(1+1+1)

You can't make the number in front of the r optional -- even if it is a 1, it has to be written, otherwise this is ambiguous without _ or ()

	332r2+1,14

could mean either:

	332r2+1,14 = 332(r2+1,1)4
	332r2+1,14 = 33(2r2+1,1)4

...so we can fix this ambiguity by requiring the number:

	3321r2+1,14 = 332(1r2+1,1)4
	332r2+1,14  = 33(2r2+1,1)4

...or we could require 	underscores always:

	3_3_2_r2+1,1_4 = 3_3_2_(r2+1,1)_4

...or we could require parens always:
		
	332(r2+1,1)4

Consider this page:

	1_(r4+c4,r3+c3,r2+c2,2)

	(333),2(1r2+2,2)
	((3),(3),(3)),((2)((1).r2(2),(2)))
	
	a__b

	3_3_3,,2_(1r2_2,1)

	(333),,
	(333)++

	{} = numbers
	() = groups (rowgroups) -- tables
	[] = pages
	[],[]

###### calculating row heights in dynamic comic page images

-  [100% Height table using DOCTYPE XHTML 1.0](http://forums.asp.net/t/942037.aspx?100+Height+table+using+DOCTYPE+XHTML+1+0)

>  Try adding this little piece of css and see the difference:
>
>		<style type="text/css">
>			html, body, form, div {height:100%;}
>		</style>

See also discussions:

-  [in CSS, how can I make a table expand to fill a container div?](http://stackoverflow.com/questions/23344002/in-css-how-can-i-make-a-table-expand-to-fill-a-container-div)
-  [DocType xhtml1-transitional.dtd ignores table cell height](http://stackoverflow.com/questions/358791/doctype-xhtml1-transitional-dtd-ignores-table-cell-height)
-  [Fix height of a table row in HTML Table](http://stackoverflow.com/questions/593849/fix-height-of-a-table-row-in-html-table)
-  [XHTML and Table Height](http://www.bernzilla.com/item.php?id=116) (2003)
-  [Making a table row fill 100% of remaining height (CSS in IE)](http://able2know.org/topic/39500-1)
-  [How to set 100% table height in html](http://www.dailycoding.com/posts/howtoset100tableheightinhtml.aspx)




##### CSS3 grid layout (general)

Video on grid layout, ++:

-  https://www.w3.org/TR/css3-grid-layout/
-  https://www.sitepoint.com/community/t/keeping-some-perspective-on-flexbox/115090
   -  grid area examples - https://youtu.be/GRexIOtGhBU?t=601
   -  flexible length unit (fr) - https://youtu.be/GRexIOtGhBU?t=1261
   -  boxes spanning over the grid - https://youtu.be/GRexIOtGhBU?t=1360
   -  linked site -- Grid by Example - http://gridbyexample.com

css3 grid and flexbox:

-  https://www.w3.org/TR/css3-grid-layout/
-  [Why Flexboxes Aren't Good for Page Layout](http://www.xanthir.com/blog/b4580)
-  http://codepen.io/ilancohen/pen/dEeBJ
-  http://stackoverflow.com/questions/22895011/rowspan-behavior-with-flexbox
-  http://stackoverflow.com/questions/25600320/css-flexbox-same-column-width-at-colspan


#### Rowgroup rendering


#### SVG rendering

```bash
	panelcode/2_3_2.svg
	panelcode/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg
```

###### HTML SVG output -- a weird issue with row compression

If I try to use rowheight to create 3 rows, but the representation is compressable to 2, then weird things happen. In particular check out how this image is shorter than every other page image -- that is because the code calculates it (correctly) as having a row height of 5, but it is rendered out by SVG XHTML as if it had a row height of 4. This may be my fault, because I forced...


file:///Users/jeremydouglass/Desktop/comics%20panel%20data/script/comic-table-test-2.html


Output:

```
pgstring: 3_7(2+r3+1,r2+r2+r2)_2
     table: 3
     table: 7(2+r3+1,r2+r2+r2)
       tbgroup: 2+r3+1,r2+r2+r2
         row: 2+r3+1
         cellgroup: 2
           cells: 2
         cellgroup: r3
           cells: 1
---r attrib:3
         cellgroup: 1
           cells: 1
         row: r2+r2+r2
         cellgroup: r2
           cells: 1
---r attrib:2
         cellgroup: r2
           cells: 1
---r attrib:2
         cellgroup: r2
           cells: 1
---r attrib:2
   rowmax:   3
   rowcount: 4
     table: 2
```

```html
<table class='row' height='rowheight'>
  <tr height='rowheight'>
    <td></td><td></td><td></td>
  </tr>
</table>
<table class='row' height='rowheight'>
  <tr height='rowheight'>
    <td height='rowheight'></td><td height='rowheight'></td>
    <td height='rowheight' rowspan='3'></td>
    <td height='rowheight'></td>
  </tr>
  <tr height='rowheight'>
    <td height='rowheight' rowspan='2'></td>
    <td height='rowheight' rowspan='2'></td>
    <td height='rowheight' rowspan='2'></td>
  </tr>
</table>
<table class='row' height='rowheight'>
  <tr height='rowheight'>
    <td></td><td></td>
  </tr>
</table>
```


```
rowcount:  5
rowheight: 12
 filename: output2/3_7(2+r3+1,r2+r2+r2)_2.svg
```


#### RESTful rendering

Someday.

Produce a url path / file path based on rowgroups. Mix with canonical for an addressing scheme -- although hashes....

```
	panelcode/2/3/2
	panelcode/2/5(1+r2+r2+r2,1)/4(r2+r2+1,1)
```


#### TEI

-   Interoperation with [DHQ comics TEI]


#### Direction renderers

Do these act as a pre-processing or post-processing step to HTML or SVG? Depends on the direction, perhaps no approach is generalizable due to the ways html tables or css grid work?

In general, how does layout order relate to reading order -- whether left-to-right right-to-left, or simply the implied sequence of panels being read. For example, could the system output tables with each `<td>` element marked with its reading order number / tab index? Marking this automatically could be hard in some cases, for example:

	1_(r2+1+r2+r2,1) --.2pg

The rowgroup is actually meant to be read with the `,1` panel third, but it is listed last because it is the only panel that starts on the second row.




#### Right-to-Left (RTL) layout renderer

The majority of global comics appear in one of two reading orders -- LTR(Left-To-Right) and RTL(Right-To-Left). **Panelcode** can mark up for either and convert between them.

Note that simple **Panelcode** is already symmetrical -- `3_2_3` 
 so `ltr--323` is the same as `rtl--323`. However the distinction may still be useful for renderers that tag the panels with a panel order

```Panelcode
	     2_3_3(1+r2,1)   # example layout
	ltr--2_3_3(1+r2,1)   # same layout, panels will be tagged 12 345 ...
	rtl--2_3_3(1+r2,1)   # same layout, panels will be tagged 21 543 ...
	ltr--2_3_3(r2+1,1)   # mirrored layout, tagged 12 345 ...
	rtl--2_3_3(r2+1,1)   # mirrored layout, tagged 21 543 ...

```

![Panelcode](Panelcode/script/output2/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg)

![Panelcode](Panelcode/script/output2/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg)

```python
	rtl(" 2_3_3(1+r2,1) ")  
	# -->  rtl--2_3_3(r2+1,1)
```

![Panelcode](Panelcode/script/output2/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg)

![Panelcode](Panelcode/script/output2/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg)


Row groups encode terms left-to-right: (r2+1) describes a 4-panel group with a column on the left-hand side. However, codes might be encoded in one order and output in another -- for example, to map reading orders (rather than physical layouts) in a hybrid collection, or to indicate data collection that encodes a different order, or to translate mirrored-page encoding back to an encoding of the original.

rtl_render()
	(adds the "rtl" inheritable property to tables,.)

	-  http://stackoverflow.com/questions/15293808/printing-table-cells-from-right-to-left
	-  http://stackoverflow.com/questions/16805147/table-columns-starts-from-right-to-left
	-  http://www.i18nguy.com/markup/right-to-left.html
	-  http://www.w3schools.com/tags/att_global_dir.asp

rtl_convert()
	(r2+2,r2+1,2) --> (2+r2,1+r2,2)
	(r3+r2+1,1,c2) --> (1+r2+r3,1,c2)

In a mixed set of strings with different reading orders, using the 'RTL_' prefix indicates groups are meant to be interpreted right-to-left.

	RTL_3(r2+1,1)_2 == 3(1+r2,1)_2

Note on rendering:

-  http://stackoverflow.com/questions/1138639/css-tables-invert-order-of-displayed-content
-  https://www.sitepoint.com/community/t/is-changing-table-cell-order-possible/193238



#### Vertical renderer

Someday

```Panelcode
	vrt: 323
	vrt: 12345

```

e.g. `v.4_4` ?





## ----------

## DEV NOTES

-  ***** [web2py - the views - table](http://web2py.com/books/default/chapter/29/05/the-views#TABLE--TR--TD) — this looks like a great simple way to render out arrays as html tables.


### type-to-display

imagine an ajax interface in which it is constantly showing you the rendered layout so long as it is complete! best data entry aid ever.


### nested structure manipulation

General nested structure manipulation in Python, and as it relates to HTML, JSON, etc....

I got this working as a hack-y string-parser and string-builder. It doesn't play well with malformed strings at all, and is incredibly specific about the way it builds. I can (should) refactor (as there is no factoring at all right now -- I just wrote the whole thing without functions) -- BUT one question is whether there arae libraries for internal native representations that would work better. I'm thinking of either / and native python lists/dictionaries, Javascript JSON arrays/objecs, and/or HTML tree building (DOM etc.).

Given a command string, could it be parsed into, say, a nested Python dictionary/list; then either exposed as JSON for other analysis or rendering programs, OR rendered as HTML for my SVG generator.

-   [Python: Read/Write to JSON](http://xahlee.info/perl-python/python_json_tutorial.html)
-   [How to parse a string and return a nested array?](http://stackoverflow.com/questions/17140850/how-to-parse-a-string-and-return-a-nested-array)
-   [String to (Multidimensional) List Conversion](http://codereview.stackexchange.com/questions/62704/string-to-multidimensional-list-conversion)
-   [Convert string with parantheses into nested list](http://stackoverflow.com/questions/8651110/convert-string-with-parantheses-into-nested-list)
-   FROM: [Google "python string into nested array"](https://www.google.com/search?q=python+string+into+nested+array)

There are also a lot of python libraries for representing JSON arrays visually **as** tables. So perhaps one of them could be co-erced into being a rendering pipeline for this?

-   [Google search: python string into nested array](https://www.google.com/search?q=python+string+into+nested+array)
-   [python json representation of html table](https://www.google.com/search?q=python+json+representation+of+html+table)

It looks like no -- the entire paradigm isn't quite right. There are two broad families of libraries:

1. libraries for **visualizing** JSON -- for inspection and documentation. They are all too specific to work with comic layouts -- often very key-value oriented and focused on deep nesting.
2. general purpose libraries for rendering html structures. at least one of these supports colspan, but none support rowspan.
3. Except maybe this one!

-   [HTML.py - a Python module to easily generate HTML tables and lists](http://www.decalage.info/en/python/html) -- has colspan support (see comment) -- and the (extremely verbose) "attribs" class MIGHT also support rowspan!

Another possibility, maybe:

-   [Tableutils](http://bolton.readthedocs.io/en/latest/tableutils.html)

Unlikely or definitely not:

-   [JSON2HTML](https://pypi.python.org/pypi/json2html) - no rowspan or colspan
    -   Demo [JSON to Human friendly Tabular format](http://json2html.varunmalhotra.xyz/#sendButton) `{"sample": [ {"a":1, "b":2, "c":3}, {"a":5, "b":6, "c":7} ] }`
-   [JSON Table Schema](http://dataprotocols.org/json-table-schema/) -- this is really for thinking about SQL and CSV data, so no rowspan / colspan type concepts
-   Simple snippet: [JSON to HTML table 2.0](http://www.smipple.net/snippet/aucontraire/JSON%20to%20HTML%20table%202.0) -- no rowspan or colspan


### Pre-caching row nums

Simple panelcodes are a numeric series. To pre-render all panelcodes containing 1-4 elements per row, and 1-4 rows, is (elements^(rows-1)) = (4^3) = 64 codes.

	1 ; 1_1 ; 1_2 ; 1_3 ; 1_4 ; 2_1 ; 2_2 ; 2_3 ...
	... 3_1_1_1 ; 3_1_1_2 ; 3_1_1_3 ; 3_1_1_4 ... 
	... 4_4_4_1 ; 4_4_4_2 ; 4_4_4_3 ; 4_4_4_4.

To pre-render 0-9 elements per row for up to 10 rows is a set of codes from `0` to `9_9_9_9_9_9_9_9_9_9` is, not surprisingly, 10^9, or 10,000,000,000 codes. However, in practice the vast majority of layouts are 5x5 or less -- that is 6^4 ([0 through 5]^(5-1)), or 1296.

### xml and xpath

-   [Wither](https://pypi.python.org/pypi/wither) "is a library designed to make XML generation under python as simple and as nicely formatted as python code." -- 2014


-  XPath? -- http://www.w3schools.com/xsl/xpath_nodes.asp

```xml
<?xml version="1.0" encoding="UTF-8"?>

<work>
  <pagegroup>
    <page>
      <row>
        <panel/><panel>
        <panel/><panel>
      </row>
      <rowgroup>
        <row>
          <panel/><panel>
          <panel/><panel>
        </row>
        <row>
          <panel/><panel>
          <panel/><panel>
        </row>
      </rowgroup>
    </page>
  </pagegroup>
</work>
```


-   example: http://www.w3schools.com/xml/schema_howto.asp

Schema: http://www.w3schools.com/xml/schema_complex.asp

```xml
<?xml version="1.0"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://www.w3schools.com"
xmlns="http://www.w3schools.com"
elementFormDefault="qualified">

<xs:element name="note">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="to" type="xs:string"/>
      <xs:element name="from" type="xs:string"/>
      <xs:element name="heading" type="xs:string"/>
      <xs:element name="body" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>

</xs:schema>
```



## ----------
