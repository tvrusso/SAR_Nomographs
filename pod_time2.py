"""
    pod_time.py

    nomogram of type 5.

    In this example: ln(1-u) = -wd*v

"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *



block_params={
    'block_type':'type_5',
    'u_func':lambda u:log(1-u/100),
    'v_func':lambda x,v:(-x*v),
    'v_values':[10.,100,1000],
    'u_values':[30.,35.,40.,45.,50.,55.,60.,65.,70.],
    'wd_values':[.0001,.001,.01,.1,1.,10.0],
    'wd_tick_levels':2,
    'wd_tick_text_levels':1,
    'wd_tick_side':'right',
    'wd_title':'Effectiveness',
    'v_title':'hours',
    'u_tick_levels':1,
    'u_tick_text_levels':2,
    'u_tick_side':'left',
    'u_title':'POD',
    'scale_type_u':'linear',
    'scale_type_wd':'log',
    'wd_title_opposite_tick':True,
    'wd_title_distance_center':2.5,
}


main_params={
              'filename':'pod_time2.pdf',
              'paper_height':10.0,
              'paper_width':10.0,
              'block_params':[block_params],
              'transformations':[('rotate',0.01),('scale paper',)]
              }

Nomographer(main_params)
