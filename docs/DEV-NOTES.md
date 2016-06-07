# DEV NOTES -- Panelcode -- Panelkit


## Roadmap

-  v0.1
   -  
   -  
   -  
-  v0.2
   -  
   -  
   -  
-  v0.3
   -  
   -  
   -  
-  v0.4
   -  
   -  
   -  
-  v0.5
   -  
   -  
   -  
-  v0.6
   -  
   -  
   -  
-  v0.7
   -  
   -  
   -  
-  v0.8
   -  
   -  
   -  
-  v0.9
   -  
   -  
   - 



-  unscheduled
   -  import -- string(s)
   -  import -- file
   -  import -- other data types

   -  row nums -- validate
   -  row nums -- parse simple `1_2_3`
   -  row nums -- parse blanks `0_2_0`
   -  row nums -- parse uncoded `0_~_0`

   -  row nums -- render simple `1_2_3`
   -  row nums -- render blanks `0_2_0`
   -  row nums -- render uncoded `0_~_0`

   -  groups -- validate
   -  groups -- parse simple: `(1.r2+1,1)`
   -  groups -- parse blanks `(1.r2+0,1)`
   -  groups -- parse uncoded `(1.r2+~,1)`
   -  groups -- parse hints `3(1.r2+1,1)`

   -  groups -- render simple: `(1.r2+1,1)`
   -  groups -- render blanks `(1.r2+0,1)`
   -  groups -- render uncoded `(1.r2+~,1)`

   -  groups ? -- parse uncoded hints `3(~)`
   -  groups ? -- render uncoded hints `3(~)`

   -  shorthands -- alpha lookup replacement
   -  shorthands -- span lookup replacement (span rendering)
   -  shorthands -- vertical lookup replacement

   -  shorthands -- quick validate
   -  shorthands -- quick parse

   -  shorthands -- alpha validate / parse (?)

   -  shorthands -- span validate
   -  shorthands -- span parse / generate

   -  shorthands -- vertical validate
   -  shorthands -- vertical parse / generate

   -  render -- HTML
   -  render to svg
   -  render to TEI
   -  render to etc. etc.

   -  search -- histogram of code strings
   -  search -- pattern in strings (row num)
   -  search -- pattern in strings (0), (~)
   -  search -- pattern in strings (group)
   -  search -- pattern in strings (group attributes r c i)
   -  search -- pattern in strings (shorthand use) ?
   -  search -- 'expanded' strings?
   -  search -- 'canonical' strings?

   -  search -- 'simplified' strings (`3_3(1+r2,1)` --> `3_3`)
   -  search -- 'sorted' string components (`3(1+r2,1)_1_2` --> `1_2_3(1+r2,1)` --> `1_2_3`)

   -  search -- histogram of layout trees
   -  search -- histogram of components ("structural inventory") e.g. row / groups
   -  search -- pattern in layout trees (row num)
   -  search -- pattern in layout trees (group)
   -  search -- pattern in layout trees (0), (~)

-  someday
   -  shorthands -- multiplier expansion (`3[*5]` --> `3_3_3_3_3` )
   -  insets -- row num insets (`1_1.i`)
   -  insets -- row num multi-insets (`1_1.i3`)
   -  insets -- group insets (`1_3(r2+1.i,1`)
   -  insets -- group multi-insets (`1_3(r2+1.i3,1`)
   -  ? insets -- row num inset groups (`1_1.i(r2+1,1)`)
   -  ? insets -- group inset groups (`1_3(r2+1.i(r2+1,1),1`)
   -  layout compositing ++
   -  layout compositing ,,
   -  serialization and minification ; - ;;
   


Big picture:

