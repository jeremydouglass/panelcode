# RESEARCH

Grrl Power to end panel codes
Idea - panel counts, row counts, row group counts - each as summary stats. Also a sorted row number (ascending) to match.

Some potential lines of investigation for research questions? See SEARCHING.md



## Literature Review


### Vocabulary (general)

-  https://en.wikipedia.org/wiki/Page_layout#Design_elements_and_choices


### Data sources

-  potential (unvetted)
	-  http://www.comicbooklibrary.org/
	-  http://www.comicbooklibrary.org/Home


### Places for submission

-  [The Comics Journal](http://www.tcj.com/)
-  DHQ
-  [Oubapo](https://en.wikipedia.org/wiki/Oubapo) - Matt Madden
-  -  www.thecomicsgrid.com — recently did a CFP on Jazz and comics that mentioned DH that I saw on some listserv


### Tools and systems

-  ACBF (Advanced Comic Book Format) -- Robert Pastierovic -- https://launchpad.net/acbf

   > Some of the properties of ACBF are:
   > 
   > -  Definition of comic book metadata (title, authors, genres ...)
   > -  Definition of comic book structure (pages, frames) as well as order in which they follow.
   > [...] ACBF is an extension of XML.
   
   -  [ACBF Viewer]() -- "ACBF Viewer is a viewer application capable of reading ACBF, CBZ/CBR and ACV comic book file formats. **It is written in Python programming language.** [...] It is distributed under GNU GPL version 3."
   -  author outreach for feedback -- only a few months ago! https://www.reddit.com/r/comicbooks/comments/3xtdmw/advanced_comic_book_format_acbf/
   - ...and four years ago http://comicbookplus.com/forum/?topic=4514.0
     > "definition of comic book structure (pages, frames) - if frames are defined you can zoom in to frame level and read frame by frame (usefull on smaller screens like PDAs, tablets ...)"
  
-  CBML (Comic Book Markup Language) -- Josh Walsh.
-  CSDL (Comic Strip Descriptive Langauge) -- Alves et al.) 
-  ComicsML -- Jason McIntosh.
-  Comics Renobator -- Dave Horlick.
   -  "A Comics Editor and Storyboarding Tool." This sounds very interesting by heresay, and was open source and cross platform (Java, ~2004), but the site(s) are all lost. Maybe contact the original author.
		-  https://www.google.com/search?q=renoberator
		-  https://web.archive.org/web/20081121042003/http://www.happinessfunction.com/renoberator/
		-  http://webcache.googleusercontent.com/search?q=cache:qy9tKar6ZxsJ:www.happinessfunction.com/renoberator/&num=1&hl=en&gl=us&strip=1&vwsrc=0
-  Defendini's (unnamed?) "responsive web design" approach to online comics (CSS div driven)
-  RageML
-  Stevens's (unnamed) "XHTML" approach to online comics.




## Bibliography

-  (Alves et al. _[Comics2D: Describing and Creating Comicsfrom Story-Based Applications withAutonomous Characters](http://www.academia.edu/544526/Comics2D_Describing_and_creating_comics_from_story-based_applications_with_autonomous_characters)_).
	
	> "We identify common conceptsin comics, introduce the Comic Strip Description Language(CSDL) and propose a system to automatically generate comicstrips using this language."

-  [Covery, Suzanne. _Beyond the Balloon: Sound Effects and Background Text in Lynn Johnston's For Better or For Worse_.](http://www.english.ufl.edu/imagetext/archives/v2_2/covey/). Based on CBML, and gives a working markup example that includes panel attributes for panel x,y,width,height (although these are unused). Includes the useful simplified diagram of CBML -- note that it has panelgroups. Not a great article. 

-  (Defendini, Pablo. [Standards, Semantics, & Sequential Art--Toward a Digital Comics Praxis](http://pablodefendini.github.io/digital-comics/).)
Part 3: ["A New Approach to Digital Comics"](http://pablodefendini.github.io/digital-comics/part-3.html)

	> "Once you start building comics out of HTML and CSS as part of these investigations, you’ll realize that you can recreate almost anything that's been done on a physical page." [Part 4](http://pablodefendini.github.io/digital-comics/part-4.html)

	-  http://pablodefendini.github.io/digital-comics/layout__4-row--11-panel.html

-  (Duncan, 1999. _[Toward a Theory of Comic Book Communication](http://www.hsu.edu/academicforum/1999-2000/1999-0AFToward%20a%20Theory%20of%20Comic%20Book%20Communication.pdf)_). An older but interesting meditation by an established scholar, partly self-published? or a draft. Describes methodology for reviewing some titles, but the write-up is purely conceptual. Describes common thinking on rhetoric and content-layout distinctions, makes the move that aspects of layout proper are too hard to deal with. Might be interesting to revisit one of Duncan's titles and show how Panelcode can answer an open question posed (e.g. "no significant pattern").

	> "The first phase of the research employed an inductive, panel-by-panel examination of ten graphic novel or comic book stories in order to discover the rhetorical dimensions, devices and strategies of encapsulation. The examination purposely excluded elements of composition and
layout." (Duncan, 1999. _[Toward a Theory of Comic Book Communication](http://www.hsu.edu/academicforum/1999-2000/1999-0AFToward%20a%20Theory%20of%20Comic%20Book%20Communication.pdf)_)

	> "The page is, by necessity of the form, an organizing principle and a unit of encapsulation. The same is also true of any two facing pages of story." (Duncan, 1999. _[Toward a Theory of Comic Book Communication](http://www.hsu.edu/academicforum/1999-2000/1999-0AFToward%20a%20Theory%20of%20Comic%20Book%20Communication.pdf)_)

	> "Are there genres of panels with specialized functions? There is no significant pattern of specialized functions for the first panels of pages. For instance, establishing panels, those that introduce the reader to the location of a new scene, seem just as likely to appear anywhere else on the page as they do in the first panel. However, last panels of pages more often serve specialized functions. The most common functions are the cliffhanger panel, that impels the reader to go the next page to find out how a conflict is resolved, and the end of scene panel. Other discernable genres that occur in the last panel are the dramatic revelation panel, the startling development panel, the clue panel, the climax panel (in which the conflict is resolved), the denouement panel (which is usually the last panel of the last page), the address-the-audience panel (often the last panel of the last page), and the posed panel (in which a dramatic picture of the hero is presented outside the context of the narrative)." (Duncan, 1999. _[Toward a Theory of Comic Book Communication](http://www.hsu.edu/academicforum/1999-2000/1999-0AFToward%20a%20Theory%20of%20Comic%20Book%20Communication.pdf)_)

-  Frimson, Mark. [RageML - XML Markup for Rage Comics](http://markfrimston.co.uk/articles/22/rageml-xml-markup-for-rage-comics). 23 January 2013.
      
	A parody but (apparently?) working XML validator for marking up that specific genre of comic. The format is really wonky -- partly as a parody, but partly because it is intended to be an image generator, and so has lots of shorthand to support rendering back out of the encoding. Interesting that it appears to have used an XML transform to do exactly what I did in my prototype -- output html embedded in SVG to create a graphic.

	> "rageml.xsl is an XSL stylesheet declaring a transform from XML to Scalable Vector Graphics format, and is an excellent example of just how far you shouldn't take XSL."

-  McIntosh, Jason. _ComicsML: A Simple Markup Language for Comics](http://www.xml.com/lpt/a/767)_. April 18, 2001 Interesting precursor (acknowledged?) to the DHQ work, and also notable for likewise ducking the layout issue.
	
	> **No Layout Here**
	> 
	> ComicsML has no concept of layout. It knows that each strip has a bunch of panels in it, but it makes no presumptions about how to present them, beyond the order in which the reader is to see them. If a comic that makes use of ComicsML chooses to add URLs for all its panel images, then an application will not know how to display them without further information from another source, and will instead use its own methods for displaying the panels one after the other.
	> 
	> For the majority of comics, whose panel layout is simply a matter of convenience, this shouldn't pose a hardship. It might become less than ideal for comics that use full-page layouts, where panel positioning can often be an art in itself, and the model might break down for those very rare comics which use panels in ways integral to their very meaning. However, I suspect that most members of the former group could probably survive the application panel-description markup with no pain.
	> 
	> The first draft of the ComicsML DTD actually did have some elements for performing rudimentary layout modeled after HTML's table elements, but I decided to ditch that, preferring to make ComicsML all about content. If you have a different view, please let me know using the form on the last page.

	-  Project site: [ComicsML - XML for digital comics](http://www.jmac.org/projects/comics_ml/)
		-  [ComicsML Writer's Guide](http://jmac.org/projects/comics_ml/docs.html)
		   > "**Layout**: ComicsML makes no account for panel layout, mostly because I couldn't think of a way to do this myself without adding frustrating and frightening levels of complexity to the language. I've since seen some encouraging example from other XML-based languages, though, so this is far from a dead issue."
		-  http://jmac.org/projects/comics_ml/about.html
			-  contains interesting references to some related
			   concepts and implementations.

-  Peeters, Benoît. [Four Conceptions of the Page](http://www.english.ufl.edu/imagetext/archives/v3_3/peeters/). From Case, planche, récit: lire la bande dessinee (Paris: Casterman, 1998), pp. 41-60. trans. Jesse Cohn. 

-  Stephens, John. _[Applying the fine art of web design to online comics](http://designop.us/wrote/applying-the-fine-art-of-web-design-to-online-comics)_. 2009.

   > "Make the meaning of your comics semantically rich and searchable."
   
   Unfortunately demo page links are all broken.

-  Tinsley, Kevin. _[Digital Prepress for Comic Books]()_. 2009. CHAPTER 7. PAGE LAYOUT - 115.

   Discussing Quark and InDesign -- some interesting observations.
   
   > "Double-page spreads need to be separated in the page layout because, with the sole exception of the center spread, facing pages in print do not face each other in the imposition file." (118)
   
   Also a short comment on scanning double-page spreads in 65. Might be a good source of industry terms for page elements and compositions. See also: [Glossary of comics terminology](https://en.wikipedia.org/wiki/Glossary_of_comics_terminology)
	
-  Walsh, 2012. _[Comic Book Markup Language: An Introduction and Rationale](http://www.digitalhumanities.org/dhq/vol/6/1/000117/000117.html)_

-  Wen et al. _[Pomics: A Computer-aided Storytelling System with Automatic Picture-to-Comics Composition](http://www.iis.sinica.edu.tw/~swc/pub/pomics.html)_. 2016.

   Auto-generated comics from photo streams -- although doesn't discuss the layout generation techniques, so not directly relevant. Generator, not analytic or descriptive or specification.

-  Whitson, Roger. _[Presentation for Comics and the Multimodal World](http://www.rogerwhitson.net/?p=2130)_. 2013.  

   Discusses DH context, cites my work with Lev. Good recent literature review from 2013.

-  Witig, Joseph. The Error and the Grid. A Comics Studies Reader. ed. Jeet Heer, Kent Worcester. p149-156. [https://books.google.com/books?id=9LUYhG9qO_8C&pg=PA153&lpg=PA153&dq=comics+tier+vs+row&source=bl&ots=tAgiXs6JCA&sig=mGXI03peoDnVt5FKQ2AObWt_rNo&hl=en&sa=X&ved=0ahUKEwiiltea8_XMAhVLXlIKHfp3A8IQ6AEITTAN#v=onepage&q=comics%20tier%20vs%20row&f=false]()

-  Wright, Vonda E. _[Metadata for Graphic Novels and Comic Books: Comic Book Markup Language and Advanced Comic Book Format](http://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=3168&context=libphilprac)_.

   This project has 2 parts, 1. detailed crosswalk between the ACBF, CBML, and DC and 2. a small collection of 5 records created from CBZ and CBR reader files from the Digital Comic Museum public domain collection cataloged in each of the three schemas ACBF, CBML, and DC. 


### research NOTES (misc)

-  [The Grand Comics Database -- Cheat Sheet](http://docs.comics.org/wiki/Cheat_Sheet) -- top-level metadata on comics for http://www.comics.org/
-  [An Application of Markup: A Comic Strip Finder](http://db.inf.uni-tuebingen.de/staticfiles/teaching/ws1213/xmldb-02.pdf). Torsten Grust (WSI) Database-Supported XML Processors Winter 2012/13.
-  [Coding a comic - Volunteer Notes](https://codeclubprojects.org/en-GB/archived/comic/notes.html)
-  [Web Accessibility Best Practices--Comics](http://cita.disability.uiuc.edu/html-best-practices/text/comics.php) -- Accessible image markup and D-link
-  [Kindle Comic Creator User Guide](http://kc2.s3.amazonaws.com/KC2UserGuide_en.pdf) -- version 2013.03.
	> "The **Virtual Panel Movement** and **Page Turn Direction** settings combine to set the **Panel Order** for a page. This determines in what order the four quadrants of the page are read"--p40, diagrams 41, 43. Settings for "double-page spread," p53-54.  Examples drawn from childrens' books and manga. kb8 files.
	-  See also: "Fixed layout is a complex, print-replica format designed primarily to accommodate children’s picture books, manga and digital comics." [*](http://www.digitalbookworld.com/2014/before-you-make-a-fixed-layout-ebook-five-things-to-watch-out-for/)
-  [Data Comics: Sequential Art for Data-Driven Storytelling](http://hcil2.cs.umd.edu/trs/2015-15/2015-15.pdf) -- possibly not relevant, but interesting. 2015.
-   [What are the different grids used in graphic novels/comic books and when is each kind used?](https://www.quora.com/What-are-the-different-grids-used-in-graphic-novels-comic-books-and-when-is-each-kind-used)
-   1995 discussion on TEI encoding of comics: [strip cartoon encoding ?](http://tei-l.970651.n3.nabble.com/strip-cartoon-encoding-td2337107.html)
-   How-Tos
	-   [Create a Comic: How to Plan and Lay Out Your Comic](http://design.tutsplus.com/tutorials/create-a-comic-how-to-plan-and-lay-out-your-comic--cms-24179) -- 2015
	-  [Field Guide to Fixed-Layout For E-Books](https://www.bisg.org/docs/FieldGuideFXLBooksfinal_version1.0_.pdf) "KF8 features a built‐in Panel View that allows comic books and graphic novels to be presented in high resolution color" ... "Book Type, which has two default values based on the original intent of fixed layout. The values can only be set to “children” or “comic.”"
	-  [Comic Book Software Reviews](http://comic-book-software-review.toptenreviews.com/)
		- 	https://en.wikipedia.org/wiki/Clip_Studio_Paint
			-  http://my.smithmicro.com/manga-studio-5-compare.html
			-  [Manga Studio Panel Layers](https://www.youtube.com/watch?v=qwMC20UvM0k) (2007)
			-  [Manga Studio: Paneling Made the Easy Way
](http://www.mangatutorials.com/2008/manga-studio-paneling-made-the-easy-way/)
-  ON LAYOUT ANALYSIS:
	-  (Khodabandeh, Bizhan. [Panel Layout--The Golden Ratio](http://www.makingcomics.com/2014/05/07/panel-layout-golden-ratio/). 2014.) Discussion contains an interesting definition of river. "A river occurs when there is a gap in information that coincides with a gap below. The danger is that a reader might drop down to the next line of info before completing the first one." Also tutorial images on gridding and links to blueline grid files
-  MISC Comic making resources
	-  http://comicsforbeginners.com/free-online-tools-for-comic-creators/

-  (_[EPUB 3 Best Practices](https://books.google.com/books?id=z0zpvR5QNvsC&pg=PA262&lpg=PA262&dq=comic+layout+markup&source=bl&ots=bQP602liUr&sig=BBgFyEOqbsVuO115wHAK2n7xsA8&hl=en&sa=X&ved=0ahUKEwiX-6ms6-vMAhXlpYMKHQzWAEsQ6AEIWTAJ#v=onepage&q=comic%20layout%20markup&f=false)_. By Matt Garrish, Markus Gylling. Chapter 9:Accessibility, p262: Image Layouts.) "The method of fixed layouts... Comic books and manga are the prime examples...."

-  new html responsive image sizing -- this could be relevant at some point to my struggles with html-embedded in svg -- https://ericportis.com/posts/2014/srcset-sizes/#part-2

-  [Storyboard](https://en.wikipedia.org/wiki/Storyboard) (Wikipedia)
-  [Page layout -- grids vs templates](https://en.wikipedia.org/wiki/Page_layout#Grids_versus_templates) (Wikipedia)


#### NOTES ON "layout description language":

-  Apple. "Auto Layout [Visual Format Language](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html)"

	Really interesting incorporation of concise parameters.

	-  Kugler. [Advanced Auto Layout Toolbox](https://www.objc.io/issues/3-views/advanced-auto-layout-toolbox/). 2013.

-  [ODIL: an SGML description language of the layout structure of documents](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=599040&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D599040) (1995)
   
   > This paper describes a coding format in SGML for the output of a document recognition prototype. Our proposal is a DTD named “ODIL”-Office Document Image description Language-that describes precisely the layout structure of a document after all recognition phases, including OCR. All layout objects of a document are defined in the form of SGML elements, and their characteristics are defined by SGML attributes. The basic objects are blocks, containing homogeneous information. Five types of information are supported by the ODIL language: texts, photos, line graphics, tables, mathematic formulas.

-  Thomas, Barry. [A layout document description language primer](http://www.amazon.com/layout-document-description-language-primer/dp/1871915007) (1989)

-  ? Tutenel, T.; Smelik, R. M.; Bidarra, R. & de Kraker, K. J. (2010), A Semantic Scene Description Language for Procedural Layout Solving Problems., in G. Michael Youngblood & Vadim Bulitko, ed., 'AIIDE' , The AAAI Press, .



-  circuit boards etc.
	-  [GBLD: A Formal Model for Layout Description and
Generation](https://espace.library.uq.edu.au/view/UQ:9876/_Tseng04_-FDL_04.pdf) (~2004)

	   This is for specifying circuit boards, but the thinking about concise, human-readable strings is very interesting -- remarkably similar in some ways to my own design patterns.
   
	   > "Grammar-Based Layout Description (GBLD) language" ... "The strings generated by GBLD represent flattened mask layouts."

	-  [Block description language (BDL): A structural description language](http://dl.acm.org/citation.cfm?id=800777) (1984) "a language for capturing the structure of an electronic system"

-  "page description language"
	
	> page description language: A high-level language for describing the layout of a page to be displayed or printed. The two major languages are Adobe's PostScript and HP's PCL, which are device independent and built into most printers. Adobe's PDF format is also widely used for printing as well as publishing on the Web (see PostScript, PCL and PDF). The standard for page-oriented XML documents is XSL-FO (see XSL). (Computer Desktop Encyclopedia copyright ©1981-2016) [*](http://lookup.computerlanguage.com/host_app/search?cid=C999999&term=page+description+language)
	
	-  [XSL-FO](https://en.wikipedia.org/wiki/XSL_Formatting_Objects) > XSL-FO [tables](https://en.wikipedia.org/wiki/XSL_Formatting_Objects#Tables)

	>  "An FO table functions much like an HTML/CSS table. The user specifies rows of data for each individual cell. The user can, also, specify some styling information for each column, such as background color. Additionally, the user can specify the first row as a table header row, with its own separate styling information. The FO processor can be told exactly how much space to give each column, or it can be told to auto-fit the text in the table."
	
	-  [Page description languages: development,
implementation and standardization](http://cajun.cs.nott.ac.uk/compsci/epo/papers/volume1/issue2/epalo012.pdf) (1988)
	-  Adobe PostScript
		-  [Thinking in PostScript](http://w3-o.cs.hm.edu/~ruckert/compiler/ThinkingInPostScript.pdf) (1990) p19+ syntax and example code
	-  Hewlett-Packard PCL (Printer Control Language)
	-  also / or "page layout language"? e.g. "A Page Layout Language (PLL) is used to describe the general presentation of individual pages." [*](http://www.anomaly.org/wade/thesis/) (~2001)
-  graphviz

-  [XFDL](https://www.w3.org/TR/1998/NOTE-XFDL-19980902) (1998) / [XForms](https://www.w3.org/TR/2009/REC-xforms-20091020/) (2009) [on Wikipedia](https://en.wikipedia.org/wiki/Extensible_Forms_Description_Language)

See Also:

-  Danilo et. al. [SVG as a Page Description Language](http://www.svgopen.org/2002/papers/danilo_fujisawa__svg_as_page_description_language/) (2002).
-  [Layout (computing)](https://en.wikipedia.org/wiki/Layout_(computing))
	-  [Page layout](https://en.wikipedia.org/wiki/Page_layout)
	-  [Document layout analysis](https://en.wikipedia.org/wiki/Document_layout_analysis)
-  [List of layout engines](https://en.wikipedia.org/wiki/List_of_layout_engines)
-  [User interface markup language](https://en.wikipedia.org/wiki/User_interface_markup_language)
-  [Constraint Cascading Style Sheets (CCSS)](https://en.wikipedia.org/wiki/Cassowary_(software)) and its successor GSS, [Grid Style Sheets](http://gridstylesheets.org/), "a layout language and layout engine for the web"
   > "FLEXBOX? MEH"

Some potential terms:

-  Page Description Language (PDL)
-  Standard Page Description Language (SPDL)
-  Forms Description Language (FDL)


#### Further reading -- someday

-  The Craft of Information Visualization: Readings and Reflections. edited by Benjamin B. Bederson, Ben Shneiderman. 2003.  https://books.google.com/books?id=-ZGJOcpTGXsC&pg=PA190&lpg=PA190&dq=comic+page+visualization&source=bl&ots=SRsUeR7FMT&sig=7nwsEa7GiPXSZjUpa9An5r5xEl4&hl=en&sa=X&ved=0ahUKEwiI-NDQ6uvMAhUC9YMKHVE1ANoQ6AEIQDAJ#v=onepage&q=comic%20page%20visualization&f=false
   
   > ~p190 -- "Description of Book Readers": Standard Reader, Comic Strip Reader, Spiral Reader.
   
   Potentially an interesting example of infovis output interfaces...?

-  [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)

	> Huffman coding is a lossless data compression algorithm. The idea is to assign variable-legth codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code.


-  Page layout markup language https://www.google.com/patents/US20040205553
-  Metatemplate driven multi-channel presentation http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=1286807&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D1286807



...The "holy grail layout" is `1_3_1` in panelcode. ;)





