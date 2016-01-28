"""
    effectiveness2.py

    Simple nomogram of type 3: F1+F2+...+FN=0

    This example has N=4: log(Effectiveness)+(-log(W)+log(5280))+(-log(v))+log(A) = 0

"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

N_params_1={
        'u_min':10.0,
        'u_max':500.0,
        'function':lambda u:(-log10(u)+log10(5280.0)),
        'title':r'Sweep width in feet',
        'tick_levels':3,
        'tick_text_levels':2,
        'scale_type':'log',
                }
N_params_2={
        'u_min':0.1,
        'u_max':20.0,
        'function':lambda u:(-log10(u)),
        'title':r'Speed in mph',
        'tick_levels':2,
        'tick_text_levels':1,
        'scale_type':'log',
                }
N_params_3={
        'u_min':0.1,
        'u_max':10.0,
        'function':lambda u:log10(u),
        'title':r'Area in mi${}^2$',
        'tick_levels':2,
        'tick_text_levels':1,
        'scale_type':'log smart',
                }
N_params_4={
        'u_min':0.0000001,
        'u_max':15.2,
        'function':lambda u:log10(u),
        'title':r'Effectiveness',
        'tick_levels':3,
        'tick_text_levels':2,
        'scale_type':'log smart',
                }

block_1_params={
             'block_type':'type_3',
             'width':10.0,
             'height':10.0,
             'reference_titles':['Effective Sweep Rate'],
             'f_params':[N_params_1,N_params_2,N_params_3,
                         N_params_4],
             'isopleth_values':[[197.0,1,.5,'x']],
             }

main_params={
              'filename':'effectiveness2.pdf',
              'paper_height':20.0,
              'paper_width':20.0,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'$E = Wv/A$',
              'title_y':21.0,
              }
Nomographer(main_params)
