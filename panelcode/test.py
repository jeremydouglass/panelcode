
t_row      = ['3','2','3','10']
t_cols     = ['1_2', '3_4_5']
t_plus     = ['1+2', '3+4+5']
t_colplus  = ['1_2+3', '4+5_6+7']
t_layouts  = ['1;2', '3;4;5']
t_lcols    = ['1_2;3_4', '1;2_3;4_5_6']
t_lplus    = ['1+2;3+4', '1;2+3;4+5+6']
t_lcolplus = ['1_2;3+4', '1;2_3;4+5_6']
t_spreads  = ['1|2', '3|4|5']
t_scols    = ['1_2|3_4|5']
t_splus    = ['1+2|3+4|5'] # ugh
t_scolplus = ['1+2_3|4_5+6']
t_slayouts = ['1|2;3', '1|2;3|4']
t_slcols   = ['1;2_3|4;5_6']
t_slplus   = ['1;2+3|4;5+6']
t_slcolplus =['1;2_3|4;5+6']

t_basics_rows_and_columns = ['1 ; 2|3 ; 1_1|1_1_1 ; 1_2|1_2_3|4_3_2_1|6_5_4_3_2_1 ; 2_2|3_3_3 {::: mini} @ 8_8_8_8_8_8_8_8 {:: small }']
t_reading       = ['c3.grayC + c1.grayB _ c2.grayA + c2.gray9 _ c1.gray8 + c3.gray7', '(c3.grayC + c1.grayB , c2.grayA + c2.gray9 , c1.gray8 + c3.gray7){: comicstrip-sunday-half w4}', '(c3.grayC + c1.grayB , c2.grayA + c2.gray9 , c1.gray8 + c3.gray7){: comicbook-us w4}',]
t_reading2      = ['c3+1_2_1+c3', '(c3+c1+c2+c2+c1+c3){: w4}', '(c3+c1+c2+c2+c1+c3){: comicstrip-sunday-half}', '(c3+c1+c2+c2+c1+c3){: comicstrip-sunday-half w4}', '(c3+c1, c2+c2, c1+c3){: comicstrip-sunday-half}', 'c3.grayC + c1.grayB , c2.grayA + c2.gray9 , c1.gray8 + c3.gray7', '(c3+c1, c2+c2, c1+c3)', '(c3+c1+c2+c2+c1+c3){: w3}', '(c3+c1+c2+c2+c1+c3){: w4}', '(c3+c1+c2+c2+c1+c3){: w6}'] # 'c3.gC + 1.gB _ 1.gA + 1.g9 _ 1.g8 + c3.g7'
t_spans_columns = ['2; (1+c2); (c2+1); 2_2; (1+c3)_(c3+1); (c3+1)_(1+c3) {::: small }']
t_spans_rows    = ['(r2+1,1)|(1+r2,1) ; 1_2|2_1 ; (r2+1,1)|(1+r2,1)|1_2|2_1 ; (c2.r2+1,1) {::: small }']
t_sizes         = ['1_2_3 ; 1_2_3{: small} ; 1_2_3{: thumb}; 1_2_3{: mini}; 1_2_3{: micro}; 1_2_3{: micro2}']
t_sizes_full    = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3']
t_sizes_small   = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: small }']
t_sizes_thumb   = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: thumb }']
t_sizes_mini    = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: mini }']
t_sizes_micro   = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: micro }']  # micro  always embedded in spreads -- look better outside
t_sizes_micro2  = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: micro2 }'] # micro2 always embedded in spreads -- look better outside

t_zeros_not_right           = ['0'] # panel omitted instead of special-cased
t_sizes_full_empty_error    = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {::: }'] # opts with no args creates index error
t_sizes_small_pcode_ignored = ['0 ; 1 ; 1_2 ; 2_2; 1_2_3; 3_3_3 {:::: small }'] # pcode-level opts aren't passed down by the htmlcss3 renderer

