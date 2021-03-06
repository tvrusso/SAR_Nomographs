"""
    effectiveness3.py

    Compound nomogram of type 1: 
            F1+F2+F3=0
            F1+F4+F5=0
            F4+F6+F7=0

    log(ESR)+(-log(W)+log(5280))-log(v) = 0
    log(Effectiveness)+(-log(ESR))+log(A) = 0
    log(Effectiveness) + log(effort-in-searcher-hours) - log(Coverage) = 0

    This one looks like it could actually be used.
"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

Wmin=10
Wmax=200
Vmin=.75
Vmax=3
ESR_min=(Wmin/5280.0)*Vmin
ESR_max=(Wmax/5280.0)*Vmax
Amin=.25
Amax=10
Emin=.005
Emax=.5
Effort_min=5
Effort_max=300
Coverage_min=.3
Coverage_max=4

print "Coverage range: ",Coverage_min,Coverage_max
print "Effort range: ",Effort_min,Effort_max

Isopleth_W=95
Isopleth_W_mi=Isopleth_W/5280.0
Isopleth_V=1.0
Isopleth_ESR=Isopleth_W_mi*Isopleth_V
Isopleth_A=1
Isopleth_Effectiveness=Isopleth_ESR/Isopleth_A
Isopleth_Effort=55

Rd_params={
    'tag':'Rd',
    'u_min':Wmin/1.8,
    'u_max':Wmax/1.8,
    'function':lambda u:(-log10(u)),
    'title':r'$R_d$',
    'title_y_shift':0.5,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1.25,
         'dy':-0.08,
         'text':r'\small $ft$',
         'width':5,
         }]
}
Rd_params_meters={
    'tag':'Rd',
    'u_min':Wmin/1.8*0.3048,
    'u_max':Wmax/1.9*0.3048,
    'function':lambda u:(-log10(u)),
    'align_func':lambda u:u/0.3048,
    'title':r'\small $m$',
    'title_x_shift':0.4,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'right',
    'scale_type':'log',
}
Multiplier_params={
    'u_min':1.1,
    'u_max':1.8,
    'function':lambda u:(-log10(u)),
    'scale_type':'linear',
    'title':r'Object Visibility',
    'tick_levels':1,
    'tick_text_levels':1,
    'scale_type':'manual line',
    'manual_axis_data':{1.1:'Low',
                        1.6:'Average',
                        1.8:'High'
                        },
}
W0_params={
    'tag':'SweepWidth',
    'u_min':Wmin,
    'u_max':Wmax,
    'function':lambda u:(log10(u)),
    'title':r'Sweep width',
    'title_y_shift':0.8,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1.25,
         'dy':0.25,
         'text':r'\small $ft$',
         'width':5,
         }]
}

W_params={
    'tag':'SweepWidth',
    'u_min':Wmin,
    'u_max':Wmax,
    'function':lambda u:(-log10(u)+log10(5280.0)),
    'title':r'Sweep width',
    'title_y_shift':0.8,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1.25,
         'dy':0.25,
         'text':r'\small $ft$',
         'width':5,
         }]
                }
W_params_meters={
    'tag':'SweepWidth',
    'u_min':Wmin*0.3048,
    'u_max':Wmax*0.3048,
    'function':lambda u:(-log10(u)+log10(5280.0)),
    'align_func':lambda u:u/0.3048,
    'title':r'\small $m$',
    'title_x_shift':0.4,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'right',
    'scale_type':'log',
}

V_params={
        'u_min':Vmin,
        'u_max':Vmax,
        'function':lambda u:(-log10(u)),
        'title':r'Speed in mph',
        'tick_levels':3,
        'tick_text_levels':2,
        'scale_type':'log',
                }
ESR_params={
    'tag':'esr',
    'u_min':ESR_min,
    'u_max':ESR_max,
    'function':lambda u:(log10(u)),
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    'title':r'Effective Sweep Rate (sq-mi/hr)',
    }

ESR_2_params={
    'tag':'esr',
    'u_min':ESR_min,
    'u_max':ESR_max,
    'function':lambda u:(-log10(u)),
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    }

A_params={
    'u_min':Amin,
    'u_max':Amax,
    'function':lambda u:log10(u),
    'title':r'Area in mi${}^2$',
    'tick_levels':2,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log smart',
}

E_params={
    'u_min':Emin,
    'u_max':Emax,
    'function':lambda u:log10(u),
    'title':r'Effectiveness',
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log smart',
    'tag':'effectiveness',
}

E2_params={
    'u_min':Emin,
    'u_max':Emax,
    'function':lambda u:log10(u),
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log smart',
    'tag':'effectiveness',
}

Effort_params={
    'u_min':Effort_min,
    'u_max':Effort_max,
    'function':lambda u:(log10(u)),
    'title':r'Allocation',
    'title_y_shift':0.75,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1.5,
         'dy':0.2,
         'text':r'\small (searcher-hours)',
         'width':5,
         }]
}

Coverage_params={
    'tag':'pod',
    'u_min':Coverage_min,
    'u_max':Coverage_max,
    'function':lambda u:(-log10(u)),
    'title':r'\large Coverage',
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
}

def POD(C):
    return (1-exp(-C))*100
def Coverage(POD):
    return(-log(1-POD/100))

POD_params={
    'tag':'pod',
    'u_min':25.0,
    'u_max':95.0,
    'function':lambda u:(u),
    'align_func':Coverage,
    'title':r'POD',
    'title_x_shift':0.5,
    'title_y_shift':0.45,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'right',
    'scale_type':'linear',
    'extra_titles':[
        {'dx':-.5,
         'dy':0.15,
         'text':r'\small \%',
         'width':5,
         }]

}

block_0_params={
    'block_type':'type_1',
    'width':2.0,
    'height':20.0,
    'f1_params':W0_params,
    'f2_params':Multiplier_params,
    'f3_params':Rd_params,
    'isopleth_values':[['x',1.6,Isopleth_W/1.6]],
}
block_0b_params={
    'block_type':'type_8',
    'f_params':Rd_params_meters,
    'isopleth_values':[['x']],
}

block_1_params={
    'block_type':'type_1',
    'width':2.0,
    'height':20.0,
    'f1_params':W_params,
    'f2_params':V_params,
    'f3_params':ESR_params,
    'isopleth_values':[[Isopleth_W,Isopleth_V,'x']],
}

block_1b_params={
    'block_type':'type_8',
    'f_params':W_params_meters,
    'isopleth_values':[['x']],
}

block_2_params={
    'block_type':'type_1',
    'width':7.0,
    'height':20.0,
    'f1_params':E_params,
    'f2_params':A_params,
    'f3_params':ESR_2_params,
    'isopleth_values':[['x',Isopleth_A,Isopleth_ESR]],
}

block_3_params={
    'block_type':'type_1',
    'width':15.0,
    'height':20.0,
    'f1_params':Coverage_params,
    'f2_params':Effort_params,
    'f3_params':E2_params,
    'isopleth_values':[['x',Isopleth_Effort,Isopleth_Effectiveness]],
}


block_3b_params={
    'block_type':'type_8',
    'f_params':POD_params,
    'isopleth_values':[['x']],
}
main_params={
              'filename':'POD_from_W_v_t.pdf',
              'paper_height':21.59,
              'paper_width':27.94,
              'block_params':[block_1_params,block_0_params,block_0b_params,block_1b_params,block_2_params,block_3_params,block_3b_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'\large $POD = 1-\exp(-Wvt/A)$',
              'title_x':27.9,
              'title_y':4.0,
              }
Nomographer(main_params)
