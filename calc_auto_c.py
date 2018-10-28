# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 07:00:18 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt


import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp

import win32api, win32con
import time
import random

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    


for i in range(100):
  
    pos_x = random.randint(100, 200)
    pos_y = random.randint(100,200)
    timee  = random.randint(10, 50)
    print('{}   {}   {}   {}'.format(i, pos_x, pos_y, timee))
    click(pos_x, pos_y)
    time.sleep(timee)

    pos_x = random.randint(100, 200)
    pos_y = random.randint(100,200)
    timee  = random.randint(10, 50)
    print('{}   {}   {}   {}'.format(i, pos_x, pos_y, timee))
    click(pos_x, pos_y)
    time.sleep(timee)