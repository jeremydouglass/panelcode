# -*- coding: utf-8 -*-

# to run, from /panelcode-master:
#    python -m tests.test_basic

from .context import panelcode
import unittest

## SET THIS True OR False
use_thumbnails = False  # or False

## PASTE PANELCODE HERE -- IT WILL RENDER TO /output
panelcode_lines = """

# CHAPTER 1
3_3_1
2(c2+1)_3_3
3_3_1
3_2(1+c2)_3
3_3_3
(r2c4,0,4)  # Or 4_1 # Not (r2,4)
3_3_3
2(c2+1)_3_3
3_2(c2+1)_3
3_3_3
3_3_2(1+c2)
2(1+c2)_3_2(c2+1)
5(4, r2c4, 0)  # Or 4_1 # Not 5(4, r2)
1_3_2(1+c2)
3_3_3
3_3_3
2(1+c2)_3_3
4(3,r2c3,0) # 4(3, r2)
3_3_3
4(c2r3+1, 1, 1)
3_3_3
3_3_3
3_3_3
1_3_3 # missing
3_2(c2+1)_3
3_3_2(c5+1)

# CHAPTER 2
3_3_3
3_3_3
4(r2c3, 0, 3) # Not 4(r2, 3)
2(c2+1)_3_3
2(c2+1)_3_2(1+c2)
3_3_3
3_3_3
3_2(1+c2)_3
5(4, r2c4, 0) # Not 5(4, r2)
3_2(1+c2)_2(c2+1)
2(1+c2)_3_3
5(r2, 4)
1_3_2(c2+1)
3_3_3
2(1+c2)_3_3
4(3, r2)
2(1+c2)_3_1
3_3_3
3_3_3
3_3_1
3_3_3
3_3_3
3_3_3
3_3_3
1_3_3
1_3_3
3_3_1
3_3_2(c5+1)

# CHAPTER 3
4(3, r2)
3_3_3
3_3_3
3_1_3
3_3_3
2(1+c2)_2(1+c2)_2(1+c2) # 3x2(1+c2)
2(1+c2)_2(1+c2)_2(1+c2) # 3x2(1+c2)
3_3_3
3_3_3
3_3_3
2(1+c2)_2(c2+1)_2(1+c2)
2(1+c2)_2(c2+1)_2(1+c2)
2(1+c2)_2(c2+1)_2(1+c2)
2(1+c2)_2(c2+1)_2(1+c2)
2(1+c2)_2(c2+1)_2(1+c2)
2(1+c2)_2(c2+1)_2(1+c2)
3_3_3
2(1+c2)_2(c2+1)_3
2(1+c2)_2(c2+1)_3 
3_3_3
3_1_3
2(1+c2)_3_2(c2+1)
2(1+c2)_1_3
3_3_3
3_3_3
2(1+c2)_2(c2+1)_2(1+c2)
2(c2+1)_2(1+c2)_2(c2+1)
4(3, r2)

# CHAPTER 4
3_3_3
3_3_1
3_3_3
2(c2+1)_2(c2+1)_2(c2+1) # 3x2(c2+1)
3_1_3
3_3_3
3_3_3
4(3, r2)
3_1_3
3_2(c2r2+r2)
 3_3_3
3_3_3
3_3_3
1_1_1
3_2(1+c2)_2(c2+1)
3_3_3
2(c2+1)_3_3
2(1+c2)_2(c2+1)_2(1+c2)
3_1_2(c2+1)
4(c2r3+1, 1, 1)
2(1+c2)_2(c2+1)_2(1+c2)
3_2(c2+1)_1
3x2(c2+1)
3_2(c2+1)_3
3_2(c2+1)_3
3_1_1
1_1_1
1_2_2(c5+1)

# CHAPTER 5
3_3_3
3_3_3
3_3_3
1_3_3
2(c2+1)_3_3
3_2(1+c2)_2(c2+1)
3_3_3
3_3_3
2(c2+1)_2(1+c2)_2(c2+1)
3_1_3
3_3_3
3_3_3
2(1+c2)_3_3
4(c2+r3, c2, c2)
4(r3+c2, c2, c2)
2(c2+1)_3_3
3_3_3
3_3_3
3_1_3
2(1+c2)_2(c2+1)_2(1+c2)
3_3_3
3_3_3
3_2(c2+1)_2(1+c2)
2(1+c2)_3_3
1_3_3
3_3_3
3_3_3
3_3_4(r3+r3+r2, 1)

# CHAPTER 6
3_3_3
1_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
1_3_3
3_3_3
3_3_3
1_3_1
3_3_3
3_3_3
3x2(1+c2)
1_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
1_3_1
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3(c2+c3+1)

# CHAPTER 7
3_3_3
3_3_1
3_3_1
3_3_3
3_3_3
3_3_3
3_3_2(1+c2)
2(1+c2)_2(c2+1)_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
6_6_5(5+c2)3_4(c2+2+c2)_3
3_3_3
2(1+c2)_3_3
3_3_3
3_3_1
3_3_1
4(r2, 3)
2(1+c2)_2(c2+1)_3
3_3_1
3_2(c2+1)_3
6_6_1
3_3_4(r3+r3+r2, 1)

# CHAPTER 8
3_3_3
3_3_1
3_3_3
6(3r2, 3)
6(3, 3r2)
3_3_3
3_3_1
3_3_3
3_3_3
3_3_1
3_3_1
3_3_1
3_3_1
3_3_1
3_3_1
4(r2, 3)
3_3_3
3_3_3
3_3_3
3_3_1
3_3_1
3_3_3
3_3_3
3_3_1
3_3_1
3_3_1
3_3_3
3_3_2(c5+1)

# CHAPTER 9
3_1_1
1_1_3
3_3_3
4(3, r2)
3_3(c2r2+1, 1)
3_3_3
3_3_3
3_3_3
4(3, r2)
7(r3+1+1, 1+1, 1+1)
3_3_3
3_3_3
3_1_3
4(r2, 3)
3_3_3
3_3_3
1_1_1
1_1_1
4(r2, 3)
3_3_3
3_3_3
4(r2, 3)
3_3_3
3_1_3
4(3r2, 1)
3_1_1
1_1_1
1_1_2(c5+1)

# CHAPTER 10
4(3, r2) 
3_3_3
1_3_1
4(3, r2)
3_1_3
3_3_3
3_1_3
1_3_1
3_3_1
3_3_3
4(3, r2)
3_3_3
3_3_3
3_3_3
3_3_3
3_3_3
1_3_3
3_1_3
3_1_3
3_3_3
3_1_3
7(r3+1+1, 2, 2)
3_3_3
3_3_3
1_3_1
4(3, r2)
3_3_3
3_3_2(c5+1)

# CHAPTER 11
3_3_1
3_1_3
3_3_1
5(3, r2+c2r2)
3_3_3
3_3_3
3(c3r2, 0, c2+1)
3_3_3
3_3_3
3_1_3
3_1_3
3_1_3
3_3_3
3_1_3
3_1_3
3_3_1
3_3_1
3_3_3
3_3_3
3_3_3
3_1_3
3_1_3
3_3_3
3_3_1
3_3_1
3_2(c2+1)_1
1_1_1
6_6_2(c5+1)

# CHAPTER 12
1 # 6_1_1
1
1
1
1
1
1_1_1
3_3_3
3_1_3
3_3_3
3_1_3
3_1_1
1_3_1
5(3, c2r2+r2)
3_1_3
3_1_3
4(3, r2)
1_3_1
3_3_1
3_3_3
3_1_3
3_3_1
1_3_3
3_1_1
3_2(c2+1)_1
3_3_1
3_3_1
1_3_3
3_3_3
3_3_1
1_3_3
3_3_2(c5+1)
"""

