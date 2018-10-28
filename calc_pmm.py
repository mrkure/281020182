# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:30:08 2018

@author: zdenek
n"""
import os
import sys
# append dir for script import
sys.path.append('U:/!Python')


import numpy as np
import pandas as pd
import functions_io as fio
import functions_plot as fplot
import matplotlib.pyplot as plt

    
"""
# =============================================================================
# user settings 
# =============================================================================
"""
included_dirs_keywords = ['Samples']
excluded_dirs_keywords = ['~']
skip_rows              = 20

temperature_diff = 1
pressure_offset  = 290

# p_diff graphs
plot_p_diff      = 1
plot_p_MSP       = 1
plot_p_BMP       = 1
# comparison graphs
plot_violin      = 1
plot_swarm       = 1
plot_box         = 1
                                  
p_diff_color_map = fplot.C_map(['red','blue', 'green'])                                                
comp_color_map   = fplot.C_map(['red', 'green', 'blue', 'grey'])
fplot.set_rc_params(font_size_offset = 6, figsize = (1400,600), linewidth = 4, markersize = 7)

temperatures        = [-8, -5, 0 , 10 , 22, 40]
voltages            = [10.5, 13.5, 15.5]
pressures           = [4500, 6000, 8500]
valid_measurements  = 50



"""
# =============================================================================
# end of user settings 
# =============================================================================
"""


# =============================================================================
# getting script dir path - initial point for all paths
# =============================================================================
cwd = fio.get_script_dir(__file__) 

results_dir, results_name                                = 'results', 'results.xlsx'
comparison_graphs                                        = 'comparison_graphs' 
p_diff_graphs, p_diff_base, p_diff_file, p_diff_root_dir = 'p_diff_graphs', 'base', 'file', 'root_dir'
hydra_name                                               = "hydra_before_test"
# creating dir structure for results
os.makedirs('{}/{}'.format(cwd, results_dir), exist_ok=True)

# =============================================================================
# calculation settings variables declaration
# =============================================================================
column_indexes      = [ 20,            21,         77     , 78    ,   79    ,     80         ,   81   ,    82      ,   85       ] 
column_names        = ['t_MSP_ok', 't_BMP_ok', 'p_diff', 'p_BMP',  'p_MSP', 'valid_meas',  'pressure', 'voltage', 'temperature']
sorted_columns      = ['pressure', 'voltage', 'temperature', 'valid_meas', 't_MSP_ok', 't_BMP_ok', 'p_diff', 'p_BMP', 'p_MSP' ]

plt.ioff()

# =============================================================================
# full calculation or only plots picker
# =============================================================================
calc = '1'
res_name = os.path.normpath('{}/{}/{}'.format(cwd, results_dir, results_name))
apaths   = fio.get_files(cwd, extension = ['xlsx'], contains = [res_name], not_contains=['~'], print_path=False)

for name in apaths:
    calc = input("results file has been found, calculate again ? ")
           
"""
# =============================================================================
#                      CALCULATION  STARTING POINT
# =============================================================================
"""
if calc == '1' or calc == 'y':
    # =============================================================================
    # getting all data file names
    # =============================================================================
    abs_paths    = fio.get_files(cwd, extension = ['xlsm'], contains = included_dirs_keywords, not_contains = excluded_dirs_keywords, print_path=False)
    root_dirs    = fio.get_parts_of_paths_list(abs_paths, -3)
    sample_dirs  = fio.get_parts_of_paths_list(abs_paths, -2)
    filenames    = fio.get_parts_of_paths_list(abs_paths, -1)
    
    # =============================================================================   
    # filtering all data-files based on conditions, calculating means of selected values
    # =============================================================================
    filtered_frames_list = []     
    for num, (abs_path, root_dir, sample_dir, filename) in enumerate(zip(abs_paths, root_dirs, sample_dirs, filenames)):
        print('Processing file ({}/{}) ........ {} / {} / {}'.format( '{x:02d}'.format(x=num+1), '{x:02d}'.format(x=len(abs_paths)), sample_dir, filename, root_dir))
    
        input_frame = pd.read_excel(abs_path, usecols=column_indexes, skiprows=skip_rows).apply(pd.to_numeric, errors='coerce', downcast='float')
        input_frame = input_frame.dropna(axis=0, how='any').reset_index(drop=True)
        input_frame.columns = column_names
        input_frame = input_frame[sorted_columns]
    
        for pressure in pressures:
            for voltage in voltages:
                for temperature in temperatures:
                    filtered_frame = input_frame[(input_frame.pressure == pressure) & 
                                                    (input_frame.voltage  == voltage ) & 
                                                    (input_frame.valid_meas == valid_measurements) &
                                                    (input_frame.temperature >= temperature - temperature_diff) & 
                                                    (input_frame.temperature <= temperature + temperature_diff) ] 
                   
                    t_MSP_non_01_count = len(filtered_frame.t_MSP_ok[filtered_frame.t_MSP_ok != 0.1])
                    t_BMP_non_01_count = len(filtered_frame.t_BMP_ok[filtered_frame.t_BMP_ok != 0.1])  
                    
                    filtered_frame = pd.DataFrame( [[root_dir, sample_dir, filename, pressure, voltage, temperature, len(filtered_frame.index), 
                                                     t_MSP_non_01_count, t_BMP_non_01_count ,filtered_frame.p_diff.mean() + pressure_offset, 
                                                     filtered_frame.p_BMP.mean() + pressure_offset, filtered_frame.p_MSP.mean() + pressure_offset ]], 
                                                     columns = ['root_dir', 'sample_dir', 'filename'] + sorted_columns)                 
                    filtered_frames_list.append(filtered_frame)
                    
    filtered_frame = pd.concat(filtered_frames_list, ignore_index=True)
# =============================================================================
# insert custom filters here
# =============================================================================    
# adding filter for more than 45 non 0.1 t_MSP values
    filtered_frame.loc[filtered_frame.t_MSP_ok <= 45, ['p_diff', 'p_MSP','p_BMP'] ] = np.nan
    
# =============================================================================
# saving selected data to excel file
# =============================================================================
    writer = pd.ExcelWriter('{}/{}/{}'.format( cwd, results_dir, results_name), engine='xlsxwriter')
    filtered_frame.to_excel(writer,'Sheet1', index=False)
    writer.save()
else:
    pass
# =============================================================================
# reading back saved selected data from excel file
# =============================================================================
input_frame = pd.read_excel('{}/{}/{}'.format(cwd, results_dir, results_name),usecols=[i for i in range(12)])
input_frame[ input_frame.columns.values.tolist()[3:] ] = \
input_frame[ input_frame.columns.values.tolist()[3:] ].apply(pd.to_numeric, errors = 'coerce')

root_dirs    = sorted([ a for a in input_frame.root_dir.unique()    ])
temperatures = sorted([ a for a in input_frame.temperature.unique() ])
pressures    = sorted([ a for a in input_frame.pressure.unique()    ])
voltages     = sorted([ a for a in input_frame.voltage.unique()     ])
samples      = sorted([ a for a in input_frame.sample_dir.unique()  ])
# =============================================================================
# insert custom filters here
# =============================================================================
input_frame  = input_frame[ (input_frame.p_diff < 2000) & (input_frame.p_diff > -2000) ] 
abs_paths    = fio.get_files(cwd, extension = ['xlsx'], contains = [hydra_name], not_contains = excluded_dirs_keywords, print_path=False)
hydra_frame  = pd.read_excel(abs_paths)
hydra_frame  = hydra_frame[['054_Diff_BMP_VIS_P_Mess_4_5bar_MP2_Sp1', '066_Diff_BMP_VIS_P_Mess_6_0bar_MP4_Sp1']] 


"""
# =============================================================================
#                  PLOTTING P_diff GRAPHS STARTING POINT 
# =============================================================================
"""
plt.ioff()
                
# =============================================================================
# generating p_diff graphs for each combination file/voltage/pressure
# =============================================================================
os.makedirs( '{}/{}/{}/{}'.format(cwd, results_dir, p_diff_graphs, p_diff_base), exist_ok=True)

g_num, g_total = 1, 0
for root_dir in root_dirs:
    filtered_frame = input_frame[input_frame.root_dir == root_dir]
    samples_s      = sorted([a for a in filtered_frame.sample_dir.unique()])
    for sample in samples_s:
        for pressure in pressures:
            for voltage in voltages:
                g_total += 1
                
for root_dir in root_dirs:
    filtered_frame = input_frame[input_frame.root_dir == root_dir]
    samples_s      = sorted([a for a in filtered_frame.sample_dir.unique()])
    for sample in samples_s:
        for pressure in pressures:
            for voltage in voltages: 
                p_diff_color_map.reset()
                plt.ioff()
                plt.figure()
                plt.ioff()
                next_frame = filtered_frame[ (filtered_frame.sample_dir == sample) & (filtered_frame.pressure == pressure) & (filtered_frame.voltage == voltage)]                                  
                next_frame = next_frame.sort_values(by='temperature')

                if plot_p_diff:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_diff.tolist(), color= p_diff_color_map.get_color(False), lw = 1, marker = 'o')
                    fplot.add_label('p_diff', p_diff_color_map.get_color(True), marker = 'o' )  
                if plot_p_BMP:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_BMP.tolist(), color = p_diff_color_map.get_color(False), lw = 1, marker = 'o')
                    fplot.add_label('p_BMP', p_diff_color_map.get_color(True), marker = 'o' ) 
                if plot_p_MSP:                               
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_MSP.tolist(), color = p_diff_color_map.get_color(False), lw = 1, marker = 'o')
                    fplot.add_label('p_MSP', p_diff_color_map.get_color(True), marker = 'o' )                               

                plt.plot([-8,-5,0,10,22,40], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
                plt.plot([-8,-5,0,10,22,40], [ 700, 700, 700, 700, 500, 700], 'k', ls = '--')
                fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]', '{}; {}; {} bar; {} V'.format(root_dir.replace('_',' '), sample, pressure/1000 ,voltage), ylim = [-2000,None])                                       
                plt.savefig( '{}/{}/{}/{}/{}_{}_bar_{}_V.png'.format( cwd, results_dir, p_diff_graphs, p_diff_base, sample, pressure/1000, voltage))                      
                plt.close()
                print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num, g_total), end="\r", flush=True)
                g_num += 1 
print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num-1, g_total))


# =============================================================================
# generating p_diff graphs for each file 
# =============================================================================
os.makedirs('{}/{}/{}/{}'.format(cwd, results_dir, p_diff_graphs, p_diff_file), exist_ok=True)

g_num, g_total = 1, 0
for root_dir in root_dirs:
    filtered_frame = input_frame[input_frame.root_dir == root_dir]
    samples_s      = sorted([a for a in filtered_frame.sample_dir.unique()])
    for sample in samples_s:
                g_total += 1
               
for root_dir in root_dirs:
    filtered_frame = input_frame[input_frame.root_dir == root_dir]
    samples_s       = sorted([a for a in filtered_frame.sample_dir.unique()])
    for sample in samples_s:

        fig = plt.figure()
        for pressure in pressures:
            for voltage in voltages: 
                p_diff_color_map.reset() 
                
                next_frame = filtered_frame[ (filtered_frame.sample_dir == sample) & (filtered_frame.pressure == pressure) & (filtered_frame.voltage == voltage)]                                  
                next_frame = next_frame.sort_values(by='temperature')
                
                if plot_p_diff:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_diff.tolist(), color= p_diff_color_map.get_color(True), lw = 1, marker = 'o')
                if plot_p_BMP:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_BMP.tolist(), color = p_diff_color_map.get_color(True), lw = 1, marker = 'o')
                if plot_p_MSP:                               
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_MSP.tolist(), color = p_diff_color_map.get_color(True), lw = 1, marker = 'o')
        
        p_diff_color_map.reset()                                       
        if plot_p_diff:
            fplot.add_label('p_diff', p_diff_color_map.get_color(True), marker = 'o' )  
        if plot_p_BMP:
            fplot.add_label('p_BMP', p_diff_color_map.get_color(True), marker = 'o' ) 
        if plot_p_MSP:                               
            fplot.add_label('p_MSP', p_diff_color_map.get_color(True), marker = 'o' ) 
                
        plt.plot([-8,-5,0,10,22,40], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
        plt.plot([-8,-5,0,10,22,40], [ 700, 700, 700, 700, 500, 700], 'k', ls = '--')
        fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]', '{}; {}; {} bar x {} V'.format(root_dir.replace('_', ' '), sample,(np.array(pressures)/1000).tolist(), voltages), ylim = [-2000,None])                  
        plt.savefig('{}/{}/{}/{}/{}.png'.format(cwd, results_dir, p_diff_graphs, p_diff_file, sample))   
        plt.close()
        print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num, g_total), end="\r", flush=True)
        g_num += 1 
print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num-1, g_total))



# =============================================================================
# plotting base graphs - one for each root_dir
# =============================================================================
os.makedirs('{}/{}/{}/{}'.format(cwd, results_dir, p_diff_graphs, p_diff_root_dir), exist_ok=True)
 
g_num, g_total = 1, 0
for root_dir in root_dirs:
                g_total += 1
                
for root_dir in root_dirs:
    filtered_frame = input_frame[input_frame.root_dir == root_dir]
    sampless       = sorted([a for a in filtered_frame.sample_dir.unique()])
    fig = plt.figure()
    for sample in sampless:
        for pressure in pressures:
            for voltage in voltages: 
             
                next_frame = filtered_frame[ (filtered_frame.sample_dir == sample) & (filtered_frame.pressure == pressure) & (filtered_frame.voltage == voltage)]                                  
                next_frame = next_frame.sort_values(by='temperature')
                p_diff_color_map.reset()
                if plot_p_diff:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_diff.tolist(), color= p_diff_color_map.get_color(True), lw = 1, marker = 'o')
                if plot_p_BMP:
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_BMP.tolist(), color = p_diff_color_map.get_color(True), lw = 1, marker = 'o')
                if plot_p_MSP:                               
                    plt.plot(next_frame.temperature.tolist(),next_frame.p_MSP.tolist(), color = p_diff_color_map.get_color(True), lw = 1, marker = 'o')                             
    p_diff_color_map.reset()
    if plot_p_diff:
        fplot.add_label('p_diff', p_diff_color_map.get_color(True), marker = 'o' )  
    if plot_p_BMP:
        fplot.add_label('p_BMP', p_diff_color_map.get_color(True), marker = 'o' ) 
    if plot_p_MSP:                               
        fplot.add_label('p_MSP', p_diff_color_map.get_color(True), marker = 'o' ) 
   
    plt.plot([-8,-5,0,10,22,40], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
    plt.plot([-8,-5,0,10,22,40], [ 700, 700, 700, 700, 500, 700], 'k', ls = '--')

    fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]', '{}; {} bar x {} V'.format(root_dir.replace('_', ' '), (np.array(pressures)/1000).tolist(), voltages), ylim = [-2000,None])        
    plt.savefig('{}/{}/{}/{}/{}.png'.format(cwd, results_dir, p_diff_graphs, p_diff_root_dir, root_dir)) 
    plt.close()
    print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num, g_total), end="\r", flush=True)
    g_num += 1 
print('Generating p_diff graphs ....... ({:02d}/{:02d})'.format(g_num-1, g_total))   
    
    

"""
# =============================================================================
#                  PLOTTING COMPARISON GRAPHS STARTING POINT
# =============================================================================
"""

each_dir_data_positions = []
root_dirs_count         = len(root_dirs)    
temperatures_count      = len(temperatures)
labels_positions        = np.arange(temperatures_count) * root_dirs_count  

for i in range(root_dirs_count):
    each_dir_data_positions.append( labels_positions + i * 0.75 )        
labels_positions        = labels_positions + (root_dirs_count-1)/2 * 0.75   


os.makedirs('{}/{}/{}'.format(cwd, results_dir, comparison_graphs), exist_ok=True)
g_num, g_total = 1, 0
for pressure in pressures:
    for voltage in voltages:
        g_total += 1
        
for pressure in pressures:
    for voltage in voltages:    
        fig = plt.figure()
        comp_color_map.reset()             
        for number, root_dir in enumerate(root_dirs):
            data =[]                  
            for temperature in temperatures:                
                 next_frame = input_frame[(input_frame.root_dir == root_dir) & (input_frame.temperature == temperature) & 
                                          (input_frame.pressure == pressure) & (input_frame.voltage == voltage)]                    
                 data.append(next_frame.p_diff.tolist())         
        
            if plot_violin:
                fplot.plot_violin(data, each_dir_data_positions[number], body_color = comp_color_map.get_color(False))
            if plot_box:
                fplot.plot_box(data, each_dir_data_positions[number], box_color = "k")                     
            if plot_swarm:
                fplot.plot_swarm(data, each_dir_data_positions[number], color=comp_color_map.get_color(False), marker ="o", ms=10, diff=0.1) 
                         
            fplot.add_label(root_dir.replace('_',' '), comp_color_map.get_color(True))
            
        fplot.modify_ticks(temperatures, labels_positions,  action = "clear")                    
        plt.xlim(labels_positions[0]-2, labels_positions[len(labels_positions)-1]+2)                      
        fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]','{} bar; {} V'.format( pressure/1000, voltage))                                       
        plt.savefig('{}/{}/{}/{}_{}_comparison.png'.format(cwd, results_dir, comparison_graphs, pressure, voltage))                     
        print('Generating comparison graphs ... ({:02d}/{:02d})'.format(g_num, g_total), end="\r", flush=True)
        g_num += 1 
        plt.close() 
print('Generating comparison graphs ... ({:02d}/{:02d})'.format(g_num-1, g_total)) 
print() 
 
input("press Enter to exit ;) ") 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    