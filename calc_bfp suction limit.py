# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:30:08 2018

@author: zdenek
"""

import os
import sys
# append dir for script import
sys.path.append('U:/!Python')
import numpy as np

# Kolik odsaje pumpa pri avg objemu na zdvih a 40 mil stroku
strokes       = 40000000
one_stroke_V  = 70e-9 # m**3
total_volume  = strokes * one_stroke_V

# Jaky je predpokladany objem na jedno odsati ?
# Uvazuji hadici 2 m dlouhou s prumerem 5 mm
r = 2.5e-3 # m
d = 2 # m
V = np.pi * r**2  * d

# Vysledek je 71301 odsati
suctions = total_volume/V
