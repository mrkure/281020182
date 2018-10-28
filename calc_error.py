# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:53:42 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt


import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp


x = np.linspace(-0.08,0.08,160)

over_200_ppm  = 6372549.02 * x**6	-800150.8296 * x**5 + 19541.8552 * x**4 + 562.4057315 * x**3 -18.20980735 * x**2 -9.135497395 * x**1 + 1.300099753 * x**0
over_10_ppm   = 4017242.862 * x**6 -438603.9335 * x**5	-8783.299926 * x**4  +	1736.291492 * x**3 + 8.192154187 * x**2	-10.47552085 * x**1 + 0.990573908 * x**0

under_200_ppm = -59264.74327 * x**6	-4554.65587	* x**5 + 335.2822676 * x**4 + 57.22096531 * x**3 + 2.013566176 * x**2 -8.579590974 * x**1 -0.383176295 * x**0
under_10_ppm  = -169755.1637 * x**6 -13455.58466* x**5 + 3216.230457 * x**4 + 89.40620783 * x**3 -19.32913576 * x**2 -8.298948559 * x**1 -0.070463402 * x**0



#plt.plot(x, over_200_ppm,  'r')
#plt.plot(x, over_10_ppm,   'r')
#plt.plot(x, under_200_ppm, 'r')
#plt.plot(x, under_10_ppm,  'r')

fplot.modify_ticks(['-8%', '-4%', '-0%', '4%', '8%'], [-0.08,-0.04,0,0.04,0.08])
plt.xlim(-0.08,0.08)
plt.ylim(-1,1.5)
plt.fill_between(x,-10, under_200_ppm, facecolor='red', alpha = 0.5)
plt.fill_between(x,under_200_ppm, under_10_ppm, facecolor='yellow', alpha = 0.5)
plt.fill_between(x,under_10_ppm, over_10_ppm, facecolor='green', alpha = 0.5)
plt.fill_between(x,over_10_ppm, over_200_ppm, facecolor='yellow', alpha = 0.5)
plt.fill_between(x,over_200_ppm, 10, facecolor='red', alpha = 0.5)
plt.grid(color = 'k')