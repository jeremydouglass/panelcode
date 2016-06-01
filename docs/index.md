# Panelcode -- tools for comic layout image generation

[0]:             ../../script/output/0.svg
[1_2_3_4_5_6]:   ../../script/output/1_2_3_4_5_6.svg
[1_3_2_4]:       ../../script/output/1_3_2_4.svg
[2]:             ../../script/output/2.svg
[2_2]:           ../../script/output/2_2.svg
[2_2_2_1_1_2_1]: ../../script/output/2_2_2_1_1_2_1.svg
[2_2++3_3]:      ../../script/output/2_2++3_3.svg
[2_3]:           ../../script/output/2_3.svg
[2_3_2]:         ../../script/output/2_3_2.svg
[2_3_2++]:       ../../script/output/2_3_2.svg
[2_3_3(1+r2,1)]: ../../script/output/2_3_3(1+r2,1).svg
[2_3_5]:         ../../script/output/2_3_5.svg
[2_2_5(r2+2,2)]: ../../script/output/2_2_5(r2+2,2).svg
[3(r2+1,1)]:     ../../script/output/3(r2+1,1).svg
[3(1+r2,1)]:     ../../script/output/3(1+r2,1).svg
[3_3]:           ../../script/output/3_3.svg
[3_3_3]:         ../../script/output/3_3_3.svg
[3_3_3_3_3]:     ../../script/output/3_3_3_3_3.svg

[4(r3+1,1,1)]:   ../../script/output/4(r3+1,1,1).svg
[4(1+r3,1,1)]:   ../../script/output/4(1+r3,1,1).svg
[5(1+r2+1,2)]:   ../../script/output/5(1+r2+1,2).svg
[5(r2+1+r2,1)]:  ../../script/output/5(r2+1+r2,1).svg
[5(r2+2,2)]:     ../../script/output/5(r2+2,2).svg
[5(2+r2,2)]:     ../../script/output/5(2+r2,2).svg

[0_(2+0+2)_0]:   ../../script/output/0_(2+0+2)_0.svg
[0_1_(1+0)]:     ../../script/output/0_1_(1+0).svg

[0_2_0]:         ../../script/output/0_2_0.svg
[0_3_0]:         ../../script/output/0_3_0.svg
[3(r2+0,1)]:     ../../script/output/3(r2+0,1).svg

[2_(1,0)]:       ../../script/output/2_(1,0).svg
[2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)]: ../../script/output/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg


## Overview

**Panelcode** is a lightweight layout description language for concisely representing panel-based layouts and design grids using plaing text strings. 

Panelcode strings concisely describe layouts. The format is optimized for rectangular panel regions, arranged in row-based groups. These codes may then be rendered to markup or images -- e.g. html, xml, svg etc.  Here are some examples:

```Panelcode
	2_2            # simple row examples
	1_3_2_4
	1_2_3_4_5_6

	3[*5]          # multiplier shorthand

	3(r2+1,1)      # rowgroups
	2_3_3(1+r2,1)
```	

|                                   | Panelcode       | render              |
|-----------------------------------|-----------------|---------------------|
| simple row examples               | `2_2`           | ![][2_2]            |
|                                   | `1_3_2_4`       | ![][1_3_2_4]        |
|                                   | `1_2_3_4_5_6`   | ![][1_2_3_4_5_6]    |
| multiplier shorthand              | `3[*5]`         | ![][3_3_3_3_3]      |
| complex rowgroups in parentheses  | `3(r2+1,1)`     | ![][3(r2+1,1)]      |
|                                   | `2_3_3(1+r2,1)` | ![][2_3_3(1+r2,1)]  |
|                                   |                 |                     |
| zero pages (blank)                | `0`             | ![][0]              |
| zero panels (absent)              | `0_1_(0+1)`     | ![][0_1_(1+0)]      |
| unmarked pages                    | `(~)`           | ![][(~)]            |
| unmarked rows                     | `2_(~)`         | ![][2_(~)]          |


