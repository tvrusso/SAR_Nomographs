"""
    pod_time.py

    nomogram of type 5.

    In this example: u = -(1/wd)*ln(1-v)

    Copyright (C) 2007-2009  Leif Roschier

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *



block_params={
    'block_type':'type_5',
    'u_func':lambda u:u,
    'v_func':lambda x,v:(-1/x)*log(1-v/100),
    'u_values':[.01,.1,1.,10.,100],
    'v_values':[30.,40.,50.],
    'wd_values':[.0001,.001,.01,.1,1.],
    'wd_tick_levels':2,
    'wd_tick_text_levels':1,
    'wd_tick_side':'right',
    'wd_title':'Effectiveness',
    'u_title':'hours',
    'u_tick_levels':2,
    'u_tick_text_levels':1,
    'u_tick_side':'left',
    'v_title':'POD',
    'scale_type_u':'log',
    'scale_type_wd':'log',
    'wd_title_opposite_tick':True,
    'wd_title_distance_center':2.5,
}


main_params={
              'filename':'pod_time.pdf',
              'paper_height':10.0,
              'paper_width':10.0,
              'block_params':[block_params],
              'transformations':[('rotate',0.01),('scale paper',)]
              }

Nomographer(main_params)
