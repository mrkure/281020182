# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 09:40:55 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('U:/!Python')
import pandas as pd
import functions_io as fio
import functions_csv as fcsv
import functions_data_processing as fdp
import math 
import os 



script_path = os.path.normpath(os.path.abspath(__file__)) 
cwd         = os.path.split(script_path)[0] 

os.makedirs('{}/{}'.format(cwd, 'results'), exist_ok=True)
def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return idx-1
    else:
        return idx

columns =  ['sample','assembly force 1', 'assembly force 2', 'assembly force 3', 'assembly force 4', 'assembly force 5', 'assembly force 6', 'assembly force 7', 'assembly force 8', 'assembly force 9', 'assembly force 10']    
llist = []
files = fio.get_files(cwd, extension=['csv'])
dirs = fio.get_parts_of_paths_list(files, -2)

for file, dirr in zip(files, dirs): 
    data = fcsv.read_data_from_csv_file(file, [0,2], 7, None, 0)
    data = fdp.nested_list_to_numpy_arr(data)

    fig  = plt.figure(figsize=(13,7))    
    plt.plot(data[1], data[0])
   
    plt.title(dirr)
    points = np.arange(0,11)*34
   
    for index, i in enumerate(points):
        if index == 0:
            points[index] = 0
        elif index == 1:
            points[index] = 26
        else:
            points[index] = points[index-1]+36
            
    points[-1] = np.floor(data[1][ len(data[1])-1 ])
    
    starts = points[:-1]
    ends = points[1:]
    
    

    plt.xlabel('Time [s]',  fontsize = 16 )
    plt.ylabel('Force [N]', fontsize = 16 )
    plt.title(dirr, fontsize = 16)
    plt.savefig('{}/results/{}.png'.format(cwd, dirr)) 
    
    plt.plot( starts, np.zeros(len(starts)), 'bo'  ) 
    plt.plot( ends, np.ones(len(starts)), 'ro'  )   
    plt.savefig('{}/results/control_points_{}.png'.format(cwd, dirr))    
    
    startsi = []
    endsi   = []
    
    
    for index, tt in enumerate(starts):
        
        startsi.append( find_nearest(data[1],starts[index]) )
        endsi.append( find_nearest(data[1],ends[index]) ) 
    
    

    mm = [dirr]
    for index, tt in enumerate(startsi):
        mm.append(  max(  data[0][ startsi[index]:endsi[index]  ])  )

    




  

    current_frame = pd.DataFrame( [ mm] , columns =  columns)
    llist.append(current_frame)
    
    
new_data_frame = pd.concat(llist, ignore_index=True)    

writer = pd.ExcelWriter('{}/results/{}'.format( cwd, "results.xlsx"), engine='xlsxwriter')
new_data_frame.to_excel(writer,'Sheet1', index=False)
writer.save()








































