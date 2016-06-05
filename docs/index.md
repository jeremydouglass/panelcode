# Panelcode -- tools for panel-based layouts

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





## Introducing Panelcode

**Panelcode** is a lightweight layout description language for concisely representing panel-based layouts and design grids using plain text strings. 

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
| zero layouts (blank)              | `0`             | ![][0]              |
| zero panels (absent)              | `0_1_(0+1)`     | ![][0_1_(1+0)]      |
| uncoded layouts                  | `(~)`           | ![][(~)]             |
| uncoded rows                     | `2_(~)`         | ![][2_(~)]           |


Panelcode is good at abstract description for comparison. It is focused in particular on layouts in comics strips, pages, and books -- although it could also be used to describe other visual layouts and related document structures. Large collections of comics may be quickly annotated in Panelcode and then searched and analyzed -- e.g. for common and unusual layouts and elements.

Further features under development:

|                                   | Panelcode       | render                            |
|-----------------------------------|-----------------|-----------------------------------|
| page series                       | `1_1;2_2;;3_3;4` |                                  |
| page compositing                  | `2_2++3+3`      | ![][2_2]![][3_3] **               |
| page spreads                      | `2_3_2++`       | ![][2_3_2] **                     |


#### How Panelcode syntax works

|                                              | Panelcode   | render         |
|----------------------------------------------|-------------|----------------|
| Specify a row of columns as a single number. | `2`         | ![][2_2]       |
| Connected rows with underscores.             | `2_3`       | ![][2_3]       |
| Indicate blank regions with 0.               | `0_3_0`     | ![][0_3_0]     |
| Detail complex groups in parentheses.        | `3(r2+1,1)` | ![][3(r2+1,1)] |
| Detail uncoded groups in parentheses with ~. | `3(~)`      | ![][3(~)]      |


#### What Panelcode produces





#### Design goals

For abstract layouts to be quickly specified and portable between rendering targets.

For large collections of layout-based work (web design, comics, etc.) to be concisely described in terms of layout.

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




## What Panelcode is not

1. **Panelcode is not a design presentation format**. It does not specify elements in pixels or picas etc. It is an abstract format expressed in rows and ratios for the purpose of summarizing similar layouts across different works and media forms.

   To style Panelcode output, use a renderer that generates html classes and ids, then style panels them using CSS (Cascading Style Sheets).

2. **Panelcode is not a content format.** Panelcode strings do not contain text, images, etc.

   To organize content with Panelcode, use it in a pre-processor workflow. See the example for a Panelcode string as a header to a Markdown document.

3. **Panelcode is not a templating language**. It contains no features for orchestrating dynamic content generation.

   To generate templates with Panelcode, use it in a pre-processor workflow to render a template framework, then dynamically embed template elements.

4. **Panelcode is not for specifying responsive designs**. Layouts are -- at least initially -- conceptually "fixed."

   To output Panelcode layouts with generic response design features, use CSS or a custom renderer.

Panelcode is _also_ not related to:

-  [military signaling methods using marking panels](http://www.thefreedictionary.com/panel+code), a.k.a. 'panel code'
-  [aerodynamic potential flow code](https://en.wikipedia.org/wiki/Aerodynamic_potential-flow_code), a.k.a. 'panel codes'
-  [card security codes](https://en.wikipedia.org/wiki/Card_security_code), a.k.a. 'panel codes' 


#### What Panelcode can and can't encode

##### difficult layouts

Panelcode can encode a lot, but there are also many layouts that Panelcode cannot represent. It is optimized for a subset of primarily horizontal, row-based grid layouts, or for expressing a grid-based approximation of a layouts that are "close enough." 

Panelcode can't easily encode:

-  diagnol layouts
-  deep nesting of panel insets
-  non-horizontal reading paths
   -  vertical reading paths
   -  multiple reading paths
   -  labeled reading paths
   -  numbered panels for reading order
-  non-rectangular panels
   -  "L" panels
   -  polygon panels
   -  "stairs"
   -  circular panels and layouts
   -  shaped frames
-  non-rectangular layouts
   -  "shattered glass" layouts
   -  offset panels
   -  continuous scenes
   -  continuous with panelboxes
   -  angled gutters
   -   borderless
   -   collage
-  non-2D surfaces

Consider these examples of difficult layouts:

|-------------|-------------|-------------|-------------|
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |
|  [][image]  |  [][image]  |  [][image]  |  [][image]  |

Some of these examples might not be tractable in panelcode:rowcode, but could be described concisely in the future in panelcode:verticode or in panelcode:layercode. Conversion and comparison between may be tricky / impossible.

##### what counts as a panel?

Panelcode is also agnostic about what a panel is. For this reason there are many apparently simple and straightforward layouts which could be coded in different ways. In comics, for example, Panelcode has no special support for narration boxes. They might be treated:

1.  As part contents of the panel that they caption.
2.  As panels in their own right.
3.  As inset panels.
4.  As some mix of the three above, depending on how they are rendered.

Consider this example:

	example


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

