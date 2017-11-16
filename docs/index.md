# Panelcode -- tools for panel-based layouts

[0]:             ../../panelcode-data/script2/output/0.svg
[1_2_3_4_5_6]:   ../../panelcode-data/script2/output/1_2_3_4_5_6.svg
[1_3_2_4]:       ../../panelcode-data/script2/output/1_3_2_4.svg
[2]:             ../../panelcode-data/script2/output/2.svg
[2_2]:           ../../panelcode-data/script2/output/2_2.svg
[2_2_2_1_1_2_1]: ../../panelcode-data/script2/output/2_2_2_1_1_2_1.svg
[2_2++3_3]:      ../../panelcode-data/script2/output/2_2++3_3.svg
[2_3]:           ../../panelcode-data/script2/output/2_3.svg
[2_3_2]:         ../../panelcode-data/script2/output/2_3_2.svg
[2_3_2++]:       ../../panelcode-data/script2/output/2_3_2.svg
[2_3_3(1+r2,1)]: ../../panelcode-data/script2/output/2_3_3(1+r2,1).svg
[2_3_5]:         ../../panelcode-data/script2/output/2_3_5.svg
[2_2_5(r2+2,2)]: ../../panelcode-data/script2/output/2_2_5(r2+2,2).svg
[3(r2+1,1)]:     ../../panelcode-data/script2/output/3(r2+1,1).svg
[3(1+r2,1)]:     ../../panelcode-data/script2/output/3(1+r2,1).svg
[3]:             ../../panelcode-data/script2/output/3.svg
[3_3]:           ../../panelcode-data/script2/output/3_3.svg
[3_3_3]:         ../../panelcode-data/script2/output/3_3_3.svg
[3_3_3_3_3]:     ../../panelcode-data/script2/output/3_3_3_3_3.svg

[4(r3+1,1,1)]:   ../../panelcode-data/script2/output/4(r3+1,1,1).svg
[4(1+r3,1,1)]:   ../../panelcode-data/script2/output/4(1+r3,1,1).svg
[5(1+r2+1,2)]:   ../../panelcode-data/script2/output/5(1+r2+1,2).svg
[5(r2+1+r2,1)]:  ../../panelcode-data/script2/output/5(r2+1+r2,1).svg
[5(r2+2,2)]:     ../../panelcode-data/script2/output/5(r2+2,2).svg
[5(2+r2,2)]:     ../../panelcode-data/script2/output/5(2+r2,2).svg

[0_(2+0+2)_0]:   ../../panelcode-data/script2/output/0_(2+0+2)_0.svg
[0_1_(1+0)]:     ../../panelcode-data/script2/output/0_1_(1+0).svg

[0_2_0]:         ../../panelcode-data/script2/output/0_2_0.svg
[0_3_0]:         ../../panelcode-data/script2/output/0_3_0.svg
[3(r2+0,1)]:     ../../panelcode-data/script2/output/3(r2+0,1).svg

[2_(1,0)]:       ../../panelcode-data/script2/output/2_(1,0).svg
[2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)]: ../../panelcode-data/script2/output/2_5(1+r2+r2+r2,1)_4(r2+r2+1,1).svg


## Introducing Panelcode

**Panelcode** is a lightweight layout description language for concisely representing panel-based layouts and design grids using plain text strings.

Each Panelcode string concisely describes a layout. The format is optimized for rectangular panel regions, arranged in row-based groups. Panelcode is human writeable, and collections of layouts may be edited and saved in hand-edited plain text files (for example, a text file containing every page of a graphic novel, one page per line).

The Panelcode specification comes with a parser and a set of example renderers. Parsed layouts may be converted into markup or visualized as images -- e.g. html, svg, xml. Panelcode collections may also be searched for specific layouts or used to generate reporte on common/uncommon layouts.


#### How Panelcode syntax works

| Example                                       | Panelcode      | render              |
|-----------------------------------------------|----------------|---------------------|
| Specify a row of columns as a single number.  | `2`            | ![][2]              |
| Combine rows with underscores.                | `2_3`          | ![][2_3]            |
| Indicate blank rows with 0.                   | `0_3_0`        | ![][0_3_0]          |
| Detail complex groups in parentheses.         | `3(r2+1,1)`    | ![][3(r2+1,1)]      |
| Combine rowgroups and simple rows.            | 2_3_3(1+r2,1)  | ![][2_3_3(1+r2,1)]  |
| Mark large layouts using shorthand.           | `3[*5]`        | ![][3_3_3_3_3]      |
<!--
| Mark groups as uncoded with ~.                | `3(~)`         | ![][3]              |
-->