Panelcode is good at abstract description for comparison. It is focused in particular on layouts in comics strips, pages, and books -- although it could also be used to describe other visual layouts and related document structures. Large collections of comics may be quickly annotated in Panelcode and then searched and analyzed -- e.g. for common and unusual layouts and elements.


#### How it works

|                                              | Panelcode   | render         |
|----------------------------------------------|-------------|----------------|
| Specify a row of columns as a single number. | `2`         | ![][2_2]       |
| Connected rows with underscores.             | `2_3`       | ![][2_3]       |
| Indicate blank regions with 0.               | `0_3_0`     | ![][0_3_0]     |
| Detail complex groups in parentheses.        | `3(r2+1,1)` | ![][3(r2+1,1)] |
| Detail uncoded groups in parentheses with ~. | `3(~)`      | ![][3(~)]      |


#### Design goals ####

For large works, series of works, and corpora to be described quickly in terms of layout.

1. **human-readable** (and writeable) simple layout representations.
2. **concise** for rapid accurate data entry, including many shorthand forms.
3. **searchable** to easily accomodate layout data mining and visualization
4. **comparative**  making it easy to say that two pages have "the same" or "similar" layouts or components -- or to concisely describe how they are different.
5. **canonical forms** -- one unique layout, one Panelcode string -- that can easily be derived from any shorthand forms, making identity comparison trivial. This also makes Panelcode friendly for inclusion in address spaces such as filenames or URL paths.
6. **flexibile** accomodation of different media types -- e.g. comic strips, comic books graphic novels, webcomics and webtoons. This includes basic support for compositing layouts in media-specific ways such as 2pg spreads (comic books) or vertical scrolling stacks (webtoons), as well as for various conversions between encoded and rendered LTR (comics) and RTL (manga) reading order.


#### Uses ####

Panelcode was originally developed specifically for analyzing comics and graphic narrative. It might be of interest for scholars and researchers looking to collect data on layout designs. It also might be of interest as a stock layout generator for storyboarding or templating content creation, or as a pre-processor for layout generation workflows.

-  collect layout data:  
   ...e.g. summarizing the layouts of comics, websites, newspapers etc.
-  search by layout:  
   ...e.g. adding composition-based search to archives of 
-  analyze layouts:  
   ...e.g. "What is the most common blog layout?" "What are the most unusual page layouts in X-Men, or Watchmen?"
-  compute layout differences and transforms:  
   ...e.g. "What page elements appear in 'Scott Pilgrim' that don't appear in O`Malley's later work?"
-  generate layouts:  
   ...e.g. render out to HTML, XML, SVG, TEI CBML etc. -- although see the section below on what **Panelcode is not**.


## Examples


### Rows: `_`

Each number signifies a row: 

|  Panelcode      |  render            |
|-----------------|--------------------|
|  `2_2`          |  ![][2_2]          |  
|  `2_3_5`        |  ![][2_3_5]        |
|  `1_3_2_4`      |  ![][1_3_2_4]      |
|  `1_2_3_4_5_6`  |  ![][1_2_3_4_5_6]  |


### Groups: `()`

