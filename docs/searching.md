## Searching / Querying

-  layout frequency
	-  What is the most common / uncommon layout?
		-  in a work? in a series?
		-  in an artist corpus?
		-  in a genre?
		-  in a period?
		-  in a corpus (all known work)
	-  What are the frequencies distributions?
		-  for works, series, artists, genres, periods, etc.
		-  how do some frequency distributions compare to others?
-  layout sequences
	-  What is the most common / uncommon sequences?
		-  row-to-row? of 3 rows, n rows?
		-  page-to-page? of 3 pages?
		-  in a work? in a series?
		-  in an artist corpus?
		-  in a genre?
		-  in a period?
		-  in a corpus (all known work)
	-  What are the sequence frequency distributions?
		-  for works, series, artists, genres, periods, etc.
		-  how do some frequency distributions compare to others?


Search for layouts that are often paired with other layouts, either verso-recto or in general. Rank all pairings. Abstract and rank again.

Is there a don’t-repeat-yourself rule? More than expected from chance? between single pages? verso-recto? between pairs of page layouts? for total layouts independent of sequence? Can non-repetition variability rates be estimated (as totals or rolling averages) for different works, authors?

Query: how many pages are made up of only full-width panels?

	1
	11
	111
	1111
	11111 ...

Query: how many pages are made up of only full-height panels?

	1
	2
	3
	4
	5 ...

Support separate encoding of the verso and recto for 2pg spreads? In general, no -- no reason one can't do this, but it is generally misleading -- if even one major panel crosses the fold, better to list it as a single layout and mark it --.2pg

Panelcode can be used to define rows, rowgroups, pages, and (multi-page) spreads.


### Examples -- discussion of concrete example

> **A note on ideal example pages for demos:**
> 
> 1.  A comics page on programming and Godel Escher Bach -- might be a great example page. https://books.google.com/books?id=IQRJCgAAQBAJ&pg=PA23&lpg=PA23&dq=comic+processing+language&source=bl&ots=MeJcwH3juq&sig=q5-Qei6h5Vig6-in7ogS2dajN4c&hl=en&sa=X&ved=0ahUKEwj9k52d6u7MAhUm94MKHaCYDhs4ChDoAQgpMAM#v=onepage&q=comic%20processing%20language&f=false
> 2. Logicomix -- some page.
> 3. Asterios Polyp?
> 4. Page from Understanding Comics or Remaking Comics.
> 5. Also perhaps computer scene from Watchmen
> 6. ... keep brainstorming.


### Questions / Code

##### row questions

	What number / percentage of the pages in x...
	...contain a this specific row layout?
		...the most common
		...the most rare
		...the most unusual among a wider population
		...the most typical among a wider population
	Which page in x...
	Which projects...

##### row count code

	is_counts()
		3       --> True
		3_2_4   --> True
		1_7_1_2 --> True
		--> False
		--> False
		--> False

	counts_to_grids()
		4_4_4_4 --> 4x4
		4_4_4_2 --> 4x2_2
		--> False
		--> False
		--> False

	counts_to_grids_force()
		4_3_5_4 --> 4x4
		4_3_4_3 --> 4x4
		4_1_2_3 --> 3x4 ...?

	counts_to_groups()
		3_3_3_3 --> 3(3)_3(3)_3(3)_3(3)

	counts_to_expanded()
		3_3_3_3 --> 3(1+1+1)_3(1+1+1)_3(1+1+1)_3(1+1+1)

#### group questions ####

#### group code ####

	is_groups()

	groups_to_grids()
		?
	groups_to_counts()
		?

	groups_to_expanded()
		!

	groups_add_counts
	groups_strip_counts
	groups_validate_counts

	groups_alphabetize_







## Methods


### Time-series analysis

I have a series of numbers for each of a large number of comic books / graphic novels / web comics. These numbers are panel counts -- the number of panels per page, or per rowgroup within a page.

Panelcode row counts for the initial pages of Scott Pilgrim, vol. 1:

	1; 1; 1; 1; 1222; 2221; 121; 12; 1; 112; 2111;
	122; 131; 221; 311; 414; 2111; 112; 1221; 1222;
	2222; 2222; 2221; 12; 1212; 1221; 12; 113