panelcode_lines_99 = """
# 99 Ways to Tell a Story
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 2_3_2
0; 3_3_2
0; 2_2_2
0; 3_3_2
0; 3_3_2
0; 6(c4, 4r2, 0, 1+c3) # Or 1_4_2(1+c3) # Not 6(c4, 4r2, 1+c3)
0; 3_3_2
0; 3_3_2
0; 2_3_3
0; 3_3_3
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 1
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 1
0; 5_5_5_5_5_5
0; 3_3_2
0; 3_3_3~
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_3_3_3
0; 2_3_3
0; 3_3_2
0; 3_3_2
0; 1_1_1
0; 1
0; 3_3_3
0; 11(3, 2+r2, 2, 3)
0; 3_3_2
0; 3_6(c4+5)_2
0; 1
0; 3_3_2
0; 2_2_2_2
0; 2_2_2_1
0; 2_2_1
0; 1_1_1_1_1_1
0; 3_3_2
0; 3_3_3_2
0; 3_3_2
0; 3_3_2
0; 1
0; 1
0; 1_2_2_2_2
0; 2_2_2
0; 3_3_2
0; 1
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 1_1_1_1_1_1_1_1
0; 8
0; 3_3_2
0; 2_2_2
0; 3_3_2
0; 2_2_2_2
0; 2_2_2
0; 1~
0; 3_3_2;*
0; 3_3_2
0; 3_3_2
0; 1~
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
0; 3_3_2
"""