#### Uses: Why encode pages in Panelode? 

Panelcode is good at abstract description for the purposes of comparison. It can be used to describe visual layouts and document structures such as newspapers, magazine pages, or websites.

It is focused in particular on layouts in visual narrative genres that rely on a fixed layout and reading order -- such as comic strips, comic books, and graphic novels. Large collections of comics may be quickly annotated in Panelcode and then searched and analyzed -- e.g. for common and unusual layouts and elements. Some uses for Panelcode include layout search engines and digital humanities data mining projects of visual materials.

Panelcode was developed specifically for analyzing comics and graphic narrative. It might be of interest for scholars and researchers looking to collect data on layout designs.

Some potential uses:

-  collect layout data:  
   ...e.g. summarizing the layouts of comics, websites, newspapers etc.
-  search by layout:  
   ...e.g. adding composition-based search to comics archives 
-  analyze layouts:  
   ...e.g. "What is the most common layout?" "What are the most unusual layout?"
-  compute layout differences and transforms:  
   ...e.g. "What page elements appear in 'Scott Pilgrim' that don't appear in O`Malley's later work?"
-  generate layouts:  
   ...e.g. render out to HTML, XML, SVG, TEI CBML etc.

Examples:

1. search
    -  "Which pages in this collection are most like Action Comics #1, pg1?"
    -  "What are the most complex layouts in Winsor McKay's Little Nemo?"
2. comparison
	-  "Which layouts are used by both R. Crumb and George Herriman?"
	-  "Which layouts appear in the later years of Bone but not the early years?"
3. summary
    -  "Show a list of every unique layout used in Watchmen"
    -  "Show a list of the most frequent layouts used by JH Williams III"
4. visualization
    -  "Display the most common layouts in the works of Becky Cloonan"
    -  "Display the entire layout sequence of Scott Pilgrim vol.1-6"

It also might be of interest as a stock layout generator for storyboarding or templating content creation, or as a pre-processor for layout generation workflows.

#### Design goals

Panelcode concisely describes the layouts of large collections layout-based works (newspapers, websites, graphic designs, comics, etc.) in a way that enables visual summary,  searchable and comparable using a shared structural vocabulary. It emphasizes abstract layout codes that are quickly specified by hand and can then be rendered as glyphs in many visual forms (html, svg, xml, etc.). Design goals include:

1. **human-readable** (and writeable) simple layout representations.
2. **concise** for rapid accurate data entry, including many shorthand forms.
3. **searchable** to easily accomodate layout data mining and visualization
4. **comparative**  making it easy to say that two pages have "the same" or "similar" layouts or components -- or to concisely describe how they are different.
5. **canonical forms** -- one unique layout, one Panelcode string -- that can easily be derived from any shorthand forms, making identity comparison trivial. This also makes Panelcode friendly for inclusion in address spaces such as filenames or URL paths.
6. **flexibile** accomodation of different media types -- e.g. comic strips, comic books graphic novels, webcomics and webtoons. This includes basic support for compositing layouts in media-specific ways such as 2pg spreads (comic books) or vertical scrolling stacks (webtoons), as well as for various conversions between encoded and rendered Left-To-Right (LTR) and Right-To-Left (RTL) reading order, e.g. comics and manga.

#### Manual layout analysis

As a layout description language, Panelcode was designed to be flexible and human-editable as an alternative and compliment to automatic document layout analysis. Panelcode is not an automated recognition system (although it can be integrated with such systems).

In automated **document layout analysis** a computer analyzes an image of the page, makes best guesses about image segmentation or regions of interest (e.g. building a partition tree), and may further build a model estimating the priority or reading order of the various elements. Such systems are very powerful but also face hard problems and have many limitations -- particularly when dealing with visual narrative. These limtations include:

1. narrow -- very specific definitions of what visual features consitute a region of interest or "panel"
2. inflexibile -- they often cannot be reconfigured to include, group or ignore elements
3. high failure rate -- unusual layouts are not recognized, or are dramatically misrecognized

Even a simple image segmentation algorithm can perform very well on classic comic strip formats and regular grids with gutters, e.g. correctly identifying 99% of the layouts and panel locations of Reg Smythe's comic strip Andy Capp.

