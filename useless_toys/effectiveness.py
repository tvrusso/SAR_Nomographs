"""
    effectiveness.py

    Nomogram to solve E = Wv/A (W in ft, v in mph, A in sq mi)

    Attempt with type 4 (proportion) nomogram.  Does not look great.

"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

A_params_1={
        'u_min':0.125,
        'u_max':2.0,
        'function':lambda u:u,
        'title':r'Area in $mi^2$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
                }
W_params_2={
        'u_min':10,
        'u_max':200.0,
        'function':lambda u:u,
        'title':r'Sweep width in feet',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
                }
v_params_3={
        'u_min':.5,
        'u_max':20.0,
        'function':lambda u:u,
        'title':r'speed in mph',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }
E_params_4={
        'u_min':.00047,
        'u_max':0.5,
        'function':lambda u:u*5280,
        'title':r'Effectiveness',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }

block_1_params={
                'block_type':'type_4',
                'f1_params':A_params_1,
                'f2_params':W_params_2,
                'f3_params':v_params_3,
                'f4_params':E_params_4,
                'isopleth_values':[[.25,50,2,'x']],
                'float_axis':'F3 or F4',
                 }

main_params={
              'filename':'effectiveness.pdf',
              'paper_height':20.0,
              'paper_width':20.0,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'$E/v=W/A$',
              'title_y':8.0,
              }
Nomographer(main_params)