panelcode_lines_understanding = """

# Table of Contents
12(r11+1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

# Introduction
3_3_3

# Ch. 1
1_2(c3+1)_3(2+c2); 6(r2+c2+1, 3)_3(1+c2+1); 3(c3r3+1, 1, 1); 2(c3+1)_4(r2+c2r2+1, 1); 3(c2+1+1_4_2(c3+1); 2_3(1+c2+1)_2(1+c3); 7(r3+c2+1, c2+1, 1+c2); 3(c2+2)_3(1+c2+1)_3(c2+2); 1_1_1; ; 3(2+c2)_2_3(2+c2); 1_2(c3+1)_2; 1_2_2(c3+1); 3(c4r2, 1+c3); 4_3(2+c2)_4; 4(c3r2+1, 1, c4); 1_2(1+c3)_4; 1_2(1+c3)_2(1+c3); 2(1, r2); 3(r2+c3, c3)_3(c2+2); 3(2+c2)_3(1+c2+1)_2; 1_1_1; 4(r2+c2+1, c3)_4

# Ch. 2
1_2_2; 2_2_2; 18~; 6(1+c2+1, 2r2+c2r2); 2_3(c2+2)_2(1+c3); 1_1_1; 1_2_2(1+c3); 3(1+c2+1)_2(c3+1)_3(c2+2); 3(1+c2+1)_3(c2+2)_1; 1_1_1; 2(c3+1)_4_3(1+c2+1); 4_4_2(1+c3); 2(c3+1)_3(2+c2)_4; 4_4_2(c3+1); 2_2_2; 4_3(1+c2+1)_2; 2(c3+1)_3(1+c2+1)_4; 3(1+c2+1)_2(1+c3)_4; 2_2_2; 2(c3+1)_3(2+c2)_3(c2+2); 3(c2+2)_4_3(1+c2+1); 2_3(1+c2+1)_2(1+c3); 1_2(c3+1)_2; 4_4_4; 3(c2+2)_4_1; 2_1_4; 1_2_2; 5(r2, 4); ~; ~; 3(2+c2)_3(c2+2)_1; 1_1_1; 1_2(c3+1)_2; 3(c2+1)_2(1+c3)_1; 1i(1); 2_3(1+c2+1)_4

# Ch. 3
1_1_1; 1_3(c2+2)_4; 1_1_1; 2_2_2; 1_2_4; 2(1+c3)_2(c3+1)_2(1+c3); 2(2+0)_1_1; 1_1_1;  2_1_3(1+c2+1); 2(1+c3)_2_2(c3+1); 2; 2; 2; 4_4_4; 4(c2r2+c2, 1, 1)_2; 3(c2+2)_3(c2+2)_1; 1_2(c3+1)_2(1+c3); 6(c3+1, c2r2+1+1, c2); 2(1+c3)_2(c3+1)_1; ~; 1_2_3(2+c2); 4(c2r2+c2, 2)_3(3+0); 2(0+1+c2)_2_2; 3(1+c2+1)_2_2; 11(r2+5, 5)_6_6_6_6_6_6_6; 16(r2+3+r2+1, 4, 6)_2_2; 2_2_4; 2_2_2; 4_2_2(1+c3); 2(c3+1)_2(c3+1)_2(1+c3); 1_1_2; 1_2_2

# Ch. 4
1_4_3(2+c2); 1_4_1; 1_2_3(1+c2+1); 3(1+c2+1)_2_2(1+c3); 4_4_3(2+c2); 4(r2+r2+c2, c2)_2(c3+1); 1_3(1+c2+1)_2(c3+1); 1_2(c3+1)_1; 2(c3+1)_2(1+c3)_4; 5(r2+r2+c2r2, c3+1); 3(0+3)_4_3(c2+2)~; 26(5+0, r4+1+c3+1, 5, 1+0+1+0+1; 5, 2+0+1+0+1)_3(1+1+c2)~; 5(c4r2, 4); 2_7(6+c2)_2; 1_3(1+c2+1)_2(c3+1); 1_4_3(c2+2); 3(1+c2+1)_4_3(2+c2); 1_2_1; 1_3(r2+c3, c3); 2_2(c3+1)_2(1+c3); 2(r2, 1); 4_4_3(1+c2+1); 1_3(1+c2+1)_2; 2_2_2(c2+2)

# Ch. 5
1_2(1+c3)_2; 3(r2+c3, c3)_2; 2_3(1+c2+1)_2; 1_2(c3+1)_3(c2+2); 4(c2r2+1+1, 0+1)_3(c2_2)~; 2(c3+1)_2_3(2+c2); 2_1_3(2+c2); 4_4_2(1+c2+1); 4_4_4; 2_2(c3+1)_4; 4_3(1+c2+1)_3(c2+2); 3(c2+2)_4_4; 4_3(c2+2)_3(2+c2); 3(1+c2+1)_4_2(1+c3); 2_2_2; 1_2_2; 2(c3+1)_2_2(c3+1); 2_2_3(c2+2) 

# Ch. 6
1_4_4; 4_4_2(c3+1); 1_1_4; 2_2(1+c3)_2; 8(r4+r4+c2+c2+r3+r3, c4r2, c6)_1_2; 1_4(c2r2+c2, 2); 4(c2r2+c2, 2)_1; 2(r2, 1); 2(c3+1)_2_2; 2_4(c2r2+2, c2); 4(2r2, 2); 2_1_4; 1_2(c3+1)_1; 2_2_2; 3(c2+2)_2(c3+1)_3(c2+2); 2(1+c3)_ 2(1+c3)_ 2(1+c3); 2(1+c3)_ 2(1+c3)_ 2(1+c3); 3(r2+c3r2, 1); 2_2_2; 3(2, c2r2); 1_2_2; 3(2, c2r2); 2(c3+1)_2_2; 2(c3+1)_2_3(2+c2) 

# Ch. 7 
37(c6r3, 6, 6, 6, 6, 6, 6)~; 2_2_2; 1_3(2+c2)_3(c2+2); 3(c2+2)_4_1; 3(c2+2)_4_3(c2+2); 4_3(c2+2)_2; 4_3(c2+1)_3(c2+2); 2_3(2+c2)_2; 6_2_2~; 2_2_4; 3(c2r2, 2); 2_2_2; 2_2_2; 2_2_2; 2_2_2; 2_2_2; 1_2_2; 2_1_2; 1_2_2; 1_2_2; 6_2_2; 2_2_2; 3(c4, r2+c3r2)

# Ch. 8
1_3(c2+2)_4; 1_3(2+c2)_3(c2+2); 3(c2+2)_3(c2+2)_3(2+c2); 1_4_4; 2(1+c3)_3(c2+2)_3(2+c2); 2(c3+1)_3(1+c2+1)_4; 5(c2r2+2, 2)_3(2+c2); 4_3(1+c2+1)_3(1+1+c2)

# Ch. 9
2(1, r2); 4(r3+1, 1, 1); 2_1_1; 2(c3+1)_3(1+c2+1)_2; 2_2_1~; 1_1_2; 3(r2+1, 1)_2; 1; 3(2, c2r2); 2(r2, 1); 1~; 2(r2, 1); 2(r2, 1); 1~; 3(r3+r2, 1); 2(r2, 1); 1~, 1~; 4(2c2r2, c3+1); 2(r2, 1); 1_1_1; 1; 3(c2+2)_4_2(c3+1)
"""

