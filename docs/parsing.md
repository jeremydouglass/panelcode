## Parsing


-  domain specific languages / mini-languages
	-  http://stackoverflow.com/questions/1547782/mini-languages-in-python
	-  https://news.ycombinator.com/item?id=403690
		- http://weblog.jamisbuck.org/2006/4/20/writing-domain-specific-languages
		- http://code.activestate.com/recipes/534150/
	-  https://www.python.org/community/sigs/retired/parser-sig/towards-standard/

-  [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/) -- 2015 -- see also list of other tools
	-  http://www.antlr.org/
	-  http://simpleparse.sourceforge.net/ -- http://simpleparse.sourceforge.net/simpleparse_grammars.html
	-  http://pages.cpsc.ucalgary.ca/~aycock/spark/ -- 2009
	-  http://theory.stanford.edu/~amitp/yapps/
	-  http://pythonhosted.org/pyrser/quickstart.html
-  https://github.com/Mappy/PyLR
-  http://web.archive.org/web/20090225132556/http://www.evanfosmark.com/2009/02/sexy-lexing-with-python/


### EBNF for Panelcode

I'm going to write a BNF definition, and then a set of `pyparser` functions, according to this guide:

-  **** [Pyparsing introduction: BNF to code
](http://eikke.com/pyparsing-introduction-bnf-to-code/index.html)
-  also:
   -  *** [pyparsing quick reference](http://infohost.nmt.edu/tcc/help/pubs/pyparsing/pyparsing.pdf)
   -  [Convert BNF grammar to pyparsing](http://stackoverflow.com/questions/27926697/convert-bnf-grammar-to-pyparsing)
   -  [Pyparseltongue: Parsing Text with Pyparsing](https://www.accelebrate.com/blog/pyparseltongue-parsing-text-with-pyparsing/)

-  a **panelcode** string is any collection of pageset, pagegroup, and page definitions.
-  a **pageset** is a collection of pagegroup or page statements
-  a **pagegroup** is the horizontal or vertical concatonation of two or more pages
-  a **page** is a layout

...


```ebnf
%start panelcode

<panelcode>         :=  <page> | <pagegroup>
	                    | <page> <linebreak> <panelcode>
						| <pagegroup> <linebreak> <panelcode>

<pagegroup>         :=  <page> <pagejoin> <page> | <page> <pagejoin> <pagegroup>
  <pagejoin>        :=  <horizontaljoin> | <verticaljoin>
  <horizontaljoin>  :=  "++";
  <verticaljoin>    :=  ",,";

<page>              :=  <row> | <row> <rowseparator> <page> | <emptypage> | <uncodedpage>
  <rowseparator>    :=  "_";
  <emptypage>       :=  <emptyrow>
  <uncodedpage>     :=  <uncodedrow>

<row>               :=  <numrow> | <grouprow> | <emptyrow> | <uncodedrow>
  <numrow>          :=  <numbers> | <numbers> <rowseparator> <row>
  <emptyrow>        :=  "0"
  <uncodedrow>      :=  <groupopen> "_" <groupclose>

<grouprow>          :=  <groupopen> <grouprowcontents> <groupclose>
	                    | <decorativenum> <groupopen> <grouprowcontents> <groupclose>
  <decorativenum>   :=  <numbers>
  <groupopen>       :=  "("
  <groupclose>      :=  ")"

<grouprowcontents>  :=  <groupunit> | <groupunit> <groupseparator> <groupunit>
  <groupseparator>  :=  <newcol> | <newrow>
    <newcol>        :=  "+"
	<newrow>        :=  ","
  <groupunit>       :=  <emptyrow> | <numbers> | <numbers> <spanmodifier> | <spanmodifier>
    <spanmodifier>  :=  <rowspan> | <colspan> | <rowspan> <colspan> | <colspan> <rowspan>
      <rowspan>     :=  "r" <numbers>
      <colspan>     :=  "c" <numbers>

<digits>            :=  <digit> | <digit> <digits>
<digit>             :=  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<numbers>           :=  <number> | <number> <digits>
<number>            :=  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<letter>            :=  a | b | c | ... | y | z

```

An example:

```ebnf
<root>   :=     <tree> | <leaves>
<tree>   :=     <group> [* <group>] 
<group>  :=     "{" <leaves> "}" | <leaf>;
<leaves> :=     {<leaf>;} leaf
<leaf>   :=     <name> = <expression>{;}

<name>          := <string_without_spaces_and_tabs>
<expression>    := <string_without_spaces_and_tabs>
```

BNF NOTES

-  **** http://classes.engineering.wustl.edu/cse425s/resources/bnf/
-  **** http://www.cs.utsa.edu/~wagner/CS3723/grammar/examples2.html
-  *** https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form
-  *** https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form
-  also
-  http://www.garshol.priv.no/download/text/bnf.html

...contains mention of BNF, Bison and YACC. 

-  http://stackoverflow.com/questions/14013792/how-to-implement-backus-naur-form-in-python
-  http://dinosaur.compilertools.net/bison/bison_4.html
-  https://en.wikipedia.org/wiki/Yacc
-  https://en.wikipedia.org/wiki/LALR_parser
-  https://www.quora.com/How-can-I-parse-and-evaluate-a-BNF-using-Flex-Bison
-  http://www.tldp.org/HOWTO/Lex-YACC-HOWTO.html
-  http://stackoverflow.com/questions/33645123/bnf-to-flex-bison


### Pyparsing

Pyparsing documentation is a bit all over the place.

Bought this book:

-  file:///Users/jeremydouglass/Downloads/Getting_Started_with_Pyparsing.pdf
-  http://infohost.nmt.edu/tcc/help/pubs/pyparsing/pyparsing.pdf

1.  [pyparsing quick reference: A Python text processing tool](http://infohost.nmt.edu/tcc/help/pubs/pyparsing/pyparsing.pdf) (John Shipman, 2013) -- collects many links to other information on p3.
2. The "Getting Started with Pyparsing" ebook, which I purchase from O'Reilly ($10)
3. [abaraw: A shorthand notation for bird records](http://infohost.nmt.edu/~shipman/aba/raw/doc/web/index.html) -- John Shipman
	-  this looks like EXACTLY what I need to do, -- everything from parsing shorthand to structured XML output. With full documentation and source.
	-  The source code -- check out section beginning below buildParser() -- http://infohost.nmt.edu/~shipman/aba/raw/doc/ims/abaraw
	-  documentation -- http://infohost.nmt.edu/~shipman/aba/raw/doc/ims/web/parseInput.html
	-  http://infohost.nmt.edu/~shipman/aba/raw/doc/ims/web/EXPLICIT_COUNT.html

4. ONLamp article, 2006 -- http://www.onlamp.com/lpt/a/6435
5. You can read the actual source code of the installed module:

	`mate /Users/jeremydouglass/.virtualenvs/panelcode/lib/python2.7/site-packages/pyparsing.py`

6. [pyparsing Documentation](http://pyparsing.wikispaces.com/Documentation) -- although a bit all over the place, some out of date, and hard to navigate


-  **** [pyparsing](http://pyparsing.wikispaces.com/)
	-  **** http://eikke.com/pyparsing-introduction-bnf-to-code/


### preparsing

-  `pc_text`: a text block. code lines (may be compound with ;), allows comment lines, end line comments, blank lines. may include shorthand(s).
-  `pc_tabs`: tab-separated values, containing a header row, a first column of panelcodes with allowed comments, optional additional rows separated by tabs. is also a valid pc_text file. may include shorthand(s).
-  `pc_mini`: a text block, minified -- no comments, all line breaks replaced with `;` . may include shorthand(s).
-  `pc_list`: a data structure, each member is a `pc_code`. codes may not be compound (;) or include comments (#). entries may not be blank or invalid. a pc list is assumed `clean.`

|  data            |  blanks?      |  end-comments?  |  line-comments?  |  shorthands?  |  compound-lines? (;)  |
| -----------------|---------------|-----------------|------------------|---------------|-----------------------|
|  `pc_text`       |  Y            |  Y              |  Y               |  Y            |  Y                    |
|  `pc_tabs`       |               |  Y*             |  Y               |  Y            |  Y                    |
|  `pc_mini`       |               |  NA             |  Y               |  Y            |  Y                    |
|  `pc_list`       |               |                 |                  |               |                       |
|  `pc_code`       |               |                 |                  |               |                       |

Pre-parsing functions convert `pc_text`, `pc_tabs`, `pc_mini` to each other, and validate and import to `pc_list`.


1. `pc_tabs.to_text`
    -  check if tsv, csv, or invalid
    -  if headers
       1. check for column header 'panelcode' or 'pcode' or 'pc'
       2. check for column header 'comment' or '#'
    -  else if no headers
       1. take column 1 only
       2. check if column contains (loosely valid) pcodes
	-  optionally, including other columns in a comment -- escape(?) hash marks and replace tab with `  #` for each column
2. `pc_text.to_tabs`
	-  add a header row
	-  delete blank lines
	-  optionally, add tabs tab (hash#1, hash#2+, or all #s)
3. `.minify`
	-  check if tabbed, if so... strip header and everything after first tab?
	-  strip comments
	-  strip end comments
    -  strip blank lines (incl whitespace)
    -  replace linebreaks with ;
4. `.lineify`
    -  replace ; with linebreaks
5. `.shorthand`
    -  shorten matching patterns to:
	   1. gridcode
	   2. etc.
	   3. etc.
6. `.longhand`
	-  lengthen matching patterns from:
	   1. gridcode
	   2. etc.
	   3. etc.	   
7. `.canonical`
	-  need to think about whether or not this is the same as longhand


#### Parsing and syntax

**Group decorators** are a key sytanx problem for (pre-)parsing. Should I forbid, allow, or require them everywhere, or...?

1. shorthand -- forbid / allow / require decorators?
2. longhand -- forbid / allow / require decorators?
3. canonical -- forbid / allow / require decorators?

Decorators are more work to enter, but make a code easier to read for a human. They give "canonical" strings some nice properties, like sorting and grouping...

`23(r2+1,1)2`
`2_3_(r2+1,1)_2`

`232`
`23()2`
`23(1+r2,1)2`
`23(r2+1,1)2`

`2 3 2`
`2 3() 2`
`2 3(1+r2,1) 2`
`2 3(r2+1,1) 2`

`2_3_2`
`2_3()_2`
`2_3(1+r2,1)_2`
`2_3(r2+1,1)_2`

`2_(1.r2+1,1)_2`

...and they also mean that panelcodes can be "simplified" by dropping their rowgroups through a simple string operation -- so `2_3(1+r2,1)` becomes `2_3` with no parsing and counting the rowgroup contents -- not true of `2_(1+r2,1)` -> `2_3` or `2_(r2+1+1,2)` -> `2_5`, although it may still not be that hard. Those still don't sort with like, and can't be searched as easily.

Finally, decorators create an ambiguity issue with unspaced shorthand. If decorators are optional, then it isn't clear whether the last number before the row is a decorator or a separate row number.

	is it? `23(1+r2,1)2` -> `2_3(1+r2,1)_2`  # 3 rows
	is it? `23(1+r2,1)2` -> `2_3_(1+r2,1)_2` # 4 rows

One solution is to only make unspaced shorthand available for panelcode that contains no rowgroups markers.

	  valid 23 = 2_3
	  valid 23++1 = 2_3++1
	  valid 23++1;2;31,,5 = 2_3++1;2;3_1,,5 
	invalid 23(1+r2,1) -- ambiguous 
	  valid 2_3(1+r2,1) -- 2 rowgroups
	  valid 2_3_(1+r2,1) -- 3 rowgroups

So, the shorthand expansion rule is something like:

-  if string contains 2 digits next to each other
-  and does not contain _
-  and does not contain (
-  replace <digit> <digit> with <digit> <_> <digit>

Parsing functions take a pc_code.

-  `pc_code`: an individual code -- codes may not be compound (;) or include comments (#). entries may not be blank or invalid. a pc list is assumed `clean.` 
   -  `pc_composition`: multiple pages connected with `++` or `,,` ... `1_2++3_3` ... `1++1++1,,2++2++2,,3++3++3` defines a 3x3 grid of pages
      -  `pc_page`: this is the key render level for svg and index generation.
         -  `pc_rowgroup`: this is the key render level for css and html output.


`pc_block` --> `pc_list`

1. strip comments
2. divide ; lines
3. strip 

`pc_list` -->

2. 

>  NOTE: a recent EBNF for CSV -- I'll be using csvwriter, largely, but this could come in useful
>  for best practices on header logic:
>  
>  -  https://www.w3.org/TR/tabular-data-model/#ebnf



### parsing code

Pyparsing example:

    ### pp.delimitedList(, delim="_", combine=True)

    #   rowcode         = Group(OneOrMore(nums) + Optional("b"))
    
    ## EXAMPLES: Getting Started with Pyparsing (p15):
    ## #1:
    ## Word(alphas)+ "(" + Group( Optional(Word(nums)|Word(alphas) + ZeroOrMore("," + Word(nums)|Word (alphas))) ) + ")"
    ## #2:
    ## Word(alphas)+ "(" + Group( Optional(delimitedList(Word(nums)|Word(alphas))) ) + ")"



git commit -m "parser.parseString_pages first draft"

----------IN parser.py: 

```python

def parseString_pages (parseString):
    template = "{0:10}|{1:10}|{2:10}" # print column widths: 8, 10, 15, 7, 10
    print '-----parseString_pages display-----'
    print template.format("", "pagegroup", "page") # header
    for panelcode in parseString:
        print panelcode
        for pagegroup in panelcode:
            print template.format("  pgroup:", str(pagegroup), "")
            for page in pagegroup:
                print template.format("    page:", "", str(page))
    return True

```

Lists of lists (flattening? Stackoverflow?)

```python

def change(lol):
    for index,item in enumerate(lol):
        if isinstance(item, list):
            change(item)
        elif item.startswith('-'):
            lol[index] = ['not',item.split('-')[1]]
    return lol

    logtext = ''

```

### Regular Expressions (regex)

Main uses for regex:

1. Parse matching code (either python `re` or `pyparsing`)
2. Validation code (either python `re` or `pyparsing`)
3. Syntax highlighting
   a.  Textmate (Ruby), Atom, Sublime Text ... etc.
   b.  Prism


-  python regex -- in particular, the `scanner` -- 2015
	-  http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems/
	-  http://www.programcreek.com/python/example/53972/re.Scanner
	-  https://www.reddit.com/r/Python/comments/3edk1g/rescanner_undocumented_class_perfect_for_a/?


#### regex test strings

[panelcode_test_strings](./panelcode-master/test/panelcode_test_strings.txt)


#### regexes for parsing

Expression Testers

Could also try:

-  http://regexr.com/
-  http://www.freeformatter.com/regex-tester.html

At site:

	https://regex101.com/

Was testing:

V1:
```regex
(RTL_)?([0-9]+)?(\([0-9\+\,cr]*\))?(_([0-9]+)?\([0-9\+\,cr]*\))*
modifier: g
```

V2:
```regex
^(((_)?([0-9]+)?(\([0-9\+\,cr]*\))?)?)*
modifier: gm
```


#### regexes for syntax highlighting

Create a syntax highlighting (reggex) file for a specification of Panelcode? using some syntax highlighter, e.g. Pygments or Prism etc. etc. Prism supports reggex language definitions.

-  EXAMPLE-BASED VALIDATION OF DOMAIN-SPECIFIC VISAUL LANGUAGES -- ACM Digital Library 2814256


##### Textmate (Ruby) syntax highlighting "language grammars"

-   [TextMate Syntax Highlighting Howto: A simple todo list](http://metalelf0dev.blogspot.com/2010/05/textmate-syntax-highlighting-howto.html) (2010) -- a very easy beginner example
-   [Writing a TextMate Grammar: Some Lessons Learned](http://www.apeth.com/nonblog/stories/textmatebundle.html) (2014)
-   []() -- advanced, extremely in-depth, with warnings about tons of gotchas for advanced writing. Really gives me pause about trying to do anything complex.

How to get started seems out of date in all documentation:

> "You can create a new language grammar by opening the bundle editor (Window → Show Bundle Editor) and select “New Language” from the add button in the lower left corner."

This is no longer the case. There is a TextMate bundle called "Bundle Development"... but considering I'll have to write my Regex-es in ruby, this whole thing is starting to look like a lot of work for not much payoff.

**Misc:**

-   [TextMate – Introduction to Language Grammars: How to add source code syntax highlighting embedded in HTML](https://developmentality.wordpress.com/2011/02/08/textmate-introduction-to-language-grammars/) (2011) -- detailed, may be out of date
-   [Textmate: Language Grammars](https://manual.macromates.com/en/language_grammars) -- detailed documentation overview, may be out of date
-   [TextMate: Search and replace matching brackets](http://lists.macromates.com/textmate/2007-September/022055.html) (2007) specific code example


##### Atom (node/LESS) syntax highlighting "language grammars"

...I looked into writing one for Atom instead, but it looks like Atom actually uses the TextMate language grammar system whole-cloth!:

-   [Documentation For Atom Grammars?](https://discuss.atom.io/t/documentation-for-atom-grammars/6525/5)
-   ...[Atom : Grammar](http://flight-manual.atom.io/using-atom/sections/grammar/)
-   ...[Atom : Converting from TextMate](http://flight-manual.atom.io/hacking-atom/sections/converting-from-textmate/)
-   **** [Create a custom syntax highlighting with Atom editor](http://blog.gaku.net/create-a-custom-syntax-highlighting-with-atom-editor/)

> "The most minimal grammar I can think of is my language-generic-config package1.1k. But, once again, the grammar does not control the color of the code." https://discuss.atom.io/t/creating-a-custom-grammar-or-language-package/16711/2


```bash
	# 16/06/02 22:28:23 
	
	cd atom-language-panelcode/
	
	# set up python virtualenv using existing tools -- see `2016-05-18 python virtual environments.md`
	source ~/.profile
	cd /Users/jeremydouglass/Dropbox/journals/journal-dropbox-eaglefiler/Files/Panelcode/atom-language-panelcode/
	mkvirtualenv atom-language-panelcode
	workon atom-language-panelcode
	
	# set up git version control
	git init
	git add .
	git commit --allow-empty -m "Initial commit"
	touch package.json
	mate package.json
	git add package.json
	git commit -m "added package.json as per tutorial http://blog.gaku.net/create-a-custom-syntax-highlighting-with-atom-editor/"
	mkdir grammars
	touch grammars/panelcode.cson
	mate grammars/panelcode.cson 
	git add grammars/
	git add grammars/panelcode.cson 
	git commit -m "added grammar as per tutorial"
	git add .
	git commit -m "tweaked package and added test data -- Atom now recognizes the extension, but no highlighting."
	
	# copy package into atom working directory -- do this each time to deploy changes
	ls ~/.atom/packages/
	cp -r /Users/jeremydouglass/Dropbox/journals/journal-dropbox-eaglefiler/Files/Panelcode/atom-language-panelcode/. ~/.atom/packages/atom-language-panelcode/
	# refresh Atom or restart Atom to see it take effect
	
	# copy new package to atom to deploy latest changes
	rm -r ~/.atom/packages/atom-language-panelcode/
	cp -r /Users/jeremydouglass/Dropbox/journals/journal-dropbox-eaglefiler/Files/Panelcode/atom-language-panelcode/. ~/.atom/packages/atom-language-panelcode/
	
	# switch out of python virtualenv
	deactivate
	
	16/06/02 23:08:20 
```

So, I got a filetype working in Atom, but no actual syntax highlighting happening on the screen. A failure for now.

Sublime Text also seems based on Textmate. In theory, doing it for one might work for all of them....? But perhaps thankless work, better to find a partner in crime.


##### Pygments or Prism syntax highlighting

At some point in the future it might be interesting to post an online tool (or provide the language for one or more of the many already existing online tools).

-   http://markup.su/highlighter/

I took a look at Prism, and it is javascript-for-the-web based and seems to emphasize ease of embedding and repurposeing in websites (the script and CSS end, not the langauge development end).

Pygments (Python Syntax Highlighter), on the other hand, is python based and has more substantially developer documentation.

-   http://pygments.org/
-   http://pygments.org/docs/lexerdevelopment/
-   http://stackoverflow.com/questions/14755721/extensive-documentation-on-how-to-write-a-lexer-for-pygments
-   [How to write a Pygments lexer](http://web.archive.org/web/20110504152615/http://www.siafoo.net/article/15)
-   Sphinx documentation is generated with Pygments... http://www.sphinx-doc.org/en/stable/markup/code.html






## ----------

## DEV NOTES

-  [html-tokenize](https://github.com/substack/html-tokenize)
-  [Parse HTML table to Python list?]() 6325216
-  [Layout with Dijit] for Dojo
	-  https://dojotoolkit.org/reference-guide/1.10/dijit/layout.html — see the part that says “Conceptually it looks like this:”
-  [Ask HN: Writing DSL in Python]()
	-  [pydsltool 0.2.0]()
	-  slideshare creating-domain-specific-languages-in-python govindaraj
	-  A DSL in 5 Languages (2010)
	-  https://pyparsing.wikispaces.com/Publications
	-  Charming Python: declarative mini-languages
ASIDE:

-  [Document Layout Analysis]() wikipedia
-  [OCRopus]() wikipedia — and see OCRopy
-  [OCRFeeder]() wikipedia


### Importing and Translating

Someday:

-  HTML tables to Panelcode ...?
	-  [Parsing HTML table to Python list](http://stackoverflow.com/questions/6325216/parse-html-table-to-python-list)-- use lxml
	-  [Simple Python HTML template DSL (improved Python 3 version)](https://gist.github.com/kstep/3516334)
        -   ...web crawling and giving homepages a panelcode, beautiful soup?

-  TEI...?
-  Layout segementation, document analysis... OCR?


## ----------
