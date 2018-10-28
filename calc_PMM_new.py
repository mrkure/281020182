# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:37:47 2018

@author: CAZ2BJ
"""
import os
import sys
sys.path.append('Z:/work/!python')

sys.path.append(r'X:\Dnox\Erprobung\13_Data_transfer\Carda\!Python_scripts')
from time import sleep

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import functions_io as fio
import functions_plot as fplot
import functions_PMM_new as fpmm

# =============================================================================
# DIR structure settings
# =============================================================================
cwd               = fio.get_script_dir(__file__) 
root_dir          = fio.get_part_of_path(cwd,-1)

results_dir       = 'results1'
results_name      = 'results.xlsx'
comparison_graphs = 'comparison_graphs' 
p_diff_graphs     = 'p_diff_graphs'

number_of_samples = 6   
number_of_files   = 36

included_dirs_keywords = ['ED']
excluded_dirs_keywords = ['~']
extension              = ['dat']

p_diff_color_map = fplot.C_map(['red','blue', 'green'])                                                
comp_color_map   = fplot.C_map(['red',  'blue', 'green', 'grey', 'black', 'cyan'])

fplot.set_rc_params(font_size_offset = 6, figsize = (1400,600), linewidth = 4, markersize = 7)

# =============================================================================
# Data integrity check
# =============================================================================
print("\nChecking data integrity\n------------------------")
data_integrity_check = fpmm.data_integrity_check(cwd, number_of_samples, number_of_files, contains=included_dirs_keywords, not_contains=excluded_dirs_keywords, extension=extension)
fio.terminate_question(data_integrity_check, "\nProceed or abort ? y/n ")    

# =============================================================================
# Data reading
# =============================================================================

data_frame_list   = []
sample_dirs = fio.get_root_dirs(cwd, contains=included_dirs_keywords, not_contains=excluded_dirs_keywords, print_path = False)
print()
for sample_dir in sample_dirs:
    print("Processing sample.....{}".format(fio.get_part_of_path(sample_dir,-1)))
    files       = fio.get_files(sample_dir, extension=extension, contains=included_dirs_keywords, not_contains=excluded_dirs_keywords, search_subdirs = False, print_path = False)
    current_file = 1
    for file in files: 
        print('Processing sample {}....... ({:02d}/{:02d})'.format(fio.get_part_of_path(sample_dir,-1),current_file, len(files)), end="\r", flush=True)
        current_file += 1
        data_frame = fpmm.read_mdf_data(file)  
        data_frame_list.append(data_frame)
        # sleep(0.5) # Time in seconds.
result_frame = pd.concat(data_frame_list, ignore_index=True)

# =============================================================================
# Data saving
# =============================================================================
os.makedirs('{}/{}'.format(cwd, results_dir), exist_ok=True) 
writer = pd.ExcelWriter('{}/{}/{}'.format( cwd, results_dir, results_name), engine='xlsxwriter')
result_frame.to_excel(writer,'Sheet1', index=False)
writer.save()
# sleep(10)
# =============================================================================
# Generating p_diff graphs for each combination file/voltage/pressure
# =============================================================================
plt.ioff()
print('\nGenerating p_diff graphs')
os.makedirs( '{}/{}/{}'.format(cwd, results_dir, p_diff_graphs), exist_ok=True)

samples      = sorted([ a for a in result_frame['sample'].unique()   ])
for sample in samples:
    next_frame = result_frame[result_frame['sample'] == sample]
    pressures     = sorted([ a for a in next_frame['pressure'].unique() ])
    for pressure in pressures:
        next_frame2 = next_frame[next_frame['pressure'] == pressure]       
        voltages     = sorted([ a for a in next_frame2['voltage'].unique()])
        for voltage in voltages: 
            last_frame = next_frame2[next_frame2['voltage'] == voltage]
           
            p_diff_color_map.reset()            
            plt.figure()
            last_frame = last_frame.sort_values(by='temperature')                                  

            plt.plot(last_frame.temperature,last_frame.pDiff, color= p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_diff', p_diff_color_map.get_color(True), marker = 'o' )  
           
            for msp, msp_cor, msp_cor_new, temp, pDiff in zip(last_frame.valid_MSP_rate,  last_frame.valid_msp_rate_cor,last_frame.valid_msp_rate_cor2, last_frame.temperature, last_frame.pDiff ):
                plt.annotate("{} \n {} \n {}".format(msp, msp_cor, msp_cor_new), [temp, pDiff], fontsize = 16, fontweight='bold', color='red')

            plt.plot(last_frame.temperature,last_frame.pDiff_BMP, color = p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_BMP', p_diff_color_map.get_color(True), marker = 'o' ) 
                         
            plt.plot(last_frame.temperature,last_frame.pDiff_MSP, color = p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_MSP', p_diff_color_map.get_color(True), marker = 'o' )                               

            plt.plot([-8,-5,0,10,22,40], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
            plt.plot([-8,-5,0,10,22,40], [ 700, 700, 700, 700, 500, 700], 'k', ls = '--')
            plt.legend(loc = 'lower right')
            fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]',' {}; {} bar; {} V'.format( sample, pressure/1000 ,voltage/1000), ylim = [-2000,None])                                      
            plt.savefig( '{}/{}/{}/{}_{}_bar_{}_V.png'.format( cwd, results_dir, p_diff_graphs, sample, pressure/1000, voltage/1000))                      
            plt.close()



# =============================================================================
# Generating comparison graphs for each combination file/voltage/pressure
# =============================================================================
print('Generating comparison graphs')
os.makedirs('{}/{}/{}'.format(cwd, results_dir, comparison_graphs), exist_ok=True)

minimum, maximum = -800, 800

pressures    = sorted([ a for a in result_frame.pressure.unique()])
for pressure in pressures:
    next_frame = result_frame[result_frame.pressure == pressure]       
    voltages     = sorted([ a for a in next_frame.voltage.unique()])  
    for voltage in voltages:
        next_frame2 = next_frame[next_frame.voltage == voltage]
        plt.figure()
        plt.ioff() 
        comp_color_map.reset() 
        samples      = sorted([ a for a in next_frame['sample'].unique()])    
        for sample in samples:    
            next_frame3 = next_frame2[next_frame2['sample'] == sample].sort_values(by='temperature')
            
            plt.plot([0,1,2,3,4,5],next_frame3.pDiff.tolist(), color= comp_color_map.get_color(False), lw = 0, marker = 'o')  
            fplot.add_label(sample, comp_color_map.get_color(True), marker = 'o', line_width = 0 )   
            
            minimum = np.nanmin(next_frame3.pDiff.tolist() + [minimum])
            maximum = np.nanmax(next_frame3.pDiff.tolist() + [maximum])
           
            if next_frame3.temperature.tolist() != [-8,-5,0,10,22,40]:
                print('Temperature values mismatch at comparison graph generating')
            if pressure == 4500:
                plt.plot([0,1,2,3,4,5], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
           
            if pressure == 6000:
                plt.plot([0,1,2,3,4,5], [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
                plt.plot([0,1,2,3,4,5], [700,700,700,700,500,700], 'k', ls = '--')                  
         
            if pressure == 8500:
                plt.plot([0,1,2,3,4,5], [700,700,700,700,500,700], 'k', ls = '--')
       
        plt.plot(6.5,minimum , markersize  = 0)  
        fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]',' {}; {} bar; {} V'.format( root_dir, pressure/1000 ,voltage/1000), ylim = [minimum -100, maximum+100])    
        fplot.modify_ticks(['-8','-5','0','10','22','40'], [0,1,2,3,4,5], action = "clear", axes_type = 'x')      
        plt.savefig( '{}/{}/{}/{}_bar_{}_V.png'.format( cwd, results_dir, comparison_graphs, pressure/1000, voltage/1000))                      
        plt.close()       






















