## PASTE IMAGE THUMBNAILS HERE, ONE PER CODE LINE
## IT MUST BE FOUND IN /input
image_lines = """watchmen_006.jpg
watchmen_007.jpg
watchmen_008.jpg
watchmen_009.jpg
watchmen_010.jpg
watchmen_011.jpg
watchmen_012.jpg
watchmen_013.jpg
watchmen_014.jpg
watchmen_015.jpg
watchmen_016.jpg
watchmen_017.jpg
watchmen_018.jpg
watchmen_019.jpg
watchmen_020.jpg
watchmen_021.jpg
watchmen_022.jpg
watchmen_023.jpg
watchmen_024.jpg
watchmen_025.jpg
watchmen_026.jpg
watchmen_027.jpg
watchmen_028.jpg
watchmen_029.jpg
watchmen_030.jpg
watchmen_031.jpg
watchmen_040.jpg
watchmen_041.jpg
watchmen_042.jpg
watchmen_043.jpg
watchmen_044.jpg
watchmen_045.jpg
watchmen_046.jpg
watchmen_047.jpg
watchmen_048.jpg
watchmen_049.jpg
watchmen_050.jpg
watchmen_051.jpg
watchmen_052.jpg
watchmen_053.jpg
watchmen_054.jpg
watchmen_055.jpg
watchmen_056.jpg
watchmen_057.jpg
watchmen_058.jpg
watchmen_059.jpg
watchmen_060.jpg
watchmen_061.jpg
watchmen_062.jpg
watchmen_063.jpg
watchmen_064.jpg
watchmen_065.jpg
watchmen_066.jpg
watchmen_067.jpg
watchmen_074.jpg
watchmen_075.jpg
watchmen_076.jpg
watchmen_077.jpg
watchmen_078.jpg
watchmen_079.jpg
watchmen_080.jpg
watchmen_081.jpg
watchmen_082.jpg
watchmen_083.jpg
watchmen_084.jpg
watchmen_085.jpg
watchmen_086.jpg
watchmen_087.jpg
watchmen_088.jpg
watchmen_089.jpg
watchmen_090.jpg
watchmen_091.jpg
watchmen_092.jpg
watchmen_093.jpg
watchmen_094.jpg
watchmen_095.jpg
watchmen_096.jpg
watchmen_097.jpg
watchmen_098.jpg
watchmen_099.jpg
watchmen_100.jpg
watchmen_101.jpg
watchmen_108.jpg
watchmen_109.jpg
watchmen_110.jpg
watchmen_111.jpg
watchmen_112.jpg
watchmen_113.jpg
watchmen_114.jpg
watchmen_115.jpg
watchmen_116.jpg
watchmen_117.jpg
watchmen_118.jpg
watchmen_119.jpg
watchmen_120.jpg
watchmen_121.jpg
watchmen_122.jpg
watchmen_123.jpg
watchmen_124.jpg
watchmen_125.jpg
watchmen_126.jpg
watchmen_127.jpg
watchmen_128.jpg
watchmen_129.jpg
watchmen_130.jpg
watchmen_131.jpg
watchmen_132.jpg
watchmen_133.jpg
watchmen_134.jpg
watchmen_135.jpg
watchmen_143.jpg
watchmen_144.jpg
watchmen_145.jpg
watchmen_146.jpg
watchmen_147.jpg
watchmen_148.jpg
watchmen_149.jpg
watchmen_150.jpg
watchmen_151.jpg
watchmen_152.jpg
watchmen_153.jpg
watchmen_154.jpg
watchmen_155.jpg
watchmen_156.jpg
watchmen_157.jpg
watchmen_158.jpg
watchmen_159.jpg
watchmen_160.jpg
watchmen_161.jpg
watchmen_162.jpg
watchmen_163.jpg
watchmen_164.jpg
watchmen_165.jpg
watchmen_166.jpg
watchmen_167.jpg
watchmen_168.jpg
watchmen_169.jpg
watchmen_177.jpg
watchmen_178.jpg
watchmen_179.jpg
watchmen_180.jpg
watchmen_181.jpg
watchmen_182.jpg
watchmen_183.jpg
watchmen_184.jpg
watchmen_185.jpg
watchmen_186.jpg
watchmen_187.jpg
watchmen_188.jpg
watchmen_189.jpg
watchmen_190.jpg
watchmen_191.jpg
watchmen_192.jpg
watchmen_193.jpg
watchmen_194.jpg
watchmen_195.jpg
watchmen_196.jpg
watchmen_197.jpg
watchmen_198.jpg
watchmen_199.jpg
watchmen_200.jpg
watchmen_201.jpg
watchmen_202.jpg
watchmen_203.jpg
watchmen_210.jpg
watchmen_211.jpg
watchmen_212.jpg
watchmen_213.jpg
watchmen_214.jpg
watchmen_215.jpg
watchmen_216.jpg
watchmen_217.jpg
watchmen_218.jpg
watchmen_219.jpg
watchmen_220.jpg
watchmen_221.jpg
watchmen_222.jpg
watchmen_223.jpg
watchmen_224.jpg
watchmen_225.jpg
watchmen_226.jpg
watchmen_227.jpg
watchmen_228.jpg
watchmen_229.jpg
watchmen_230.jpg
watchmen_231.jpg
watchmen_232.jpg
watchmen_233.jpg
watchmen_234.jpg
watchmen_235.jpg
watchmen_236.jpg
watchmen_237.jpg
watchmen_245.jpg
watchmen_246.jpg
watchmen_247.jpg
watchmen_248.jpg
watchmen_249.jpg
watchmen_250.jpg
watchmen_251.jpg
watchmen_252.jpg
watchmen_253.jpg
watchmen_254.jpg
watchmen_255.jpg
watchmen_256.jpg
watchmen_257.jpg
watchmen_258.jpg
watchmen_259.jpg
watchmen_260.jpg
watchmen_261.jpg
watchmen_262.jpg
watchmen_263.jpg
watchmen_264.jpg
watchmen_265.jpg
watchmen_266.jpg
watchmen_267.jpg
watchmen_268.jpg
watchmen_269.jpg
watchmen_270.jpg
watchmen_271.jpg
watchmen_278.jpg
watchmen_279.jpg
watchmen_280.jpg
watchmen_281.jpg
watchmen_282.jpg
watchmen_283.jpg
watchmen_284.jpg
watchmen_285.jpg
watchmen_286.jpg
watchmen_287.jpg
watchmen_288.jpg
watchmen_289.jpg
watchmen_290.jpg
watchmen_291.jpg
watchmen_292.jpg
watchmen_293.jpg
watchmen_294.jpg
watchmen_295.jpg
watchmen_296.jpg
watchmen_297.jpg
watchmen_298.jpg
watchmen_299.jpg
watchmen_300.jpg
watchmen_301.jpg
watchmen_302.jpg
watchmen_303.jpg
watchmen_304.jpg
watchmen_305.jpg
watchmen_312.jpg
watchmen_313.jpg
watchmen_314.jpg
watchmen_315.jpg
watchmen_316.jpg
watchmen_317.jpg
watchmen_318.jpg
watchmen_319.jpg
watchmen_320.jpg
watchmen_321.jpg
watchmen_322.jpg
watchmen_323.jpg
watchmen_324.jpg
watchmen_325.jpg
watchmen_326.jpg
watchmen_327.jpg
watchmen_328.jpg
watchmen_329.jpg
watchmen_330.jpg
watchmen_331.jpg
watchmen_332.jpg
watchmen_333.jpg
watchmen_334.jpg
watchmen_335.jpg
watchmen_336.jpg
watchmen_337.jpg
watchmen_338.jpg
watchmen_339.jpg
watchmen_346.jpg
watchmen_347.jpg
watchmen_348.jpg
watchmen_349.jpg
watchmen_350.jpg
watchmen_351.jpg
watchmen_352.jpg
watchmen_353.jpg
watchmen_354.jpg
watchmen_355.jpg
watchmen_356.jpg
watchmen_357.jpg
watchmen_358.jpg
watchmen_359.jpg
watchmen_360.jpg
watchmen_361.jpg
watchmen_362.jpg
watchmen_363.jpg
watchmen_364.jpg
watchmen_365.jpg
watchmen_366.jpg
watchmen_367.jpg
watchmen_368.jpg
watchmen_369.jpg
watchmen_370.jpg
watchmen_371.jpg
watchmen_372.jpg
watchmen_373.jpg
watchmen_380.jpg
watchmen_381.jpg
watchmen_382.jpg
watchmen_383.jpg
watchmen_384.jpg
watchmen_385.jpg
watchmen_386.jpg
watchmen_387.jpg
watchmen_388.jpg
watchmen_389.jpg
watchmen_390.jpg
watchmen_391.jpg
watchmen_392.jpg
watchmen_393.jpg
watchmen_394.jpg
watchmen_395.jpg
watchmen_396.jpg
watchmen_397.jpg
watchmen_398.jpg
watchmen_399.jpg
watchmen_400.jpg
watchmen_401.jpg
watchmen_402.jpg
watchmen_403.jpg
watchmen_404.jpg
watchmen_405.jpg
watchmen_406.jpg
watchmen_407.jpg
watchmen_408.jpg
watchmen_409.jpg
watchmen_410.jpg
watchmen_411.jpg
"""


















# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------

panelcode_test_string = """
1
2
2_2
2_3
2_3_2
2_3_5

1_3_2_4
1_2_3_4_5_6
3_3_3_3_3
2_5_1_3_2
2_2_2_1_1_2_1

3
3_3
3_3_3

33
333
25132

0
0_0_0
0_2_0
0_3_0


00
03
30
303

3()
3()3()
3()3()3()

33()
3()3

3++3
3++3++3
3,,3
3,,3,,3

3++3;3,,3
3_3;3_3

2_(1,0)
2_(1+0)
2_2++3_3
2_3_3(1+r2,1)
2_5(1+r2+r2+r2,1)_4(r2+r2+1,1)
3(r2+0,1)
3(r2+1,1)
3_3_3++2_5(r2+2,2)
4(r3+1,1,1)
4(1+r3,1,1)
5(1+r2+1,2)
5(r2+1+r2,1)
5(r2+2,2)
5(2+r2,2)

2(c2+1)
2(1+c2)
3(c2+2)
3(2+c2)
2(c2+1)
2(1+c2)
3(c2+2)
3(2+c2)
3(1+c2+1)
3(c2+1+c2)
4(c2+3)
4(3+c2)
4(1+c2+c2+1)
4(c2+2+c2)
5(c2+4)
5(4+c2)
5(1+c3+1)
5(c2+3+c2)

0_(2+0+2)_0
0_1_(0+1)
0_1_(1+0)

3C
3D

3\n3
3\n\n\n3

3;3
3;3;

3_
_3

3 3

3++3(),,3
3++(),,3

()
()_()
()()

~
(~)
(~)_(~)
(~)(~)

3_(~)_3
(~)_3_(~)

(~)++(~)
(~),,(~)
(~);(~)
"""

