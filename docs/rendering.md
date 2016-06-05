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

Two overviews:  

-   https://wiki.python.org/moin/Templating
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


##### CSS3 grid layout (general)

Video on grid layout, ++:

-  https://www.w3.org/TR/css3-grid-layout/
-  https://www.sitepoint.com/community/t/keeping-some-perspective-on-flexbox/115090
   -  grid area examples - https://youtu.be/GRexIOtGhBU?t=601
   -  flexible length unit (fr) - https://youtu.be/GRexIOtGhBU?t=1261
   -  boxes spanning over the grid - https://youtu.be/GRexIOtGhBU?t=1360
   -  linked site -- Grid by Example - http://gridbyexample.com


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

```
	panelcode/2/3/2
	panelcode/2/5(1+r2+r2+r2,1)/4(r2+r2+1,1)
```


#### Direction renderers

Do these act as a pre-processing or post-processing step to HTML or SVG? Depends on the direction, perhaps no approach is generalizable due to the ways html tables or css grid work?


##### RTL rendering

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


Note on rendering:

-  http://stackoverflow.com/questions/1138639/css-tables-invert-order-of-displayed-content
-  https://www.sitepoint.com/community/t/is-changing-table-cell-order-possible/193238


##### Vertical rendering

```Panelcode
	vrt: 323
	vrt: 12345

```


