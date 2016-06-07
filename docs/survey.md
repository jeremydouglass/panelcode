## Survey


### Encoding tables

Currently many leightweight markup languages have support for tables as a page design element for organizing content. Tables are generally drawn in an ASCII-art fashion with pipes and dashes, or cell boundaries are minimally indicated, or some combination.

-  [Leightweight markup language > comparison of language features](https://en.wikipedia.org/wiki/Lightweight_markup_language#Comparison_of_language_features) -- see list with column on support for tables
	-  [lightweight markup > tables](http://www.appservgrid.com/hyper/hyp/lightweight-markup#tables-etal) -- a great comparison of syntax!!!
	-  http://www.subspacefield.org/~travis/static_blog_generators.html -- http://www.subspacefield.org/~travis/python_lightweight_markup_languages.html
   -  [skriv markup language - table syntax](http://markup.skriv.org/language/syntax#tables) -- here is an example (SkrivML) of the reasoning behind why lightweight markup languages don't support colspan or rowspan -- which means that the "ascii art" approach doesn't have widespread reference implementations for my purposes, and probably isn't practical from a data entry point of view. "The major goal with the table syntax was to provide a convenient way to create tables, without doing ascii-art. That's the reason why there is only two type of cells, no merged cells, and a very simple layout."
   -  [txt2tags](http://txt2tags.org/markup.html) is another example of a simple table format that can't accomodate rowspans etc.

Some noteable formats:

-  AsciiDoc
-  Markdown (extended)
-  reStructuredText
-  Textile
-  txtstags


###### (MORE) Reference designs


-  [HTML <td> rowspan Attribute](http://www.w3schools.com/tags/att_td_rowspan.asp)
-  [ASCIIdoc Tables](http://www.methods.co.nz/asciidoc/userguide.html#_tables)
-  [rst (reStructuredText) "Grid Tables" and "Simple Tables"](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#tables)

-  [Markdown](https://daringfireball.net/projects/markdown/)  tables -- [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)
-  [Emmet]() -- [Expand Abbreviation](http://docs.emmet.io/actions/expand-abbreviation/)

	> "Type a CSS-like abbreviation" ... e.g.
	
			#page>(#header>ul#nav>li*4>a)+(#content>h1{Hellow world}+p)+#footer

-  [Twiki Text Formatting Rules > Table](http://twiki.org/cgi-bin/view/TWiki/TextFormattingRules)
   
   some interesting ideas here on multi-spans... that might also be relevant to layout compositing...?

-  [Kramdown table syntax](http://kramdown.gettalong.org/syntax.html#tables) -- "based on PHP Markdown Extra package" -- but with documented differences from Extra:


#### AsciiDoc tables

-   colspans? YES
-   rowspans? YES

AsciiDoc actually supports complex semi-visual string syntax for rendering ascii tables with colspans, rowspans, and properties.

-  [AsciiDoc New tables in version 8.3.0](http://www.methods.co.nz/asciidoc/newtables.html)
   -   "The following additions were made at AsciiDoc 8.4.4: Cell column and row spanning."
   -   see: "Table 3. Columns formatted with strong, monospaced and emphasis styles"
   -   see: "Table 12. Spans, alignments and styles"
-  [AsciiDoc Syntax Quick Reference: Tables](http://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#tables)

A renderer might take a panelcode string and render AsciiDoc tables -- such a thing may already exist from some intermediate representation (e.g. HTML, XML).

One limitation is that, because AsciiDoc tables are fundamentally one html `<table>` they cannot support variable rows without some serious column math.

An importer might take an AsciiDoc table, parse it with AsciiDoc, and then import the parsed form (e.g. HTML, XML) into a Panelcode string. That could be an interesting trick, although drawing ASCII tables is a mess from a data entry point of view.

##### Example: an AsciiDoc table

Here is the AsciiDoc [example table](http://www.methods.co.nz/asciidoc/newtables.html).

**Spans, alignments and styles**

```AsciiDoc
.Spans, alignments and styles
[cols="e,m,^,>s",width="25%"]
|================
|1 >s|2 |3 |4
^|5 2.2+^.^|6 .3+<.>m|7
^|8
|9 2+>|10
|================
```

Use [asciidoclive.com](https://asciidoclive.com) and paste in for a live editable preview.

Here is the Panelcode equivalent of this layout:

```Panelcode
	4_(1+r2c2+r3,1,c2)
```

...and here is the original layout again in ASCIIdoc, this time unlabeled and with the absolute minimum markup:

**Minimal markup**

```AsciiDoc
|===
||||
| 2.2+| .3+|
|
| 2+|
|====
```

There are some interesting ideas here. AsciiDoc is parsing properties: (`2.2+`) becomes (`.r2c2`) in Panelcode. Also, because it supports basic alignment, it can display labeled panels:

**Sans text formatting, with center-middle text**

```
.Sans text formatting, with center-middle
[cols="^.^,^.^,^.^,^.^",width="50%"]
|================
|1 |2 |3 |4
|5 2.2+|6 .3+|7
|8
|9 2+|10
|================
```

Note that AsciiDoc tables aren't conceptually set up to render a different number of cells per row without cells having explicit column spans (which must be based on common factors between rows). In addition, the `cols` header argument is required if the first row stars with fewer than the maximum number of columns -- although it

This incorrectly renders a 12-cell, 4x3 grid. It ignores the visually formatted rows and just fills in cells -- once it has 11 cells in 3 rows of 4, it includes a 12th to round out the last row.

```
|===
||||
|||
||
||||
|===
```

This incorrectly renders an 8-cell, 2x8 grid, not 11 panels. The first two rows are forced to 4, and the last 3 cells are dropped because the row is incomplete. Ugh.

```
[cols="4"]
|===
||
|||
||
||||
|===
```

*In theory*, I could let people generate things like this:

```
|===
||
|||
||
||||
|===
```

...and then use a post-processor to make it a valid AsciiDoc table -- but I'm not sure what the point is compared to writing `2_3_2_4` -- it isn't even visually that informative without creative spacing, and even then it is misleading without cell contents, as the right-hand edge is invisible.

Supposing I also allowed people to add a terminal '|' and put in a content placeholder, then changed it to columned AsciiDoc after....

```
|===
| * | * |
| * | * | * |
| * | * |
| * | * | * | * |
|===
```

... *and* suppose that these not-so-informative images were visually spaced to create correct alignment:

```
|=======================|
|     *     |     *     |
|-----------------------|
|   *   |   *   |   *   |
|-----------------------|
|     *     |     *     |
|-----------------------|
|  *  |  *  |  *  |  *  |
|=======================|
```

...and the pre-processor would create a valid AsciiDoc table which aligns rows based on colspans (using common denominators):

```
[cols="12"]
|===
6+| 6+|
4+| 4+| 4+|
6+| 6+|
3+| 3+| 3+| 3+| 
|===
```

This last example uses common factors to label the columns, and renders correctly -- for the most part. Even if you solve width, not sure how to specify height, and the cells are weirdly not uniform in width -- left/right edge cells are bigger. But that is probably CSS styling, not a showstopper.


#### Markdown (extended) tables

-   rowspans? NO
-   colspans? NO

```markdown
|  header 1  |  header 2  |
|------------|------------|
|  row 1     |            |
|  row 2     |            |
|  row 3     |            |
```


#### reStructuredText tables

https://gist.github.com/dupuy/1855764 -- see "tables" section with example of reStructuredText

```reStructuredText
+-------+----------+------+
| Table Headings   | Here |
+-------+----------+------+
| Sub   | Headings | Too  |
+=======+==========+======+
| cell  | column spanning |
+ spans +----------+------+
| rows  | normal   | cell |
+-------+----------+------+
| multi | * cells can be  |
| line  | * formatted     |
| cells | * paragraphs    |
| too   |                 |
+-------+-----------------+
```

This is the full ascii concept. Might be fun for data entry? Parsing output doesn't even seem imaginable without a library to convert in either direction. Presumeably that tool is available. Might be interesting to export rowgroups ... or not.


#### Texttile tables

-   rowspans? YES
-   colspans? YES

Textile also supports colspan and rowspan -- while AsciiDoc anchors the modifier to the outside of the left cell divider, Textile uses the inside of the left cell divider.

-  https://txstyle.org/doc/15/tables

AsciiDoc colspan 2: ` 2.+|`  
AsciiDoc rowspan 2: ` .2+|`  
 Textile colspan 2: `|\2. `
 Textile rowspan 2: `|/2. `

##### Example: a Textile table

Interestingly, the Textile renderer performs a lot better (for panelcode purposes) with changing the cell counts in each row, in the sense that it doesn't attempt to rationalize them into a professionally formatted square the way that AsciiDoc does. By default, it produces a kind of bar chart -- as expected of something rendering to a single `<table>` object.

```textile
||
|||
||
||||
```

When given computed column hints (it does not require a header, as AsciiDoc does) it performs as well as AsciiDoc in generating a full page layout:

```textile
|\6. |\6. |
|\4. |\4. |\4. |
|\6. |\6. |
|\3. |\3. |\3. |\3. |
```

Considering that it concisely supports rowspan / colspan and doesn't require a ton of decoration, it would be trivial to write a Textile translator for rowgroups (not full layouts), like so:

Panelcode rowgroup:

```Panelcode
2r2+1,1
```

Textile equivalent:

```textile
|/2. |/2. | |
| |
```


#### txt2tags tables



#### Conclusion on lightweight markup tables

ULTIMATELY, when evaluated as data input, drawing little ascii art tables all seems like a crazy amount of data entry work for something that is ultimately only going to be good at representing clean row codes -- not anything fancy with rowheights. ascii-like processing all seems like a dead end.
