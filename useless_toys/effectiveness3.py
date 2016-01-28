"""
    effectiveness3.py

    Compound nomogram of type 1: 
            F1+F2+F3=0
            F1+F4+F5=0

    log(Effectiveness)+(-log(ESR))+log(A) = 0
    log(ESR)+(-log(W)+log(5280))-log(v) = 0

    This one looks like it could actually be used.
"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

W_params={
    'u_min':10.0,
    'u_max':500.0,
    'function':lambda u:(-log10(u)+log10(5280.0)),
    'title':r'Sweep width in feet',
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
                }
V_params={
        'u_min':0.1,
        'u_max':20.0,
        'function':lambda u:(-log10(u)),
        'title':r'Speed in mph',
        'tick_levels':2,
        'tick_text_levels':1,
        'scale_type':'log',
                }
ESR_params={
    'tag':'esr',
    'u_min':(10.0/5280.0)*.1,
    'u_max':(500.0/5280.0)*20,
    'function':lambda u:(log10(u)),
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    'title':r'Effective Sweep Rate (sq-mi/hr)',
    }

ESR_2_params={
    'tag':'esr',
    'u_min':(10.0/5280.0)*.1,
    'u_max':(500.0/5280.0)*20,
    'function':lambda u:(-log10(u)),
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    }

A_params={
    'u_min':0.1,
    'u_max':10.0,
    'function':lambda u:log10(u),
    'title':r'Area in mi${}^2$',
    'tick_levels':2,
    'tick_text_levels':1,
    'tick_side':'left',
    'scale_type':'log smart',
}
E_params={
    'u_min':(10.0/5280.0)*.1/10.0,
    'u_max':(500.0/5280.0)*20/.1,
    'function':lambda u:log10(u),
    'title':r'Effectiveness',
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log smart',
}

block_1_params={
    'block_type':'type_1',
    'width':10.0,
    'height':20.0,
    'f1_params':W_params,
    'f2_params':V_params,
    'f3_params':ESR_params,
    'isopleth_values':[[197.0,1.0,'x']],
}

block_2_params={
    'block_type':'type_1',
    'width':10.0,
    'height':20.0,
    'f1_params':E_params,
    'f2_params':A_params,
    'f3_params':ESR_2_params,
    'isopleth_values':[['x',.5,197.0/5280.0]],
}

main_params={
              'filename':'effectiveness3.pdf',
              'paper_height':20.0,
              'paper_width':20.0,
              'block_params':[block_1_params,block_2_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'$E = Wv/A$',
              'title_y':21.0,
              }
Nomographer(main_params)
