"""

POD_from_W_v_t_simplified

  This one is like POD_from_W_v_t with the "effective sweep rate" and "effectiveness" scales turned into just plain index lines, by making 
  part of the nomograph type 3.

  Rd to W is done in one type 1 nomograph, and the rest in type 3
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
Coverage_min=.27
Coverage_max=3

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
    'title':r'Visibility',
    'title_x_shift':.5,
    'title_draw_center':True,
    'tick_levels':1,
    'tick_text_levels':1,
    'scale_type':'manual line',
    'linewidth_ticks':style.linewidth.THick,
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
    'title':r'Speed',
    'title_y_shift':.8,
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1,
         'dy':.25,
         'text':r'\small MPH',
         'width':5,
         }]
}

A_params={
    'u_min':Amin,
    'u_max':Amax,
    'function':lambda u:log10(u),
    'title':r'Area',
    'title_y_shift':0.8,
    'tick_levels':2,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log smart',
    'extra_titles':[
        {'text':r'$mi{}^2$',
         'dx':-1.25,
         'dy':0.25,
         }]
}

Effort_params={
    'u_min':Effort_min,
    'u_max':Effort_max,
    'function':lambda u:(-log10(u)),
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
    'function':lambda u:(log10(u)),
    'title':r'\large Coverage',
    'title_x_shift':-1,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'left',
    'scale_type':'log',
}

def POD(C):
    return (1-exp(-C))*100

def PODint(C):
    return int((1-exp(-C))*1000.0)/10.0

def Coverage(POD):
    return(-log(1-POD/100.0))

#POD_params={
#    'tag':'pod',
#    'u_min':35.0,
#    'u_max':90.0,
#    'function':lambda u:(u),
#    'align_func':Coverage,
#    'title':r'POD',
#    'title_x_shift':0.5,
#    'title_y_shift':0.45,
#    'tick_levels':3,
#    'tick_text_levels':2,
#    'tick_side':'right',
#    'scale_type':'linear',
#    'extra_titles':[
#        {'dx':-.5,
#         'dy':0.15,
#         'text':r'\small \%',
#         'width':5,
#         },
#        {'dx':-1.25,
#         'dy':-10,
#         'text':r'\small $POD = 1-\exp(-Wvt/A)$',
#         'width':5,
#         },
#    ]
#
#}
# POD_params={
#     'tag':'pod',
#     'u_min':Coverage_min,
#     'u_max':Coverage_max,
#     'function':lambda u:(log10(u)),
#     'align_func':lambda u:u,
#     'title':r'POD',
#     'title_x_shift':0.75,
#     'title_y_shift':0.45,
#     'tick_levels':3,
#     'tick_text_levels':2,
#     'tick_side':'right',
#     'scale_type':'manual line',
#     'manual_axis_data':{.3:PODint(.3),
#                         .4:PODint(.4),
#                         .5:PODint(.5),
#                         .6:PODint(.6),
#                         .7:PODint(.7),
#                         .8:PODint(.8),
#                         .9:PODint(.9),
#                         1:PODint(1),
#                         1.2:PODint(1.2),
#                         1.4:PODint(1.4),
#                         1.6:PODint(1.6),
#                         1.8:PODint(1.8),
#                         2:PODint(2),
#                         2.5:PODint(2.5),
#                         3:PODint(3),
#                         },
#     'extra_titles':[
#         {'dx':-.25,
#          'dy':0.15,
#          'text':r'\small \%',
#          'width':5,
#          },
#         {'dx':-1.25,
#          'dy':-12,
#          'text':r'\small $POD = 1-\exp(-Wvt/A)$',
#          'width':5,
#          },
#     ]
# }

POD_Axis_Range={}
for POD in range(25,96):
    if (POD%5 == 0):
        POD_Axis_Range[Coverage(POD)]='%d'%POD
    else:
        POD_Axis_Range[Coverage(POD)]=''

        POD_params={
    'tag':'pod',
    'u_min':Coverage_min,
    'u_max':Coverage_max,
    'function':lambda u:(log10(u)),
    'align_func':lambda u:u,
    'title':r'POD',
    'title_x_shift':0.75,
    'title_y_shift':0.45,
    'tick_levels':3,
    'tick_text_levels':2,
    'tick_side':'right',
    'scale_type':'manual line',
    'manual_axis_data':POD_Axis_Range,
    'extra_titles':[
        {'dx':-.25,
         'dy':0.15,
         'text':r'\small \%',
         'width':5,
         },
        {'dx':-1.25,
         'dy':-12,
         'text':r'\small $POD = 1-\exp(-Wvt/A)$',
         'width':5,
         },
    ]
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

block_1b_params={
    'block_type':'type_8',
    'f_params':W_params_meters,
    'isopleth_values':[['x']],
}

block_3b_params={
    'block_type':'type_8',
    'f_params':POD_params,
    'isopleth_values':[['x']],
}
block_main_params={
    'block_type':'type_3',
    'width':10.0,
    'height':20.0,
    'f_params':[W_params,V_params,A_params,Effort_params,Coverage_params],
    'reference_titles':['A','B'],
    'isopleth_values':[[Isopleth_W,Isopleth_V,Isopleth_A,Isopleth_Effort,'x']],
}
    
main_params={
              'filename':'POD_from_W_v_t_simplified.pdf',
              'paper_height':20,
              'paper_width':20,
              'block_params':[block_main_params,block_3b_params,block_0_params,block_0b_params,block_1b_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'\large POD Calculator for Planning',
              'title_x':12.5,
              'title_y':0,
              }
Nomographer(main_params)