Groups specify complex row layouts -- in particular, stacking together panels of different row depths and column heights ('colspans'. These are indicated in groups by 'rowspan' (`r2`, `r3` etc.) and 'colspan' (`c2`,`c3`).

	(1.r2 + 4 + 1.c2.r2, 2.c2)

This can be simplified by ommiting the optional `.` and ommiting the `1` in front of any single panel.

	(r2+4+c2r2,2c2)

Consider this simple group:

|  Panelcode                         |  render                               |
|------------------------------------|---------------------------------------|
|  `3`                               |  ![][3]                               |
|  `3(r2+1,1)`                       |  ![][3(r2+1,1)]                       |

This group reads:

-  `3` there are three panels in this row
-  `(` grouped as follows:
   -  `r2` = `1.r2` 1 panel, stretching 2 rows deep
      -   `+` and
      -   `1` 1 panel
      -   `,` followed on the next row by
   -   `1` a panel
-  `)`

When the row number `3` is expanded by a group `3()` it becomes a "count-hint" -- nice for readability, but optional. With or without the count-hint, `3(r2+1,1)` and `(r2+1,1)` both describe the same layout.

Panelgroups scale panels with row and column spans. Multi-row panels (`r2`, `r3` etc.) take up space in the rows below them, while on those next rows new cells "fill-in" the unoccupied spaces.

Groups and rows may be stacked horizontally (`_`) to form a single layout.

| Panelcode                          |  render                               |
|------------------------------------|---------------------------------------|
|  `2_3_3(1+r2,1)`                   |  ![][2_3_3(1+r2,1)]                   |  
|  `2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)`  |  ![][2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)]  |


### Blanks: `0`

Pages, rows, and individual panels may be blanks -- missing entirely from the layout (with no borders indicated).

The zero-panel marker (`0`) acts as a placeholder to indicate these empty areas in the layout. Panelcode will render an invisible panel' to fill the space indicated.

|  zero codes            |  Panelcode    |  render                         |
|------------------------|---------------|---------------------------------|
|  blank page            |  `0`          |  ![][0]                         |
|  blank rows            |  `0_2_0`      |  ![][0_2_0]                     |
|  blank in group        |  `0_2_0`      |  ![][0_2_0]                     |
|  blank in group        |  `2_(1+0)`    |  ![][2_(1+0)]                   |
|  blank in group        |  `2_(1,0)`    |  ![not quite working][2_(1,0)]  |
|  blank in group        |  `3(r2+0,1)`  |  ![][3(r2+0,1)]                 |


### Uncoded: `~`

Some layouts elements cannot be encoded or rendered in Panelcode. The uncoded marker (`~`) acts as a placeholder for these.

The row separator is used in an empty group to indicate that the group layout is not encoded. This empty group may be prefixed by a panel count -- or not. If not, it may be treated as a 1 panel row.

|  Panelcode   |  Panelcode    |  uncoded markers              |
|--------------|---------------|-------------------------------|
|  `~`         |  ![][(~)]     |  uncoded page                 |
|  `5(~)`      |  ![][5(~)]    |  uncoded page w/count hint    |
|  `3_(~)`     |  ![][3_(~)]   |  uncoded group                |
|  `3_5(~)`    |  ![][3_5(~)]  |  uncoded group  w/count hint  |
|  `3(r2+~,1)` |  ![][3_5(~)]  |  uncoded panel in group       |


## Shorthands

Panelcode supports a variety of shorthand syntaxes to make reading and writing panelcode easier and more expressive.

Shorthands are indicated within `[]`. Each shorthand defines a row or group of rows.

Shorthands are pre-processed and replaced before a panelcode is manipulated or rendered. In general they are expanded into a canonical rowcode form.


**Examples:**

|  shorthand   |  code    |             |                |  rowcode        |  image                |
|--------------|----------|-------------|----------------|-----------------|-----------------------|
|  alpha code  |  `[C]`   |  `[C].a`    |  `[C].alpha`   | `3(r2+1,1)`     |  ![C][3(r2+1,1)]      |
|  span code   |  `[2L]`  |  `[2L].s`   |  `[2L].span`   | `2(c2+1)`       |  ![2L][2(c2+1)]       |
|  vert code   |          |  `[212].v`  |  `[212].vert`  | `5(1+r2+1,2)`   |  ![][5(1+r2+1,2)]     |
|              |          |             |                |                 |                       |
|  multipler   |  `4[*5]` |             |                | `4_4_4_4_4`     |  ![][4_4_4_4_4]       |


**A table of shorthands:**