t_spreads       = ['0|1|1_2|2_2 {:: thumb} ; 0|1|1_2|2_2 {:: mini} @ 1_2_3|3_3_3 {:: thumb} ; 1_2_3|3_3_3 {:: mini}']
t_sequences_and_sorting = ['0 ; 1 ; 2 ; 3 ; 1_1 ; 1_2 ; 1_3 ; 2_1 ; 2_2 ; 2_3',
                           '3_1 ; 3_2 ; 3_3 ; 1_1_1 ; 1_1_2 ; 1_1_3 ; 1_2_1 ; 1_2_2 ; 1_2_3 ; 1_3_1',
                           '1_3_2 ; 1_3_3 ; 2_1_1 ; 2_1_2 ; 2_1_3 ; 2_2_1 ; 2_2_2 ; 2_2_3 ; 2_3_1 ; 2_3_2',
                           '2_3_3 ; 3_1_1 ; 3_1_2 ; 3_1_3 ; 3_2_1 ; 3_2_2 ; 3_2_3 ; 3_3_1 ; 3_3_2 ; 3_3_3']

t_blanks = [' 0 ; 1_0 | 0_(1+0c2, c2+0, 1+c2) {::: small}',
            '1x ; 1_x | 1x_(1+2x, 1c2+1x, 1+c2) {::: small}',
            '1z ; 1_z | 1z_(1+z.c2, c2+z, 1+c2) {::: small}']

t_blanks_gallery = ['0 ; 0+1 ; 0+0+1 ; 0_1 ; 1_(0+1) ; 0_(0+2) ; (1+0)_1 ; (1+0)_(0+1) ; (1+0)_(1+0+1) {::: thumb}',
                    '(2+0)_1 ; (2+0)_(0+1) ; (1+0+0)_(2+0) ; 0_1_0 ; 0_1_2 ; 1_0_(1+0+1) ; 1_2_0 ; 0_(0+1)_2 ; 1_(1+0)_(1+0+0) ; 0_(0+1+0)_0 {::: thumb}',
                    '1_3_(0+1) ; 1_1+0+1_3 ; 1+0_1_0 ; 0+1_1_0+1 ; 1+0_0_0+2 ; 1+0_0+1_1 ; 1+0_1+0_0+1 ; 2_2_0+2 ; 1+0_3_1 ; 1+0_2+0_1+0 ; 2_0+2_0+0+1 {::: thumb}',
                    '0+1+0_1_1 ; (2+0)_1_(1+0) ; 3_0_3 ; 1+0+0_0+1_0+1 ; 3_(0+1)_(1+0) ; (1+0+0)_(1+0)_3 ; 3_(0+1+0)_1 ; (0+1+0)_(0+1+0)_2 ; (1+0+1)_(0+1+0)_(1+0+1) {::: thumb}']

t_unencoded = ['1+u', '1+c2,x+u0+u4.r2,c2']

t_shape_scale = ['scale-125 + scale-50, scale-50 + scale-125 | 3 _ 1 + scale-200 + 1 _ 3']
t_shape_skew  = ['2_2 {: skew-fwd} | 3_3_3 {: skew-back} | 2+r2.skew-back, c2.skew-fwd _ skew-back + skew-fwd + skew-back']
t_shape_tilt  = ['1+c2,c2+1 {: tilt-up} ; 3_3_3 {: tilt-down}', '3{tilt-up} _ 3{tilt-down} | 3.tilt-up _ 3.tilt-down ; (1+c2){tilt-up} _ (c2+1){tilt-down} | (1+c2) _ 3.tilt-none _ (c2+1){: tilt-down} | (1+c2) _ 3{tilt-none} _ (c2+1){: tilt-down}']
t_shape_rot   = ['2_2{:rot-up} | '
                 '3_3{:rot-down} | '
                 '1 + rot-down + 1 _ rot-up + 2 _ 1 + rot-up + rot-down']
t_shape_circle= ['1 | 2_2 | 3_3_3 ;'
                 '3 | 1_2_3 | r4+c3, 1+c2, r2.c2 + r2 {:::circle}']
