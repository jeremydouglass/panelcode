## Syntax


### Rows: `_`

Each number signifies a row: 

|  Panelcode      |  render            |
|-----------------|--------------------|
|  `2_2`          |  ![][2_2]          |  
|  `2_3_5`        |  ![][2_3_5]        |
|  `1_3_2_4`      |  ![][1_3_2_4]      |
|  `1_2_3_4_5_6`  |  ![][1_2_3_4_5_6]  |


### Groups: `( )`

#### group intro A

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

#### group intro B

Sometimes panels span multiple rows, or panel columns overlap in meaningful ways. A `group` expands a count from one row into a multi-row block with detailed layout information. A group layout is defined in parentheses: `(r2+1,1)`. It may be proceeded by an optional number -- called a count hint -- indicating the number of panels in the group: `3(r2+1,1)`.

Example groups:

	3(r2+1,1)
	4(r2+1+r2,1)
	4(1+r2+1,2)

'+' indicates panels on the same group row, while ',' indicates a new group row.

	r (rowspan, or # of rows high)
	c (colspan, or # of cols wide)

The suffix 'r' indicates a group-row height:

	2   = 2 panels
	3   = 3 panels
	 r2 = 1 panel,  2 rows high
	 r3 = 1 panel,  3 rows high
	2r3 = 2 panels, 3 rows high each

So in the group:

	7(r3+2r2+1,1,2)

...notice that the subsequent group rows "fill in" the gaps left by the panels above. This is exactly how HTML tables work.

Within the group parentheses 'c' indicates a column.

 	 c2 = 1 panel,  2 columns wide
 	 c3 = 1 panel,  3 columns wide
	2c3 = 2 panels, 3 columns wide each

When appearing bare, modifiers refer to a single panel. 'r3' = '1r3'. When preceded by a count, modifiers apply to each panel in the count:

	(3r2+1,1) = (r2+r2+r2+1,1)

Both rowspan and colspan can be defined in a group, and then can be combined.

	(r3+2r2+1,1,c2)

	(1+r2c2+1,r2+r2,c2)

	(2r2c2,1,r2,4)

Groups are assembled together into a layout using '_' -- just like row counts:

	row counts layout: 3_3_4
	row groups layout: 3(r2+1,1)_4(r2+1+r2,1)_4(1+r2+1,2)

A single layout will often mix simple counts and complex groups:

	3_3_4(1+r2+1,2)

Empty groups are equivalent to a simple row number:

	3_3_4() = 3_3_4(4) = 3_3_4

	Note: You can use empty groups as placeholders for more detailed layout data collection.
	Simply

Groups can be "bare", without a preceding number (e.g. for convenient fast data entry):

	(1+r2+1,2) = 4(1+r2+1,2)

Note: row groups can be invalid due to a mismatch between the initial count

 number/group mismatch:

	group numbers 
	3(r2+1+r2,1) -- number is 3, group details 4

Note: sometimes a layout contains now horizontal divisions at all, and must be specified by a single group. For example, this 4x4 layout can only be defined in a continuous group:

	12(r2+3,r2+2,1+r2+1,3)

By extension, any "normal" layout could be defined as a single group. For example, this 3x3 layout:
	
	3x3
	= 3_3_3
	= 9(3,3,3)
	= 9(1+1+1,1+1+1,1+1+1)

#### Groups that reduce to simple rows

Groups `( )` which contain only simple rows are reduced to simple rows.

|  zero codes                      |  original     |  Panelcode |  render        |
|----------------------------------|---------------|------------|----------------|
|  group with simple row           |  `1_(2)`      |  `1_2`     |  ![][1_2]      |
|  groups with simple rows         |  `(1)_(2)`    |  `1_2`     |  ![][1_2]      |
|  empty groups with hints         |  `1()_2()`    |  `1_2`     |  ![][1_2]      |
|  empty groups                    |  `()_()`      |  invalid   |                |
|  group with simple rows          |  `1_(2,3)`    |  `1_2_3`   |  ![][1_2_3]    |
|  group with simple rows (blank)  |  `1_(2,0)`    |  `1_2_0`   |  ![][1_2_0]    |
|  group with simple rows (uncod)  |  `1_(2,~)`    |  `1_2_~`   |  ![][1_2_~]    |
|  group with missing row          |  `1_(2,)`     |  invalid   |                |
|  group with missing rows         |  `1_(,)`      |  invalid   |                |
|  group with missing rows         |  `1_(,)`      |  invalid   |                |


### Blanks: `0`

Blanks indicate blank areas in a layout.

Whole pages, rows, or individual panels may be blank -- not empty panels, but missing entirely from the layout (with no panel borders indicated).

The zero marker (`0`) acts as a placeholder to indicate these empty areas in the layout -- 'zero-panels', 'zero-row', or 'zero-pages'. Panelcode renderers will place an invisible panel' to fill the space indicated.

|                        |  Panelcode    |  render                         |
|------------------------|---------------|---------------------------------|
|  blank page            |  `0`          |  ![][0]                         |
|  blank rows            |  `0_2_0`      |  ![][0_2_0]                     |
|  blank in group        |  `2_(1+0)`    |  ![][2_(1+0)]                   |
|  blank in group        |  `3(r2+0,1)`  |  ![][3(r2+0,1)]                 |


#### Blank rendering

Internally, the 0 panel is represented as 1.blank -- a single panel with special rendering features which will not be included in panel counts.

-  `0_2_0` = `1.blank_2_1.blank`
-  `3(r2+0,1)` = `3(r2+1.blank,1)`


#### No blanks as a group hint

`0` is not a meaningful group hint.

	0(r2+1,1) What should a 0 hint do? Allowable? Meaningful? Maybe there are reasons people would want to do it to hack things in and out of analysis...?
	0(~) ...would this be meaningful? Blank space, but also uncodeable at the same time?
	0()  ...

	~(r2+1,1)  What should an uncoded hint do? Meaningful? Parse error?
	~(0) What should this do?
	~()  ...


#### Blanks vs. ommitting group panels

Rather than ommiting a panel at the end of a group row, specify a blank.

Ommitting a panel may generate a similar  visual output under certain circumstances, however it may also change the markup in unpredictable ways, and makes it difficult to search, render, and validate a panelcode. Instead, specify the blank.

|  zero codes                         |  Panelcode    |  render                      |
|-------------------------------------|---------------|------------------------------|
|  missing panel in rowgroup (wrong)  |  `3(r2,1)`    |  ![][3(r2,1)]                |
|    blank panel in rowgroup (right)  |  `3(r2+0,1)`  |  ![][3(r2+0,1)]              |


### Uncoded: `~`

Some layouts elements cannot be encoded or rendered in Panelcode. The uncoded marker (`~`) acts as a placeholder for these. Panelcode renderers will place a specially marked or styled 'panel' to fill the space indicated.

The row separator is used in an empty group to indicate that the group layout is not encoded.

|  Panelcode   |  Panelcode      |  uncoded markers               |
|--------------|-----------------|--------------------------------|
|  `~`         |  ![][(~)]       |  uncoded page                  |
|  `3_(~)`     |  ![][3_(~)]     |  uncoded group                 |
|  `(r2+~,1)` |  ![][3(r2+~,1)]  |  uncoded panel in group        |

Uncoded pages and groups `(~)` may optionally be prefixed by a panel count: `3(~)`.

|  Panelcode   |  Panelcode      |  uncoded markers               |
|--------------|-----------------|--------------------------------|
|  `5(~)`      |  ![][5(~)]      |  uncoded page w/count hint     |
|  `3_5(~)`    |  ![][3_5(~)]    |  uncoded group w/count hint    |
|  `3(r2+~,1)` |  ![][3(r2+~,1)] |  uncoded panel in group w/hint |

If a count is included, renderers may use a row of specially marked panels as a layout placeholder, rather than a single marked panel.


#### Uncoded rendering


Internally, the `~` panel is represented as `1.uncoded` -- a single panel with special rendering features. For the purposes of panel counts an uncoded panel counts as '1' unless it is part of a hinted group.

-  `~_2_~` = `1.buncoded_2_1.uncoded`
-  `3(r2+~,1)` = `3(r2+1.uncoded,1)`


### Shorthands: `[ ]`

Panelcode supports a variety of shorthand syntaxes to make reading and writing panelcode easier and more expressive.

Shorthands are indicated within `[ ]`. Each shorthand defines a row or group of rows.

Shorthands are pre-processed and replaced before a panelcode is manipulated or rendered. In general they are expanded into a canonical rowcode form.


**Examples:**

|  shorthand   |  code    |             |                |  rowcode        |  render               |
|--------------|----------|-------------|----------------|-----------------|-----------------------|
|  alpha code  |  `[C]`   |  `[C].a`    |  `[C].alpha`   | `3(r2+1,1)`     |  ![C][3(r2+1,1)]      |
|  span code   |  `[2L]`  |  `[2L].s`   |  `[2L].span`   | `2(c2+1)`       |  ![2L][2(c2+1)]       |
|  vert code   |          |  `[212].v`  |  `[212].vert`  | `5(1+r2+1,2)`   |  ![][5(1+r2+1,2)]     |
|              |          |             |                |                 |                       |
|  multipler   |  `4[*5]` |             |                | `4_4_4_4_4`     |  ![][4_4_4_4_4]       |


**A table of shorthands:**

|  shorthand  |  short   |  full          |  rowcode        |  render               |
|-------------|----------|----------------|-----------------|-----------------------|
|  quick      |  `33`    |  `[33].quick`  |  `3_3`          |  ![][3_3]             |
|  quick      |  `25132` |  `[25132].quick` |  `2_5_1_3_2`  |  ![][2_5_1_3_2]       |
|             |          |                |                 |                       |
|  alpha      |  `[C]`   |  `[C].alpha`   | `3(r2+1,1)`     |  ![C][3(r2+1,1)]      |
|  alpha      |  `[D]`   |  `[D].alpha`   | `3(1+r2,1)`     |  ![D][3(1+r2,1)]      |
|  alpha      |  `[E]`   |  `[E].alpha`   | `4(r3+1,1,1)`   |  ![E][4(r3+1,1,1)]    |
|  alpha      |  `[B]`   |  `[B].alpha`   | `4(1+r3,1,1)`   |  ![B][4(1+r3,1,1)]    |
|  alpha      |  `[I]`   |  `[I].alpha`   | `5(1+r2+1,2)`   |  ![I][5(1+r2+1,2)]    |
|  alpha      |  `[O]`   |  `[O].alpha`   | `5(r2+1+r2,1)`  |  ![O][5(r2+1+r2,1)]   |
|             |          |                |                 |                       |
|  span       |  `[2L]`  |  `[2L].span`   | `2(c2+1)`       |  ![2L][2(c2+1)]       |
|  span       |  `[2R]`  |  `[2R].span`   | `2(1+c2)`       |  ![2R][2(1+c2)]       |
|  span       |  `[3L]`  |  `[3L].span`   | `3(c2+2)`       |  ![3L][3(c2+2)]       |
|  span       |  `[3R]`  |  `[3R].span`   | `3(2+c2)`       |  ![3R][3(2+c2)]       |
|  span       |  `[3W]`  |  `[3W].span`   | `3(1+c2+1)`     |  ![3W][3(1+c2+1)]     |
|  span       |  `[3N]`  |  `[3N].span`   | `3(c2+1+c2)`    |  ![3N][3(c2+1+c2)]    |
|  span       |  `[4L]`  |  `[4L].span`   | `4(c2+3)`       |  ![4L][4(c2+3)]       |
|  span       |  `[4R]`  |  `[4R].span`   | `4(3+c2)`       |  ![4R][4(3+c2)]       |
|  span       |  `[4W]`  |  `[4W].span`   | `4(1+c2+c2+1)`  |  ![4W][4(1+c2+c2+1)]  |
|  span       |  `[4N]`  |  `[4N].span`   | `4(c2+2+c2)`    |  ![4N][4(c2+2+c2)]    |
|  span       |  `[5L]`  |  `[5L].span`   | `5(c2+4)`       |  ![5L][5(c2+2)]       |
|  span       |  `[5R]`  |  `[5R].span`   | `5(4+c2)`       |  ![5R][5(2+c2)]       |
|  span       |  `[5W]`  |  `[5W].span`   | `5(1+c3+1)`     |  ![5W][5(1+c2+1)]     |
|  span       |  `[5N]`  |  `[5N].span`   | `5(c2+3+c2)`    |  ![5N][5(c2+1+c2)]    |
|             |          |                |                 |                       |
|  vertical   | `[12V]`  |  `[12].vert`   | `3(r2+1,1)`     |  ![][3(r2+1,1)]       |
|  vertical   | `[21V]`  |  `[21].vert`   | `3(1+r2,1)`     |  ![][3(1+r2,1)]       |
|  vertical   | `[13V]`  |  `[13].vert`   | `4(r3+1,1,1)`   |  ![][4(r3+1,1,1)]     |
|  vertical   | `[31V]`  |  `[31].vert`   | `4(1+r3,1,1)`   |  ![][4(1+r3,1,1)]     |
|  vertical   | `[212V]` |  `[212].vert`  | `5(1+r2+1,2)`   |  ![][5(1+r2+1,2)]     |
|  vertical   | `[121V]` |  `[121].vert`  | `5(r2+1+r2,1)`  |  ![][5(r2+1+r2,1)]    |
|  vertical   | `[122V]` |  `[122].vert`  | `5(r2+2,2)`     |  ![][5(r2+2,2)]       |
|  vertical   | `[221V]` |  `[221].vert`  | `5(2+r2,2)`     |  ![][5(2+r2,2)]       |


#### Quick shorthand: `333`

Quick shorthand syntax describes a layout using only row counts, and with no row separators (`_`). A quick panelcode is a string of 2 or more digits

```Panelcode
	333            # quick 3_3_3
	2221121        # quick 2_2_2_1_1_2_1
```

![][2_2_2_1_1_2_1]

Quick syntax will be expanded automatically if the string contains 2 or more digits and nothing else -- no row separators `_`, groups `( )`, or shortcodes `[ ]` etc.

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



#### Alpha shorthand: `[C]`, `[D]`, ... 

Some small groups are extremely common, occuring over and over again.

Some of the most common rowgroups in comics are various configurations including one or more double-height rows, e.g. `3(r2+1,1)`:

![C][3(r2+1,1)]

Alpha shorthand 


	3A = 
	3C = 
	3D = 
	3U = 
	4H = 
	4I = 

	3C_4H_4I --> 3(r2+1,1)_4(r2+1+r2,1)_4(1+r2+1,2)


#### Span shorthand: `[2L]`, `[3W]`,  ...

By default panels in a row are equal width. Within a rowgroup, column span markers (e.g. `c2`) can be used to make panels proportionally wider or narrower within their row. However, this can be quite verbose in a way that is harder to read and to write.

Consider a 3-panel row with a wider center panel. "3W" makes encoding and easier.

|            |  spancode  |  rowcode      |  render               |
|------------|------------|---------------|-----------------------|
| a '3-wide' |  `[3W]`    |  `3(1+c2+1)`  |                       |


|  spancode           |  rowcode        |  render               |
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


#### Vertical shorthand: `[121V]`

While alpha shorthand describes some common small groups with row-spanning panels, vertical shorthand is a more general description of any group with only rowspans (and no column spans). The (r2+1,1) `[C]` pattern is written [12V] in vertical shorthand -- 1 panel in the first column, and two in the second column. `[E]` is written [13V]. Vertical shorthand can also describe many groups that have no alpha codes -- such as [112V], [1112V], and [11112V].

A group that mixes panels of 2, 3, 4, and 5+ rowspans can be extremely verbose and complex to encode in rowcode. For example, a rowgroup with a column of 5 panels next to a column of 3 is extremely hard to work out and then manually encode in rowcode:

|----------|--------------------------------------|
|  rowcode | `(r3+r5,,,r5,,r3,r5,,,r5,r3,,r5,,,)` |
| vertical | `[53V]`                              |



#### Multiplier shorthand: `[*3]`

The multiplier shorthand (`[*3]`) expands n repetitions of the previous term or group.

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


> **DEV NOTE:** Multiplier shorthand was originally called grid shorthand or "grid code", because a multiplier * a rownum would produce a grid, e.g. 3*5 = 3x5 grid. However, the main use of the multiplier is actually in duplicating complex rowgroups -- which do not in fact produce grids.


#### Mixing shorthands

Shorthands may offer different ways of encoding the same row group, however these expand to the same rowcode. For example, these alpha and vertical shorthands encode the same layout -- and expand the same way.

|  render               |  alpha  |  vertical  |  rowcode        |
|-----------------------|---------|------------|-----------------|
|  ![3C][3(r2+1,1)]     |  [C]    |   [12V]    |  `3(r2+1,1)`    |
|  ![3D][3(1+r2,1)]     |  [D]    |   [21V]    |  `3(1+r2,1)`    |
|  ![4E][4(r3+1,1,1)]   |  [E]    |   [13V]    |  `4(r3+1,1,1)`  |
|  ![4D][4(1+r3,1,1)]   |  [B]    |   [31V]    |  `4(1+r3,1,1)`  |
|  ![5I][5(1+r2+1,2)]   |  [I]    |  [212V]    |  `5(1+r2+1,2)`  |
|  ![5H][5(r2+1+r2,1)]  |  [O]    |  [121V]    |  `5(r2+1+r2,1)` |

Different shorthands may be mixed in different layout strings in a panelcode data file. Shorthand groups can be mixed with each other in the same panelcode string.

1. `[C]_[C]`    
2. `[12V]_[12V]`
3. `[C]_[12V]`
4. `[12V]_[C]`
5. `[12].verical_[C].alpha`

...will all expand to the same rowcode layout:

`3(r2+1,1)_3(r2+1,1)`

However, each shorthand processor is separate, and different shorthand codes cannot be mixed together into new codes. Invalid constructs like `[B12V]` or `[CC4L]` will not be recognized.

Shorthand groups can also be combined with multipler syntax -- just like row numbers or groups.

`4_[C][*3]_[2L][*2]_[212].v`

-  ... a 4-panel row,
-  and a C-shaped row, x3,
-  and a 2-panel row, wider on the Left, x2,
-  and a row described as vertical stacks of 2-1-2 panels.

This layout expands as follows:

	4_[C][*3]_[2L][*2]_[212].v =
	4_3(r2+1,1)_3(r2+1,1)_3(r2+1,1)_2(c2+1)_2(c2+1)_5(1+r2+1,2)


#### Extending shorthands

Shorthand can accommodate unknown markup. These rows will be marked as 'uncoded' for rendering,
and hinted with a placeholder of the correct rowcount if a count decorator is provided: `5[foo]`.
Tokens will be passed through as classes for styling.

|  shorthand   |  code    |             |                |  Panelcode      |  render               |
|--------------|----------|-------------|----------------|-----------------|-----------------------|
|  unknown     |  `[foo]` |  `[foo].b`  |  `[foo].bar`   |   `(~)`         |  ![][(~)]             |
|  unknown     | `6[foo]` | `6[foo].b`  | `6[foo].bar`   |  `6(~)`         |  ![][6(~)]            |
|  unknown     | `6[baz]` | `6[baz].b`  | `6[baz].bar`   |  `6(~)`         |  ![][6(~)]            |

Panelcode shorthands are also extensible.

-  a `.name` to tag -- this will also match on the first letter `.n` if not already used.
-  a regular expression for matching the bracket content. 
    ...if this is unambiguous with other shorthands then the code can be used without an identifier
-  a function which produces rowcode.
    -  this could involve a simple lookup table (as in alpha code) or a generator.

So, for example, imagine an encoder and renderer that represents a 'pizza' group, which can be divided into radial slices, beginning at 180 and proceeding counter-clockwise. Slices may be equal or their arcs may be weighted differently according to the arc property `.a`:

`5[3+1.a2+1].pizza`

...specifies three equal slices across the top half of the pizza, followed by a double-slice and a single slice, all read counter-clockwise in a circle. Howeer, without the pizza encoder or renderer, panelcode designates the group `5(~)` and renders -- as a placeholder -- 5 marked panels as an approximation.


### Canonicals

Panelcode's goal is to be writeable and readable through accomodating a variety of shorthands.
However, for the purposes of comparison, search, and resource management (e.g. image generation or URL caching) it is ideal for one layout to have one and only one 'canonical' panelcode representation.

Some advantages of resolving Panelcode to canonical form include:

-   easy readability
-   easy search and pattern matching
-   better caching

#### equivalence of different short forms


Consider the many ways in which one can indicate a 3x3, 9-panel grid in Panelcode. All of these reduce to the canonical representation `3_3_3`
 
|  shorthand   |  string         |  fully expanded             |  Panelcode   |  render      |
|--------------|-----------------|-----------------------------|--------------|--------------|
|              |  `3_3_3`        |  `(1+1+1)_(1+1+1)_(1+1+1)`  |  `3_3_3`     |  ![][3_3_3]  |
|  groups      |  `(3)_(3)_(3)`  |  `(1+1+1)_(1+1+1)_(1+1+1)`  |  `3_3_3`     |  ![][3_3_3]  |
|  hints       |  `3()_3()_3()`  |  `(1+1+1)_(1+1+1)_(1+1+1)`  |  `3_3_3`     |  ![][3_3_3]  |
|  multiplier  |  `3[*3]`        |  `(1+1+1)_(1+1+1)_(1+1+1)`  |  `3_3_3`     |  ![][3_3_3]  |
|  vertical    |  `3_[222].v`    |  `(1+1+1)_(1+1+1)_(1+1+1)`  |  `3_3_3`     |  ![][3_3_3]  |


#### full expansion, then ordered compression

-  Shorthands are always expanded
-  Expanded shorthands are always compressed if possible
-  Contiguous simple row nums are merged (if they have no different properties):
   -   `1+1,1+1` --> `2,2`
   -   `1+1+1+1r2,2+1` -> `3+1r2,3`
   -   `r2+r2+1+1,1+1` = `2r2+2,2`
   -   always!
-  Groups of simple row nums are ungrouped (if they have no different properties):
   -  `(2,2)_2` --> `2_2_2`
   -   always!
-  Properties such as `.c`, `.r`, `.i`, `.blank`, `.uncoded`, `.{userdefined}`
   -   are always alphabetized, e.g.
   -   `(~r2c2+1,1)` --> `(1.c2.r2.uncoded + 1, 1)`
      -  + sorting, serach
      -  ! ...?
-  Group hints always...
   -  ...present
      -  + readability, simplify `3(etc.)_3(etc.)` to `3_3` with regex
      -  ! validation -- can get out of sync
      -  ! required complex logic to generate them for program and/or reader
   -  ...absent ?
      -  + 
      -  ! 
-  For the top level page, `( )` is always...
   -  ...absent
      -  + 
      -  ! 
   -  ...present ?
      -  + 
      -  ! 

rows+groups canonical

`3(r2+1,1)_4(r2+1+r2,1)_4(1+r2+1,2)`

'mixed' --> full
`4(1+r2+1,1+1) --> 4(1+r2+1,2)`

'mixed' --> short
`4(1+r2+1,1+1) --> 4`

shorthand --> full

`3C_4H_4I --> 3(r2+1,1)_4(r2+1+r2,1)_4(1+r2+1,2)`

``(3)_(3)_(3) --> 3_3_3``

`3(r2+1,1)`

canonical_form()