|  shorthand   |  code    |             |                |  rowcode        |  image                |
|--------------|----------|-------------|----------------|-----------------|-----------------------|
|  quick code  |  `33`    |             |                |  `3_3`          |  ![][3_3]             |
|  quick code  |  `25132` |             |                |  `2_5_1_3_2`    |  ![][2_5_1_3_2]       |
|              |          |             |                |                 |                       |
|  alpha code  |  `[C]`   |  `[C].a`    |  `[C].alpha`   | `3(r2+1,1)`     |  ![C][3(r2+1,1)]      |
|  alpha code  |  `[D]`   |  `[D].a`    |  `[D].alpha`   | `3(1+r2,1)`     |  ![D][3(1+r2,1)]      |
|  alpha code  |  `[E]`   |  `[E].a`    |  `[E].alpha`   | `4(r3+1,1,1)`   |  ![E][4(r3+1,1,1)]    |
|  alpha code  |  `[B]`   |  `[B].a`    |  `[B].alpha`   | `4(1+r3,1,1)`   |  ![B][4(1+r3,1,1)]    |
|  alpha code  |  `[I]`   |  `[I].a`    |  `[I].alpha`   | `5(1+r2+1,2)`   |  ![I][5(1+r2+1,2)]    |
|  alpha code  |  `[O]`   |  `[O].a`    |  `[O].alpha`   | `5(r2+1+r2,1)`  |  ![O][5(r2+1+r2,1)]   |
|              |          |             |                |                 |                       |
|  span code   |  `[2L]`  |  `[2L].s`   |  `[2L].span`   | `2(c2+1)`       |  ![2L][2(c2+1)]       |
|  span code   |  `[2R]`  |  `[2R].s`   |  `[2R].span`   | `2(1+c2)`       |  ![2R][2(1+c2)]       |
|  span code   |  `[3L]`  |  `[3L].s`   |  `[3L].span`   | `3(c2+2)`       |  ![3L][3(c2+2)]       |
|  span code   |  `[3R]`  |  `[3R].s`   |  `[3R].span`   | `3(2+c2)`       |  ![3R][3(2+c2)]       |
|  span code   |  `[3W]`  |  `[3W].s`   |  `[3W].span`   | `3(1+c2+1)`     |  ![3W][3(1+c2+1)]     |
|  span code   |  `[3N]`  |  `[3N].s`   |  `[3N].span`   | `3(c2+1+c2)`    |  ![3N][3(c2+1+c2)]    |
|  span code   |  `[4L]`  |  `[4L].s`   |  `[4L].span`   | `4(c2+3)`       |  ![4L][4(c2+3)]       |
|  span code   |  `[4R]`  |  `[4R].s`   |  `[4R].span`   | `4(3+c2)`       |  ![4R][4(3+c2)]       |
|  span code   |  `[4W]`  |  `[4W].s`   |  `[4W].span`   | `4(1+c2+c2+1)`  |  ![4W][4(1+c2+c2+1)]  |
|  span code   |  `[4N]`  |  `[4N].s`   |  `[4N].span`   | `4(c2+2+c2)`    |  ![4N][4(c2+2+c2)]    |
|  span code   |  `[5L]`  |  `[5L].s`   |  `[5L].span`   | `5(c2+4)`       |  ![5L][5(c2+2)]       |
|  span code   |  `[5R]`  |  `[5R].s`   |  `[5R].span`   | `5(4+c2)`       |  ![5R][5(2+c2)]       |
|  span code   |  `[5W]`  |  `[5W].s`   |  `[5W].span`   | `5(1+c3+1)`     |  ![5W][5(1+c2+1)]     |
|  span code   |  `[5N]`  |  `[5N].s`   |  `[5N].span`   | `5(c2+3+c2)`    |  ![5N][5(c2+1+c2)]    |
|              |          |             |                |                 |                       |
|  verti code  |          |  `[12].v`   |  `[12].verti`  | `3(r2+1,1)`     |  ![][3(r2+1,1)]       |
|  verti code  |          |  `[21].v`   |  `[21].verti`  | `3(1+r2,1)`     |  ![][3(1+r2,1)]       |
|  verti code  |          |  `[13].v`   |  `[13].verti`  | `4(r3+1,1,1)`   |  ![][4(r3+1,1,1)]     |
|  verti code  |          |  `[31].v`   |  `[31].verti`  | `4(1+r3,1,1)`   |  ![][4(1+r3,1,1)]     |
|  verti code  |          |  `[212].v`  |  `[212].verti` | `5(1+r2+1,2)`   |  ![][5(1+r2+1,2)]     |
|  verti code  |          |  `[121].v`  |  `[121].verti` | `5(r2+1+r2,1)`  |  ![][5(r2+1+r2,1)]    |
|  verti code  |          |  `[122].v`  |  `[122].verti` | `5(r2+2,2)`     |  ![][5(r2+2,2)]       |
|  verti code  |          |  `[221].v`  |  `[221].verti` | `5(2+r2,2)`     |  ![][5(2+r2,2)]       |