Page panel counts for the same pages:

	1; 1; 1; 1; 7; 7; 4; 3; 1; 4; 5;
	5; 5; 4; 4; 9; 5; 4; 6; 7;
	8; 8; 7; 3; 6; 6; 3; 5

This title has ~160pgs, and ~3 rowgroups per page.

-   series of ~160 panel counts
-   series of ~480 row counts

Method questions:

-   Could an algorithm "recognize" that a particular sequence was likely to come from a particular title / artist / genre?
-   Could an algorithm "predict" future trends based on past information?
-   What are the patterns?
	-   are there recurring rises and falls, etc.
-   What are the meta-patterns?

-  [dynts functions](https://pythonhosted.org/dynts/functions) — time series analysis — e.g. for economics. lots of measures, like rolling variance and volatility


#### Test viz - sparklines

I tried quick bar and line graphs (sparklines) of some panel counts, just to see:

>  http://omnipotent.net/jquery.sparkline/#s-about  
>  4, 8, 9, 3, 4, 6, 5, 5, 4, 9, 5, 7, 6, 5, 8, 1, 7, 8, 9, 7, 8, 10, 9,  8, 7, 8, 8, 8, 8, 13, 5, 9, 6, 9, 3, 3, 3, 8, 7, 10, 12, 7, 6, 6, 7,  7, 6, 5, 8, 9, 8, 8, 11, 9, 10, 3, 8, 8, 7, 7, 9, 8, 13, 9, 6, 8, 10,  10, 15, 11, 6, 8, 5, 11, 10, 7, 1, 10, 10, 8, 11, 8, 9, 10, 10, 9, 10, 11, 4, 12, 9, 12, 13, 8, 12, 9, 2, 6, 5, 6, 11, 13, 10, 14, 7,  13, 7, 9, 4, 8, 9, 8, 12, 11, 10, 8, 10, 10, 9, 11, 8, 8, 6, 11, 12, 9, , 11, 12, 2, 8, 8, 7, 8, 8, 6, 7, 4, 6, 11, 6, 10, 7, 9, 10,  8, 5, 5, 10, 7, 8, 7, 4, 8, 9, 4, 8, 8, 9, 8, 7, 12, 10, 10, 11, 10,  6, 11, 12, 8, 7, 8, 10, 7, 6, 8, 7, 6, 11, 8, 5, 10, 5, 4, 6, 7, 7,  5, 7, 6, 5, 6, 8, 8, 8, 7, 8, 8, 7, 7, 13, 7, 6


#### Time-series method search notes

Search keywords: "number series", "time series", "identification", "prediction"

-  Generalized Feature Extraction for Structural Pattern Recognition in Time-Series Data
   Robert T. Olszewski, February 2001 CMU-CS-01-108
   http://www.cs.cmu.edu/~bobski/pubs/tr01108-twosided.pdf

-  Chapter 1 - Pattern Recognition in Time Series
   Jessica Lin Sheri Williamson Kirk Borne David DeBarr
   http://cs.gmu.edu/~jessica/publications/astronomy11.pdf
   
-  Pattern recognition in time series - Stackoverflow
   http://stackoverflow.com/questions/11752727/pattern-recognition-in-time-series
   
-  Pattern Recognition and Classification for Multivariate Time Series
   Stephan Spiegel, Julia Gaebler, Andreas Lommatzsch Ernesto De Luca, Sahin Albayrak
   https://www.dai-labor.de/fileadmin/Files/Publikationen/Buchdatei/tsa.pdf
 
-  Pattern recognition with time series analysis
   http://stats.stackexchange.com/questions/117420/pattern-recognition-with-time-series-analysis   

-  PATTERN RECOGNITION IN TIME-SERIES
   By: Rick Martinelli, Haiku Laboratories, July 1995.
   http://www.haikulabs.com/pattrec.htm
   
-  Time Series Analysis and Order Prediction with R
   By ikocsis on October 31, 2011
   http://www.inside-r.org/howto/time-series-analysis-and-order-prediction-r

