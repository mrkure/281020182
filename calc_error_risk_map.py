# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:53:42 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('U:/!Python')
import os
import pandas as pd
import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp

cwd = fio.get_script_dir(__file__) 
hydra_name                        = "hydra_after_test"
results_dir                       = 'results'
included_dirs_keywords            = ['samples']
excluded_dirs_keywords            = ['~', 'backup']



# creating dir structure for results
os.makedirs('{}/{}'.format(cwd, results_dir), exist_ok=True)


abs_paths      = fio.get_files(cwd, extension = ['xlsm'], contains = included_dirs_keywords, not_contains = excluded_dirs_keywords, print_path=False)
root_dirs      = fio.get_parts_of_paths_list(abs_paths, -3)
sample_dirs    = fio.get_parts_of_paths_list(abs_paths, -2)
filenames      = fio.get_parts_of_paths_list(abs_paths, -1)
#   hydra file
try:
    hydra_abs_path   = fio.get_files(cwd, extension = ['xlsx'], contains = [hydra_name], not_contains = ['~'], print_path=False)
    hydra_frame      = pd.read_excel(hydra_abs_path[0]) 
except Exception:   
    print('{}{}{}'.format('file: ', hydra_name, ' not found'))
    input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    raise
try:    
    hydra_frame      = hydra_frame[['Ident No.', '066_Diff_BMP_VIS_P_Mess_6_0bar_MP4_Sp1', '006_BerechnetesHubvolumen_6_0bar_3_Sp1']] 
except Exception:   
    print('{}{}{}'.format('required column in file :', hydra_name, ' missing'))
    input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    raise
    
hydra_samples_sorted = sorted(list(hydra_frame['Ident No.']))    
samples_sorted       = sorted(sample_dirs)

# controll for equality between samples and hydra samples 
    
if len(samples_sorted) != len(hydra_samples_sorted):        
    print('{}'.format('not the same number of samples in data and hydra'))
    input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
    raise           
for sam, ple in zip(samples_sorted, hydra_samples_sorted):
    if sam == ple:
        pass
    else:
        print('{}'.format('files not equal'))
        input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
        raise
print('All data files found and valid')   
input("Press ENTER to continue..")   



c_map = fplot.C_map()
c_map


volumetric_constant = 31.75


samples        = sorted([ a for a in hydra_frame['Ident No.'].unique()])

print('sample', ' ' ,  'volumetric', ' ' , 'p_diff')
for sample in samples:
    p_diff      = hydra_frame.loc[(hydra_frame['Ident No.'] == sample),['066_Diff_BMP_VIS_P_Mess_6_0bar_MP4_Sp1']].values[0]
    volumetric  = hydra_frame.loc[(hydra_frame['Ident No.'] == sample),['006_BerechnetesHubvolumen_6_0bar_3_Sp1']].values[0] 
    plt.plot(   volumetric/volumetric_constant -1  , p_diff , color = c_map.get_color(False), marker = 'o', markeredgecolor = 'k')
    fplot.add_label(sample, c_map.get_color(True),0, '-', 'o'  )
    
    print(sample, ' ' ,  volumetric/volumetric_constant -1, ' ' , p_diff)


x = np.linspace(-0.08,0.08,20000)

over_200_ppm  = 6372549.02 * x**6	-800150.8296 * x**5 + 19541.8552 * x**4 + 562.4057315 * x**3 -18.20980735 * x**2 -9.135497395 * x**1 + 1.300099753 * x**0
over_10_ppm   = 4017242.862 * x**6 -438603.9335 * x**5	-8783.299926 * x**4  +	1736.291492 * x**3 + 8.192154187 * x**2	-10.47552085 * x**1 + 0.990573908 * x**0

under_200_ppm = -59264.74327 * x**6	-4554.65587	* x**5 + 335.2822676 * x**4 + 57.22096531 * x**3 + 2.013566176 * x**2 -8.579590974 * x**1 -0.383176295 * x**0

under_10_ppm  = -169755.1637 * x**6 -13455.58466* x**5 + 3216.230457 * x**4 + 89.40620783 * x**3 -19.32913576 * x**2 -8.298948559 * x**1 -0.070463402 * x**0

aa = np.where(under_200_ppm < -0.5)[0][0]

start = np.where( (x >= -0.04) )[0][0]
under_200_ppm[start:aa] = -0.5


#under_10_ppm[np.where(x > -0.04 and x < 0.04)] = -0.5

fplot.modify_ticks(['-8%', '-4%', '-0%', '4%', '8%'], [-0.08,-0.04,0,0.04,0.08])
plt.xlim(-0.08,0.08)
plt.ylim(-1,1.5)
plt.fill_between(x,-10, under_200_ppm, facecolor='red', alpha = 0.5)
plt.fill_between(x,under_200_ppm, under_10_ppm, facecolor='g', alpha = 0.5)
plt.fill_between(x,under_10_ppm, over_10_ppm, facecolor='green', alpha = 0.5)
plt.fill_between(x,over_10_ppm, over_200_ppm, facecolor='g', alpha = 0.5)
plt.fill_between(x,over_200_ppm, 10, facecolor='red', alpha = 0.5)
plt.grid(color = 'k')

plt.xlabel('Volumetric (compared to nominal)')
plt.ylabel('p_diff [bar]')

plt.savefig('{}/{}/{}'.format(cwd, results_dir, 'error_risk.png' ))

print()
input("press Enter to exit ;)") 


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    