### Quick code

Quick code syntax describes a layout using only row counts, and with no row separators `_`

```Panelcode
	2_2_2_1_1_2_1  # standard
	2221121        # quick
```

![][2_2_2_1_1_2_1]

Quick syntax will be expanded automatically if the string contains 2 or more digits and nothing else -- no row separators `_`, groups `()`, or shortcodes `[]` etc.

-  Row separators `_` are required for any layout referring to a two-digit number greater than 9.
-  If used, row separators must be used throughout a Panelcode line -- they cannot be mixed.
-  In the case of a single row layout >9, use a group

```Panelcode
	1212     # = 1 + 2 + 1 + 2
	12_12    # = 12 + 12
	1_2_12   # = 1 + 2 + 12
```

```Panelcode
	12112_12   # = 12112 + 12 !!
	           # ...NOT 1 + 2 + 1 + 1 + 2 + 12
```

![][2_2_2_1_1_2_1]
![][3_3_3_3_3]


### Alpha code shorthand

...


### Spancode shorthand

By default panels in a row are equal width. Within a rowgroup, column span markers (e.g. `c2`) can be used to make panels proportionally wider or narrower within their row. However, this can be quite verbose in a way that is harder to read and to write.

Consider a 3-panel row with a wider center panel. "3W" makes encoding and easier.

|            |  spancode  |  rowcode      |  image                |
|------------|------------|---------------|-----------------------|
| a '3-wide' |  `[3W]`    |  `3(1+c2+1)`  |                       |


|  spancode           |  rowcode        |  image                |
|---------------------|-----------------|-----------------------|
|   `2`               |  `2`            |  ![2][2]              |
|  `[2L] | [2Left]`   |  `2(c2+1)`      |  ![2L][2(c2+1)]       |
|  `[2R] | [2Right]`  |  `2(1+c2)`      |  ![2R][2(1+c2)]       |
|   `3`               |  `3`            |  ![3][3]              |
|  `[3L] | [3Left]`   |  `3(c2+2)`      |  ![3L][3(c2+2)]       |
|  `[3R] | [3Right]`  |  `3(2+c2)`      |  ![3R][3(2+c2)]       |
|  `[3W] | [3Wide]`   |  `3(1+c2+1)`    |  ![3W][3(1+c2+1)]     |
|  `[3N] | [3Narrow]` |  `3(c2+1+c2)`   |  ![3N][3(c2+1+c2)]    |
|   `4`               |  `4`            |  ![4][4]              |
|  `[4L] | [4Left]`   |  `4(c2+3)`      |  ![4L][4(c2+3)]       |
|  `[4R] | [4Right]`  |  `4(3+c2)`      |  ![4R][4(3+c2)]       |
|  `[4W] | [4Wide]`   |  `4(1+c2+c2+1)` |  ![4W][4(1+c2+c2+1)]  |
|  `[4N] | [4Narrow]` |  `4(c2+2+c2)`   |  ![4N][4(c2+2+c2)]    |
|   `5`               |  `5`            |  ![5][5]              |
|  `[5L] | [5Left]`   |  `5(c2+4)`      |  ![5L][5(c2+2)]       |
|  `[5R] | [5Right]`  |  `5(4+c2)`      |  ![5R][5(2+c2)]       |
|  `[5W] | [5Wide]`   |  `5(1+c3+1)`    |  ![5W][5(1+c2+1)]     |
|  `[5N] | [5Narrow]` |  `5(c2+3+c2)`   |  ![5N][5(c2+1+c2)]    | 


	2L_2R_2L = (c2+1)_(1+c2)_(c2+1)
	2_2_2


