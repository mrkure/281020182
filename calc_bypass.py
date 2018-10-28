# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 07:40:50 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt


import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp

import pandas as pd
import datetime as dt

def time_stamp_to_time_diff(time_stamp, formatt = "%H:%M:%S"):
    times = []

    start = dt.datetime.strptime(time_stamp[0], formatt)
       
    for time in time_stamp:
        current = dt.datetime.strptime(time, formatt)
        timedelta = current - start 
        times.append(timedelta.total_seconds())
    return times



fplot.set_rc_params(font_size_offset = 0, figsize = (1400,600), linewidth = 2, markersize = 6)


path = r'X:\Dnox\Erprobung\13_Data_transfer\Carda\BFP_volumetric_bypass_test\Logged data-7.5V-10.01A'


# =============================================================================
# 
# =============================================================================
filesa = fio.get_files(path, contains = ['A0'], extension = ['csv'])
filesaa = fio.get_files(path, contains = ['A1'], extension = ['csv'])
filesa = filesa + filesaa

for file in filesa:
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    plt.plot(time, weight, 'b')
fplot.add_label('A', 'b')



filesb = fio.get_files(path, contains = ['B0'],  extension = ['csv'])
filesbb = fio.get_files(path, contains = ['B1'],  extension = ['csv'])
filesb = filesb + filesbb

for file in filesb:
    
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    plt.plot(time, weight, 'r')
fplot.add_label('B', 'r')


filesc = fio.get_files(path, contains = ['C0'], extension = ['csv'])
filescc = fio.get_files(path, contains = ['C1'], extension = ['csv'])
filesc = filesc + filescc

for file in filesc:
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    plt.plot(time, weight, 'g')
fplot.add_label('C', 'g')

plt.grid()
fplot.set_plot_config('Time [s]', 'Weight [g]')



# =============================================================================
# 
# =============================================================================
plt.figure()
filesa = fio.get_files(path, contains = ['A0'], extension = ['csv'])
filesaa = fio.get_files(path, contains = ['A1'], extension = ['csv'])
filesa = filesa + filesaa
for file in filesa:
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    line,  = plt.plot(time, weight)
    fplot.add_label(fio.get_part_of_path(file,-1), line.get_color())
fplot.set_plot_config('Time [s]', 'Weight [g]')
plt.grid()



plt.figure()
filesb = fio.get_files(path, contains = ['B0'],  extension = ['csv'])
filesbb = fio.get_files(path, contains = ['B1'],  extension = ['csv'])
filesb = filesb + filesbb
for file in filesb:    
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    line,  = plt.plot(time, weight)
    fplot.add_label(fio.get_part_of_path(file,-1), line.get_color())

fplot.set_plot_config('Time [s]', 'Weight [g]')
plt.grid()


plt.figure()
filesc = fio.get_files(path, contains = ['C0'], extension = ['csv'])
filescc = fio.get_files(path, contains = ['C1'], extension = ['csv'])
filesc = filesc + filescc
for file in filesc:
    print(file)
    dataframe = pd.read_csv(file, sep=';', decimal  = ',' )
    weight = dataframe[r'Weight [g]'].tolist()
    time   = dataframe.Time    
    time   = time.tolist()
    time   = time_stamp_to_time_diff(time)
    line,  = plt.plot(time, weight)
    fplot.add_label(fio.get_part_of_path(file,-1), line.get_color())
fplot.set_plot_config('Time [s]', 'Weight [g]')
plt.grid()



















