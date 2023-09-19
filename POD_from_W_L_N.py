"""

POD_from_W_L_T.py

  Compute POD/Coverage from sweep width, one searcher's track length, and number of searchers on team

  C = WNL/A = (W/5280)*N*L/A

  Taking log of both sides, this defines the type 3 nomograph:
  log C = log W-log(5280) + log(N) + log(L) - log(A)
  or 
  log C - log W + log(5280) - log N - log L + log A = 0

  Rd to W is done in one type 1 nomograph, and the rest in type 3
"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *
from pyx import *
from math import log,log10

# Scale limit parameters
# Range of sweep widths
Wmin=10
Wmax=200
# range of searcher track lengths (miles)
Lmin=.5
Lmax=10
# Range of areas
Amin=.25
Amax=10
# range of team sizes (# searchers
N_min=3
N_max=10
# Range of coverage scale
Coverage_min=.27
Coverage_max=3

# Example isopleth calculation
Isopleth_W=95
Isopleth_W_mi=Isopleth_W/5280.0
Isopleth_A=.5

Isopleth_L = 5.0   # Miles
Isopleth_N = 6     # searchers

Isopleth_C = Isopleth_W_mi*Isopleth_L*Isopleth_N/Isopleth_A

print ("Computed coverage should be ",Isopleth_C)

# Primary range of detection scale
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

# Secondary range of detection scale, in meters
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

# Scale for object visibility, high, average, low, per Koester et. al,
# WILDERNESS &ENVIRONMENTALMEDICINE, 25, 132-142 (2014)
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

# Sweep width primary scale
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

# Sweep width primary scale, duplicated for second nomograph, lined up with
# W0 scale
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

# Sweep width secondary scale, in meters
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

# Single searcher track length, in miles
L_params={
    'u_min':Lmin,
    'u_max':Lmax,
    'function':lambda u:(-log10(u)),
    'title':r'Track length',
    'title_y_shift':.8,
    'tick_levels':3,
    'tick_text_levels':2,
    'scale_type':'log',
    'extra_titles':[
        {'dx':-1,
         'dy':.25,
         'text':r'\small Miles',
         'width':5,
         }]
}

# Area scale in square miles
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

# Team size (# searchers)
N_params={
    'u_min':N_min,
    'u_max':N_max,
    'function':lambda u:(-log10(u)),
    'title':r'N',
    'title_y_shift':0.75,
    'tick_levels':1,
    'tick_text_levels':1,
    'tick_side':'left',
    'scale_type':'linear',
    'extra_titles':[
        {'dx':-1.5,
         'dy':0.2,
         'text':r'\small (searchers)',
         'width':5,
         }]
}

# Coverage scale
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
    return (1.0-exp(-C))*100.0
def PODint(C):
    return int((1-exp(-C))*1000.0)/10.0
def Coverage(POD):
    return(-log(1.0-POD/100.0))

# Define the POD ticks to line up correctly with corresponding coverage
POD_Axis_Range={}
for POD in range(25,96):
    if (POD%5 == 0):
        POD_Axis_Range[Coverage(POD)]='%d'%POD
    else:
        POD_Axis_Range[Coverage(POD)]=''

#POD  scale
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
         'text':r'\small $POD = 1-\exp(-WNL/A)$',
         'width':5,
         },
    ]
}

# Define the nomographs
# Block 0 is the nomograph for converting Range of Detection to Sweep Width
block_0_params={
    'block_type':'type_1',
    'width':2.0,
    'height':20.0,
    'f1_params':W0_params,
    'f2_params':Multiplier_params,
    'f3_params':Rd_params,
    'isopleth_values':[['x',1.6,Isopleth_W/1.6]],
}

# This is the meters scale for range of detection, so Rd measurements in
# either units can be used
block_0b_params={
    'block_type':'type_8',
    'f_params':Rd_params_meters,
    'isopleth_values':[['x']],
}

# This is the meters scale for sweep width, just in case users have W tables
# in meters already --- they can then skip the Rd -> W computation.
block_1b_params={
    'block_type':'type_8',
    'f_params':W_params_meters,
    'isopleth_values':[['x']],
}

# This is the POD scale, to be lined up with coverage scale
block_3b_params={
    'block_type':'type_8',
    'f_params':POD_params,
    'isopleth_values':[['x']],
}

# This is the main nomograph block, computing coverage from W, N, L and A.
block_main_params={
    'block_type':'type_3',
    'width':10.0,
    'height':20.0,
    'f_params':[W_params,L_params,N_params,A_params,Coverage_params],
    'reference_titles':['A','B'],
    'isopleth_values':[[Isopleth_W,Isopleth_L,Isopleth_N,Isopleth_A,'x']],
}
    
# Now generate the thing for real.
# Note that the order of blocks in the block_params field makes no immediate
# sense --- it is neither left-to-right nor right-to-left.  I had to move
# things around here until the nomograph looked as I wanted it to.
main_params={
              'filename':'POD_from_W_L_N.pdf',
              'paper_height':20,
              'paper_width':20,
              'block_params':[block_main_params,block_3b_params,block_0_params,block_0b_params,block_1b_params],
              'transformations':[('rotate',0.01),('scale paper',),('polygon',)],
              'title_str':r'\large POD Calculator for Debriefing',
              'title_x':12.5,
              'title_y':0,
              }
Nomographer(main_params)