### Verticode shorthand

...


### Multiplier shorthand

The multiplier shorthand `[*3]` expands n repetitions of the previous term or group.

|  grid shorthand    |  expansion                   |  render                       |  note              |
|--------------------|------------------------------|-------------------------------|--------------------|
|  `3[*2]`           |  `3_3`                       |  ![][3_3]                     | repeat simple rows |
|  `3[*5]`           |  `3_3_3_3_3`                 |  ![][3_3_3_3_3]               | "   "              |
|  `[123][*2]`       |  `[123]_[123]`=`1_2_3_1_2_3` |  ![][1_2_3_1_2_3]             | "   "              |
|  `[3C][*2]`        |  `[3C]_[3C]`                 |  `(r2+1,1)_(r2+1,1)`          | repeat shorthand   |
|  `[v212][*2]`      |  `[v212]_[v212]`             |  `(r2+1,1)_(r2+1,1)`          | "   "              |
|  `(r2+r2+1,1)[*2]` |  `(r2+r2+1,1)_(r2+r2+1,1)`   |  ![][(r2+r2+1,1)(r2+r2+1,1)]` | repeat group       |

The multiplier is expanded before all other shorthands are applied.

> **NOTE:** Low multipliers of simple rows does not enhance readability or save space:
> `2[*2]` is not shorter or simpler than `2_2`.


### Shorthand mixing

Shorthand groups can be mixed with each other in the same panelcode string. They can also be combined with multipler syntax -- just like row numbers or groups.

	4_[C][*3]_[2L][*2]_[212].v

-  ... a 4-panel row,
-  and a C-shaped row, x3,
-  and a 2-panel row, wider on the Left, x2,
-  and a row described as vertical stacks of 2-1-2 panels.

This layout expands as follows:

	4_[C][*3]_[2L][*2]_[212].v =
	4_3(r2+1,1)_3(r2+1,1)_3(r2+1,1)_2(c2+1)_2(c2+1)_5(1+r2+1,2)


### Shorthand extensions

Shorthand can accommodate unknown markup. These rows will be marked as 'uncoded' for rendering,
and hinted with a placeholder of the correct rowcount if a count decorator is provided: `5[foo]`.
Tokens will be passed through as classes for styling.

|  shorthand   |  code    |             |                |  rowcode        |  image                |
|--------------|----------|-------------|----------------|-----------------|-----------------------|
|  unknown     |  `[foo]` |  `[foo].b`  |  `[foo].bar`   |   `(~)`         |  ![][(~)]             |
|  unknown     | `5[foo]` | `5[foo].b`  | `5[foo].bar`   |  `5(~)`         |  ![][5(~)]            |

Panelcode shorthands are also extensible.

-  a `.name` to tag -- this will also match on the first letter `.n` if not already used.
-  a regular expression for matching the bracket content. 
   ...if this is unambiguous with other shorthands then the code can be used without an identifier
-  a function which produces rowcode.
   -  this could involve a simple lookup table (as in alpha code) or a generator.