bad_strings = """
3(
3)
3;
;3

3(\n)3()

(())
((~))
"""

panelcode_test_string_3 = """3x5            # grid shorthand
	0_1_(0_1)      # zero panels
	2_3_2++        # page-compositing
	2_2++3+3       #"""

verbose = 1
# quick verbose printing hack, as per http://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script
if verbose:
    def vprint(*args):
        for arg in args:
           # print 'vprint: ',
           print arg,
        print
else:   
    vprint = lambda *a: None      # do-nothing function

def old_preparse(pstr):
    pstr = pstr.replace("~", "0") # replace uncoded page markers as empty pages
    pstr = pstr.replace(";", "\n") # split pages into lines
    return pstr

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_app_batch_svg(self):
        test_strings  = [ panelcode_lines_understanding
                        ]
        # test_strings  = [ maite_string_ch1
        #                , maite_string_ch2
        #                , maite_string_ch3
        #                , maite_string_ch4
        #                , maite_string_ch5
        #                , maite_string_ch6
        #                , maite_string_ch7
        #                , maite_string_ch8
        #                , maite_string_ch9
        #                , maite_string_ch10
        #                , maite_string_ch11
        #                , maite_string_ch12
        #                ]
        
        thumbfilelist  = [ image_lines
                         ]
        # tests = zip(test_strings)
        # for test in test_strings:
            # test_string = test[0]
        for test_string in test_strings:
            # test_string = panelcode.pstr_clean(panelcode_test_string) # strip all kinds of bad behavior
            test_string = old_preparse(test_string)
            ## this function needs to be replaced with pyparser output,
            ## but temporarily cleaning the input in-place during testing

            if use_thumbnails:
                ## RUN THIS FOR PANELCODE PLUS THUMBNAILS
                panelcode.app_batch_svg(test_string, thumbfilelist[0].split('\n'))
            else:
                ## RUN THIS FOR JUST PANELCODE IMAGES
                panelcode.app_batch_svg(test_string)

        #for test_string in test_strings:
        #    print(test_string)
        
        assert True

    @unittest.skip("maite testing")
    def test_pstr_rowcount(self):
        self.assertEqual(panelcode.pstr_rowcount('1'), 1)
        self.assertEqual(panelcode.pstr_rowcount('3'), 1)
        self.assertEqual(panelcode.pstr_rowcount('3_3'), 2)
        self.assertEqual(panelcode.pstr_rowcount('1_2_3_4_5'), 5)        

        # self.assertEqual(panelcode.pstr_rowcount('(~)'), 1)        
        self.assertEqual(panelcode.pstr_rowcount('3,,3'), 1) # should this be 1 row, or 2 rows? or just throw an error if passed a pagegroup?
        self.assertEqual(panelcode.pstr_rowcount('3++3'), 1)