1.  panel data collection
	-  choose a standard data store location
	-  choose a format
		-  save in CSV / TSV files in a standard format
	-  choose an extension (e.g. .panels.csv
	-  recovery of past panel data
		-  check ...?
2. development of tools
	-  document driven, then test driven
	-  the data can be:
		-  transformed -- short, long, and mixed forms of markup to support data entry, different kinds of encoding projects (e.g. comic, manga, webcomic (strip, paged, korean etc.)) and comparisons (complex vs. simple vs. counts, with transforms) 
		-  rendered -- a data stream can be output as a list of layout images, possiblye paired with originals. lists can then be passed to HTML templates for display.
		-  searched, summarized, queried, and analyzed (e.g. regex, imported into trees and then queried, a la XPATH)
		-  data visualized...?



## CODE NOTES

### Python -- in general

-   Learning Python
	-  http://blamcast.net/python/ex1.html
	-  http://pixelmonkey.org/pub/python-training/
	-  https://docs.python.org/3/faq/programming.html
	-  http://sthurlow.com/python/
	-  http://www.amazon.com/Python-Visual-QuickStart-Guide-3rd/dp/0321929551


#### python virtualenv notes

1. `source ./~profile`
2. from anywhere: `workon panelcode`
3. ...work...
4. `deactivate`

see `2016-05-18 python virtual environments.md` for details


#### Panel layout data structures

-   Tuples, Lists, Dictionaries
	-  [Tuples, Lists, and Dictionaries](http://sthurlow.com/python/lesson06/)
	-  [Lists and tuples](http://introtopython.org/lists_tuples.html)
	-  [Understanding tuples vs. lists in Python](http://news.e-scribe.com/397)
	-  [List comprehensions](http://www.secnetix.de/olli/Python/list_comprehensions.hawk) -- could something like that work for panel definitions? Maybe any potential economy of expression doesn't make sense until you have more than 4 rows. See multipler syntax.
	-  http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
	-  http://sthurlow.com/python/lesson06/
-   
	-  https://pythonproject.wordpress.com/tag/think-python/
	-  ... could use (imutable) tuple representation of panel structure as dictionary key hashable, for canonical lookup? See [Create a dictionary in python which is indexed by lists](http://stackoverflow.com/questions/2671211/create-a-dictionary-in-python-which-is-indexed-by-lists) So the tuple representation of `3_3_3` would be:
	
			dict = {  ((1,1,1),(1,1,1),(1,1,1)) : 'value'  } # key is tuple of tuples
			dict = {   repr([[1,1,1],[1,1,1],[1,1,1]]) : 'value'  } key is string of list of lists
-   Generators
	-  [Generator Tricks For Systems Programmers](http://www.dabeaz.com/generators/Generators.pdf)

Flattening:

-  http://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python
-  http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python

#### Testing -- with Python unittest


Manually running basic test suite after each set of changes

```bash
	git status
	git log
	python -m tests.test_manual
```


Later, using test_basic and writing log files for inspection:


```bash
	# save 1st testing output log
	python -m tests.test_basic > templog1
	
	# make a change that shouldn't change anything
	# save 2nd testing output log
	 python -m tests.test_basic > templog2
	
	# check if the logs are identical
	md5 templog1 templog2
		MD5 (templog1) = 72198e7d3a1bbd5a9169ee715670ea93
		MD5 (templog2) = d91524a70648e39dab78f7602fe4810a
	
	# check how they are different
	diff templog1 templog2
	
	# interactive diff -- launches FileMerge
	opendiff templog1 templog2
```

Early command line function testing:


From [panelcode-master](/Users/jeremydouglass/Dropbox/journals/journal-dropbox-eaglefiler/Files/Panelcode/panelcode-master):

```python
	> python
	
	>>> import panelcode
	>>> panelcode.pstr_to_html('3_3_3')
	>>> panelcode.pstr_to_svg('3_3_3')
	>>> panelcode.text_to_file('test.svg', panelcode.pstr_to_svg('3_3_3'))
```


### git -- version control notes

```bash
	cd ~/Dropbox/journals/journal-dropbox-eaglefiler/Files/Panelcode/panelcode-master
	
	#### set up new repo and commit
	git init
	
	get add .
	git commit -m "First commit"
	
	##### view status
	git status
	git log
	git branch -av
	
	#### make changes and commit
	
	git add .
	git commit -m "fixed 2 bugs in pstr_to_html -- extra row from test string and rowcount not pstr_rowcount called with wrong argument" 
	
	#### asked to config author
	
	git config --global user.name "Jeremy Douglass"
	git config --global user.email jeremydouglass@gmail.com
	git commit --amend --reset-author
	
	#### unhappy with .DS_Store files 
	
	git config --global core.excludesfile ~/.gitignore_global
	mate ~/.gitignore_global
	
	git rm -r -n --cached *.DS_Store
	git rm -r --cached *.DS_Store
	git add .
	git commit -m "updated .gitignore to exclude .DS_Store"
	
	#### unhappy that I messed up author on several commits, learned to use rebase to step through and fix them one at a time.
	#### as per http://stackoverflow.com/questions/3042437/change-commit-author-at-one-specific-commit
	
	git rebase -i 735d8f3f0b322cb65c35b4a70e2634d6a60b8978
	# mark each commit as 'edit'
	git commit --amend --author="Jeremy Douglass <jeremydouglass@gmail.com>"
	git rebase --continue
	git commit --amend --author="Jeremy Douglass <jeremydouglass@gmail.com>"
	git rebase --continue
	git commit --amend --author="Jeremy Douglass <jeremydouglass@gmail.com>"
	git rebase --continue
```


#### git commits -- a series of git commits

Making changes to core.py:

```bash
	git status
	git add panelcode/core.py
	git commit -m "fixed rowcount bug in pstr_rowcount, renamed input to pstr in pstr_to_html, added func descriptions throughout"

	git add panelcode/core.py
	git commit -m "added section comments: Analyzers, Renderers, File Output"

	git status
	git add panelcode/core.py
	git commit -m "added Cleaners and Shorthands sections and initial functions"

	git add panelcode/core.py
	git commit -m "wrote app_batch_svg with use of cleaners / shorthand functions to past tests/test_manual.py"

	git add panelcode/core.py
	git commit -m "move pstr_to_svg code block to Renderers section"
```


#### git diffs -- using git visual diff inspection on OS X

To use FileMerge on OSX, use git difftool -- no config needed on Reason3 laptop!

Checking out what changes I made before adding and commiting using the visual FileMerge, auto-selected and launched from difftool helper:

```bash
	git difftool
```


#### git revert one file


I changed .gitignore, but decided I wanted the old version. How to reset just that file? Find the appropriate git number with log, then restore the old version (overwriting any recent changes in the working directory) as per http://stackoverflow.com/questions/215718/reset-or-revert-a-specific-file-to-a-specific-revision-using-git

	git log -p -M --follow --stat -- .gitignore
	git checkout 70eb717c752121693cc0a5957ab632c45b95144a .gitignore 
	git status

I didn't find the output of `git blame .gitignore` very useful.

Note also that, in addition to diffing a specific file to the previous version -- after identifying commit numbers with status / log / blame, you can diff all changes from two specific commits like this (order matters, old-new is normal):

	git diff .gitignore
	git diff 70eb717c 34991e0e



# ----------


# MISC


## What started it all

~2016-05-15

> I want to create a generic image from each panel sequence. I've decided to use cut rows and columns as per the HTML `td` and `tr` colspan and rowspan method -- it is very quick to do data entry.

Initially I was writing the data like this:

```
Data from: https://www.comic-rocket.com/explore/grrl-power/

9	3;4;2			# http://grrlpowercomic.com/archives/57
9	3;4(1r3+1,1,1);2	# http://grrlpowercomic.com/archives/57
7	3;2;2			# http://grrlpowercomic.com/archives/159
7	3(1r2+1,1);2;2		# http://grrlpowercomic.com/archives/159
```