However, many categories of page layouts are not recognized by even state-of-the-art layout systems because they do not meet narrow assumptions about what constitutes a layout or a region of interest. As the visual layout being considered becomes more unique, dynamic, innovative, or experimental that layout often tends to become increasingly illegible to automated systems. Because automated encoding performs most poorly on the most innovative work, Bill Watterson's Calvin and Hobbes will have a high failure rate -- and those failures will occur disproportionately on its most acclaimed pages.

The application of document layout analysis to visual narrative is an area of ongoing research. Better results may come from more complex automated systems that use multiple or hybrid approaches to evaluate the same page, as well as from the incorporation of machine learning in different stages of the layout analysis process. However there are reasons to believe that *some* key limitations of automated systems are intractable without strong AI. Comics readers often use a broad set of expert literacies to assemble a theory of a given page, how it is laid out, and how it is meant to be read -- in what units and what order. Such reader literacies may be specific to particular genres, artists, or titles. They may also be based on the layouts of preceding pages, or to the way that narrative interpretations suggests which images are plausibly occuring in the same or different places and times. Narrative plausability and genre convention may thus inform both segmentation and a preferred reading order, and these are sources of information that pixel-based algorithms cannot access.

Panelcode was developed a rapid annotation alternative and complement powerful but extremely limited automated systems. Using Panelcode experts can quickly generate layout representations according to a theory of the page that is informed by their own experience, inflected by their own interests, and nuanced in the face of exceptions.

<!--
Further, Panelcode can integrate with automated systems - their automated layout data can be imported into Panelcode, reviewed, and quickly revised as needed.
-->


## Panelcode is not for publishing

Panelcode is a lightweight layout description language -- it parses, searches, and renders abstract panel-based layout descriptions.

There are many systems for specifying or generating layouts which are primarily focused on content creation and publishing. With different goals, these languages can do many things that Panelcode cannot -- and also cannot do many things that Panelcode can.

1. **Panelcode is not a design presentation format**. It does not specify elements in pixels or picas etc. It is an abstract format expressed in rows and ratios for the purpose of summarizing similar layouts across different works and media forms.

   To style Panelcode output, use a renderer that generates html classes and ids, then style panels them using CSS (Cascading Style Sheets).

2. **Panelcode is not a content format.** Panelcode strings do not contain text, images, etc.

   To organize content with Panelcode, use it in a pre-processor workflow. For example, use a Panelcode string as the header to a Markdown document.

3. **Panelcode is not a templating language**. It contains no features for orchestrating dynamic content generation.

   To generate templates with Panelcode, use it in a pre-processor workflow to render a template framework (e.g. html, xml) and then dynamically embed template elements.

4. **Panelcode is not for specifying responsive web designs**. Layouts are conceptually "fixed."

   Panelcode layouts that exhibit generic responsive design features like liquid/fluid layout, use CSS or a custom renderer.

Panelcode is _also_ not related to these other things with the same or similar names:

-  [military signaling methods using marking panels](http://www.thefreedictionary.com/panel+code), a.k.a. 'panel code'
-  [aerodynamic potential flow code](https://en.wikipedia.org/wiki/Aerodynamic_potential-flow_code), a.k.a. 'panel codes'
-  [card security codes](https://en.wikipedia.org/wiki/Card_security_code), a.k.a. 'panel codes' 


## What Panelcode cannot encode

Panelcode can encode a lot -- but these encodings are always abstractions and approximations, and there are many layouts that it can only partially represent. It is optimized for a subset of primarily horizontal, row-based grid layouts, or for expressing a grid-based approximation of a layouts that are "close enough."

In general, a Panelcode layout is a set of rectangular regions laid out on a checkerboard. That paradigm of abstraction comes with strong assumptions, such as:

1. a layout is a collection of rows
2. the rows are on a grid
3. the panel units are rectangles
4. panels are aligned without overlapping

To the extent that this is not true, Panelcode layouts are increasingly distant abstractions of the original page -- both approximate, and in many ways inaccurate. However, this framework of "rows and panels" provides a method for comparison. The value in using Panelcode for data mining, search, and information visualization is the extent to which says "these layouts are similar" is a useful gesture across extremely disparate material.






Some non-rectalinear layouts are poorly approximated:

 non-rectalinear layouts challenging , non-rectangular panels

Non-rectalinear layouts:
-  encodable *as if* they were rectalinear:
    -  diagnol layouts
    -  offset panels
-  encodable *as if* they were explicitly paneled:
    -  borderless layouts
    -  collages
-  encodable 

Panelcode can only approximate non-rectangular such as:

-  non-rectangular layouts
   -  "shattered glass" layouts
   -  continuous scenes
   -  continuous with panelboxes
   -  angled gutters


Panelcode does not yet have support for:

-  deeply nested layouts (inset panels, panel groups within groups within groups)

Panelcode cannot encode non-rectangular panel units:

-  non-rectangular panels
   -  "L" panels
   -  polygon panels
   -  "stairs"
   -  circular panels and layouts
   -  shaped frames
-  non-2D surfaces (boxes, sculptures, Mobious strips)

 easily encode:


#### What counts as a panel?

Panelcode is agnostic about what a panel is. For this reason there are many apparently simple and straightforward layouts which could be coded in different ways. In comics, for example, Panelcode has no special support for captions -- a box of text that presents narration.

Depending on the layout and art style a caption may be a marked off panel section, or inset within a panel, or floating between panels, or some combination. Correspondingly, captions in a Panelcode might be treated as:

1.  As a part contents of an image panel that it captions -- unnecessary to encode separately.
2.  As a text panel, appearing next to image panels.
3.  As a text panel inset within an image panel.

A given encoding might chose one method consistently or use some mix of the three encoding strategies above depending on how captions appear are rendered on a given page.

<!-- 

Consider this example:

	example

-->

The correct approach may depend on the project, the layout style, and the relative advantages of a simple encoding vs. a complex. In general, simple encodings ignore narration boxes.


##### difficult layouts

<!--
-  non-horizontal reading paths
   -  vertical reading paths
   -  multiple reading paths
   -  labeled reading paths
   -  numbered panels for reading order
-->


<!--

Consider these examples of difficult layouts:

|-------------|-------------|-------------|-------------|
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |

Some of these examples might not be tractable in panelcode:rowcode, but could be described concisely in the future in panelcode:verticode or in panelcode:layercode. Conversion and comparison between may be tricky / impossible.

-->

##### working with the unencoded and the unencodeable

Panelcode offers two primary tools for working with layouts that it cannot represent (in whole or in part).

1. uncoded + count hints
2. uncoded + custom properties

Count hints allow search and statistics to reason about the layout using a best-approximation.

Custom properties allow tagging of unusual layouts or elements.

	(~)     # compare ?
	(20~)   # 
	1(~)    # compare 1
	3(~)    # compare 3
	3(~)_3  # compare 3_3

	3(~.circle)
	5(~.circle.stairs)
	3(~.stairs)
	10(~.collage)


## More on Syntax

| Example                           | Panelcode       | render              |
|-----------------------------------|-----------------|---------------------|
| simple row examples               | `2`             | ![][2]              |
|                                   | `2_2`           | ![][2_2]            |
|                                   | `1_3_2_4`       | ![][1_3_2_4]        |
|                                   | `1_2_3_4_5_6`   | ![][1_2_3_4_5_6]    |
| multiplier shorthand              | `3[*5]`         | ![][3_3_3_3_3]      |
| complex rowgroups in parentheses  | `3(r2+1,1)`     | ![][3(r2+1,1)]      |
|                                   | `2_3_3(1+r2,1)` | ![][2_3_3(1+r2,1)]  |
|                                   |                 |                     |
| zero layouts (blank)              | `0`             | ![][0]              |
| zero panels (absent)              | `0_1_(0+1)`     | ![][0_1_(1+0)]      |
| uncoded layouts                   | `(~)`           | ![][(~)]            |
| uncoded rows                      | `2_(~)`         | ![][2_(~)]          |

Further features under development:

| Example                           | Panelcode       | render                            |
|-----------------------------------|-----------------|-----------------------------------|
| page series                       | `1_1;2_2;;3_3;4` |                                  |
| page compositing                  | `2_2++3+3`      | ![][2_2]![][3_3] **               |
| page spreads                      | `2_3_2++`       | ![][2_3_2] **                     |


|     | What the parts mean     |
|-----|-------------------------|
| 1-9 | a row of panels         |
| 0   | a blank panel or row    |
| ~   | an unencoded area       |
| _   | next row in a page      |
| ()  | a rowgroup              |
| +   | next panel in a row     |
| ,   | next row in a rowgroup  |
| ;   | page separator          |
