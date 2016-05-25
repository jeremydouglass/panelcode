Panelcode
========================

**Panelcode** is a lightweight layout description language for concisely representing panel-based layouts and design grids. 

Panelcode strings concisely describe layouts. The format is optimized for rectangular panel regions, arranged in row-based groups, with rows containing columns of equal width. Here are some examples:

```Panelcode
	2_2           // simple row examples
	1_3_2_4
	1_2_3_4_5_6
	3x5           // grid shorthand
	2_3_3(1+r2,1) // rowgroups
	0_1_(0_1)     // zero panels
	2_2++3+3      // page-compositing
	2_3_2++       // page-compositing
```	