t_color       = ['red + green + blue, yellow + magenta + cyan ;'
                 'gray0 + gray1 + gray2 + gray3, '
                 'gray4 + gray5 + gray6 + gray7, '
                 'gray8 + gray9 + grayA + grayB, '
                 'grayC + grayD + grayE + grayF ; '
                 'texture1 + texture2, texture3 + texture4',
                 'red+1_2_red | '
                 '1+red+1_1+red+red_1 | '
                 '1+red.r2,1 | '
                 'red | '
                 '2_1+red+1_2 | '
                 'red+1+1_2_1+red'
                 '  {:: thumb}']
t_color_black = ['(r2+1,1) | (1+r2,1) {::black};'
                  '(r2+1,1){:black} | (r2+1,1);'
                 '6{black w2}_2_1 {:::thumb}'
                 ' @ '
                 '1+c3,c3+1{:black} | '
                 '1+c3,c3+black | '
                 '1+c3,c3+1.black {:black}'
                 '  {:::small}']

t_direction    = ['(r2+2,2)_(1+c2+c4) | (r2+2,2)_(1+c2+c4) {:rtl}'
                  ' @ '
                  '(r2+1,1) | 2_1 | 2_2 ; '
                  '(r2+1,1) | 2_1 | 2_2 {::rtl} {:::small}']

t_bleeds       = ['1 | 1.bleed.all ; 1.bleed.up | 1.bleed.down | 1.bleed.right ']

# test_overview_page = [[t_blanks[1] + ' {::: thumb}']]
test_overview_page = [t_bleeds]

test_sets_list = [ t_row, t_cols, t_plus, t_colplus,
                   t_layouts, t_lcols, t_lplus, t_lcolplus,
                   t_spreads, t_scols, t_splus, t_scolplus,
                   t_slayouts, t_slcols, t_slplus, t_slcolplus ]

t_attrib        = [  'r2',   'c2',    'r2c2']
t_attrib2       = [  'r3',   'c4',    'r5c6']
t_dotattrib     = [ '.r2',  '.c2',  '.r2.c2']
t_dotattrib2    = [ '.r3',  '.c4',  '.r5.c6']
t_numattrib     = [ '1r2',  '1c2',   '1r2c2']
t_numdotattrib  = ['1.r2', '1.c2', '1.r2.c2']
t_numdotattrib2 = ['1.r3', '1.c4', '1.r5.c6']
t_twodotattrib  = ['2.r2', '2.c2', '2.r2.c2']
t_twodotattrib2 = ['2.r3', '2.c4', '2.r5.c6']

test_attribs_list = [ t_attrib, t_attrib2,
                      t_dotattrib, t_dotattrib2,
                      t_numdotattrib, t_numdotattrib2,
                      t_twodotattrib, t_twodotattrib2 ]


t_group         = [' r2 + 2 , 4, 5.r2zc2zz{ .blank .etc } ']
t_group2        = ['(1.r2+1,1)']
t_group3        = ['(r2+1,1)  ']
t_group4        = ['(1r2c2+1,2c2,1+2,1+c3r3,c2+r2)@1_2']

test_groups_list = [ t_group4, t_group2, t_group3, t_group ]

# test_list     
# test_list     = ['1_()']
# test_list     = ['1_(3)']
# test_list     = ['1_3()']
# test_list     = ['1_(r2+1,1)']
# test_list     = ['1_3(r2+1,1)']

# test_all        = ['3++3', '3++3++3', '3,,3', '3++3(),,3', '3\n3', '3(\n)3()', '3', '33', '3 3', '3_3', '333', '3_3_3', '303', '30', '03', '0', '', '3()', '3()3()', '33()', '3()3']
test_all_opts   = ['1{ a:1 }_2{ b:2 }{: abc:12 };3{ abcd:3 }++4{: abcde:4 };;5{}{:}{::}{:::}{::::}'] # attributes OneOrMore example: https://pythonhosted.org/pyparsing/pyparsing.OneOrMore-class.html
test_all_opts.append("2{::: a b c};;2{::: d}")