###  currently already cascade tested by test_app_batch_svg
#    def test_app_svg_preview_page(self):
#        panelcode.app_svg_preview_page(svg_file_list,'script/output/','index.html')
#        assert True

class CleanTestSuite(unittest.TestCase):
    """Clean test cases."""

    @unittest.skip("maite testing")
    def test_pstr_clean(self):
        self.assertTrue('#' not in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))

        # note that clean DOES NOT do page decompositing
        self.assertTrue('++' in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))
        self.assertTrue(',,' in panelcode.pstr_clean('1_2++3_4,,5 ### comment'))

    @unittest.skip("maite testing")
    def test_pstr_strip_comments(self):
        self.assertTrue('#' not in panelcode.pstr_strip_comments('1++2'))
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 #comment') ,'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 # comment'),'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('1_2_3 # comment #comment'),'1_2_3')
        self.assertEqual(panelcode.pstr_strip_comments('#comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('# comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('#### comment'),'')
        self.assertEqual(panelcode.pstr_strip_comments('############'),'')

    @unittest.skip("maite testing")
    def test_pstr_decomposite_pages(self):
        """Test that horizontal and vertical pagegroups break down correctly."""
        self.assertTrue('++' not in panelcode.pstr_decomposite_pages('1_2_3++4_5_6'))
        self.assertTrue(',,' not in panelcode.pstr_decomposite_pages('1_2_3,,4_5_6'))        
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1++2').split('\n'))==2)
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1,,2_3,,3').split('\n'))==3)
        self.assertTrue(len(panelcode.pstr_decomposite_pages('1++2,,3_4++5').split('\n'))==4)

    @unittest.skip("maite testing")
    def test_pstr_minify (self):
        result = panelcode.pstr_minify(panelcode_test_string)
        vprint('Minified: ' + result)
        self.assertTrue('\n' not in result)
        self.assertTrue('\r' not in result)

class ParseTestSuite(unittest.TestCase):
    """Parser test cases."""

#    def test_parse_example (self):
#        self.assertEqual(panelcode.parse_example("x=2+2")[0], 'x')
#        self.assertEqual(panelcode.parse_example("x=2+2")[1], '=')
#        self.assertEqual(panelcode.parse_example("x=2+2")[2], '2')
#        self.assertEqual(panelcode.parse_example("x=2+2")[3], '+')
#        self.assertEqual(panelcode.parse_example("x=2+2")[4], '2')
        
    @unittest.skip("maite testing")
    def test_parse_panelcode (self):
        vprint("\n\n-----TEST parse_panelcode-----\n")
        test_string = panelcode.pstr_clean(panelcode_test_string)
        test_string = panelcode_test_string.split()
        vprint(test_string)
        for s in test_string:
            vprint("\n           In:  " + str(s))
            vprint("--------------  -----------------")
            try:  
                result = panelcode.parse_panelcode(s)
                self.assertTrue(len(result)>0) # returns parsed objects, not nothing
                vprint("   ...matches:  {0}".format(result))
                vprint("   ...as Dict:  " + str(result.asDict()))
                try:
                    vprint("['panelcode']: ", result['panelcode'])
                    vprint("['pagegroup']: ", result['panelcode']['pagegroup'])
                    vprint("     ['page']: ", result['panelcode']['pagegroup']['page'])
                    vprint("     ['rows']:", result['panelcode']['pagegroup']['page']['rows'])
                except: ## some pages have no rows -- empty an uncoded. could force them to have rows. might help for css and html / svg rendering.
                    pass              
            except panelcode.pp.ParseException as x:
                vprint("    ...except:  ParseException")
                # print "...ParseException: {0}".format(str(x)) + '\n'
                pass

if __name__ == '__main__':
    unittest.main()