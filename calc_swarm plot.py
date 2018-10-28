# -*- coding: utf-8 -*-
"""
Created on Wed May 30 12:56:28 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp

fplot.set_rc_params(font_size_offset=4)



path          = r'X:/Dnox/Tesla/2017/E1700224-08/data/recording/ecr_samples.xlsx'
frame         = pd.read_excel(path, usecols=[0,1]).dropna()
ecr_maxima    = frame["Maximum force"].tolist()

fplot.plot_swarm([ecr_maxima], [1], color='b')
fplot.plot_violin([ecr_maxima], [1])

path          = r'X:/Dnox/Tesla/2017/E1700224-08/data/recording/serial_samples.xlsx'
frame         = pd.read_excel(path, usecols=[0,1]).dropna()
series_maxima = frame["Maximum force"].tolist()

fplot.plot_violin([series_maxima], [2], body_color='g')
fplot.plot_swarm([series_maxima], [2], color='g')



fplot.set_plot_config(xa_label='sample groups sequence', ya_label='Force [N]', title='', xlim = [0, 3], ylim = [None,None])
fplot.modify_ticks(['ecr samples', 'series samples'], [1,2])

fplot.add_label('ecr samples', 'b', line_width=0, marker = 'o', marker_size=6)
fplot.add_label('serial samples', 'g', line_width=0, marker = 'o', marker_size=6)


fplot.set_rc_params()
plt.grid()
plt.savefig(r'X:/Dnox/Tesla/2017/E1700224-08/data/recording/results/swarm_comparison.png')