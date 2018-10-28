# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:04:17 2018

@author: CAZ2BJ
"""
import numpy as np
import pandas as pd

import mdfreader

import functions_io as fio




def data_integrity_check(root_dir, number_of_samples, number_of_files, contains=[], not_contains=[], extension=[]):
    integrity_check = 1

    samples_dirs = fio.get_root_dirs(root_dir, contains=contains, not_contains=not_contains, print_path = False)
    
    if len(samples_dirs) != number_of_samples:
        print('Wrong number of samples, {} of {} samples found'.format(len(samples_dirs), number_of_samples))
        integrity_check = 0
    else:
        print('All files found')
    
    for sample_dir in samples_dirs:
        files =  fio.get_files(sample_dir, extension=extension, contains=contains, not_contains=not_contains, search_subdirs = False, print_path = False)
        if len(files) != number_of_files:
            print('Wrong number of measured points at sample {}. {} of {} points found'.format(fio.get_part_of_path(sample_dir,-1), len(files), number_of_files))
            integrity_check = 0
        else:
            pass
            
        for file in files:
            file = file.replace('\\', '_').split('.')[0].split('_')
            if file[-1] == '110':
                print('Voltage out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] ))
                integrity_check = 0
            elif file[-1] == '101':
                print('Temperature out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] ))
                integrity_check = 0
            elif file[-1] == '011':
                print('Pressure out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] ))
                integrity_check = 0
            elif file[-1] == '001':
                print('Pressure and temperature out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] ))  
                integrity_check = 0
            elif file[-1] == '010':
                print('Pressure and voltage out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] )) 
                integrity_check = 0
            elif file[-1] == '100':
                print('Temperature and voltage out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] )) 
                integrity_check = 0
            elif file[-1] == '000':
                print('Pressure, temperature and voltage out of limits for sample {} at point {} mbar {} °C {} mV'.format(file[-7],file[-4], file[-3], file[-2] ))                
                integrity_check = 0
            else: pass

    return integrity_check

def find_rising_edges(array):
    new_array = np.zeros(len(array)) + array
    new_array = np.append(array[0],np.diff(new_array))
    new_array[new_array != 1] = 0
    return new_array

def find_indicies_of_centres(array):
    rising_edges_indicies = np.where(array == 1)[0]
    diffs_between_edges   = np.diff(rising_edges_indicies)
    centres_indicies      = (diffs_between_edges/2).astype(int) + rising_edges_indicies[0:-1]
    return centres_indicies
    
def calc_MSP_valid_cor(dictionary):
    t_msp = dictionary['UrSolnPmp_tiMSP']['data']
    i_msp = dictionary['UrSolnPmp_iMSP']['data']
    ps_flag = dictionary['UrSolnPmp_flgPs']['data']
 
    ps_flag_rising_edges = find_rising_edges(ps_flag)
    centre_indicies      = find_indicies_of_centres(ps_flag_rising_edges)
    
    time_values    = t_msp[centre_indicies]
    time_values[time_values != 0.1] = 1
    time_values[time_values == 0.1] = 0
    
    current_values = i_msp[centre_indicies]
    current_values[current_values != 0] = 1
    
    
    # last ps_flag is not used
    ps_flag_count   = sum(ps_flag_rising_edges) - 1
    msp_valid_count = sum(time_values  * current_values)
    
    valid_msp_rate = msp_valid_count * 100/ps_flag_count
    
    test = np.zeros(len(t_msp))
    test[centre_indicies] = 999
    
    ll = [t_msp, i_msp, ps_flag, ps_flag_rising_edges, test]
    ar = np.array(ll)
    return np.round(valid_msp_rate,2), ar

def calc_MSP_valid_cor2(dictionary):
  
    t_msp = dictionary['UrSolnPmp_tiMSP']['data']
    i_msp = dictionary['UrSolnPmp_iMSP']['data']
    ps_flag = dictionary['UrSolnPmp_flgPs']['data']
    UrSolnPmp_stErrMSP_MP = dictionary['UrSolnPmp_stErrMSP_MP']['data']
    UrSolnPmp_stOpMode_MP = dictionary['UrSolnPmp_stOpMode_MP']['data']    
    
    ps_flag_rising_edges = find_rising_edges(ps_flag)
    centre_indicies      = find_indicies_of_centres(ps_flag_rising_edges)
    UrSolnPmp_stOpMode_MP[ps_flag_rising_edges == 0]  = 0 
     
    #  remove measuring strokes from centre indicies
    ps_flag_ind       = np.where(ps_flag_rising_edges == 1)[0][:-1] # indexy, kde rising edges vektor je jedna  
    
    values            = UrSolnPmp_stOpMode_MP[ps_flag_ind]     # selekce hodnot ze ziskanych indexu
    
    regular_strokes   = centre_indicies[values == 1]
    # measuring_strokes = centre_indicies[values == 3]
       
    time_values    = t_msp[regular_strokes]
    time_values[time_values != 0.1] = 1
    time_values[time_values == 0.1] = 0
    
    current_values = i_msp[regular_strokes]
    current_values[current_values != 0] = 1
    
    stErrMSP_values = UrSolnPmp_stErrMSP_MP[regular_strokes]
    stErrMSP_values[stErrMSP_values != 0]  = -1
    stErrMSP_values[stErrMSP_values == 0]  = 1
    stErrMSP_values[stErrMSP_values == -1] = 0
    
    
    regular_strokes_count   = len(regular_strokes) 
    msp_valid_count = sum(time_values  * current_values * stErrMSP_values )
    
    valid_msp_rate = msp_valid_count * 100/regular_strokes_count
    
    test = np.zeros(len(t_msp))
    test[regular_strokes] = 1
    
    frame = pd.DataFrame.from_dict({ 't_msp':t_msp, 'i_msp':i_msp, 'ps_flag':ps_flag,'ps_flag_edges':ps_flag_rising_edges, \
           'UrSolnPmp_stErrMSP_MP':UrSolnPmp_stErrMSP_MP, 'UrSolnPmp_stOpMode_MP':UrSolnPmp_stOpMode_MP, 'centres':test}   )
           
    sequence = ['t_msp',    'i_msp', 'UrSolnPmp_stErrMSP_MP', 'ps_flag', 'ps_flag_edges',  'UrSolnPmp_stOpMode_MP', 'centres']
    frame = frame.reindex(columns=sequence)
    
    return np.round(valid_msp_rate,2), frame

def read_mdf(path):
    data_file  = mdfreader.mdf(path,noDataLoading=False)
    info       = mdfreader.mdfinfo()
    channels   = info.listChannels(path) # returns only the list of channels    info=mdfreader.mdfinfo()   
    dictionary = {}
    [dictionary.update({channel:data_file.getChannel(channel)}) for channel in channels]
    return dictionary


def read_mdf_data(file):
    data_file  = mdfreader.mdf(file,noDataLoading=False)
    info       = mdfreader.mdfinfo()    
    channels   = info.listChannels(file)

    dictionary = {}
    [dictionary.update({channel:data_file.getChannel(channel)}) for channel in channels]
        
    X20_validBMP_rate_last60s = round(dictionary['X20_validBMP_rate_last60s']['data'][-1],1)
    X21_validMSP_rate_last60s = round(dictionary['X21_validMSP_rate_last60s']['data'][-1],1)
    
    X56_pMess_avg60s          = round(dictionary['X56_pMess_avg60s']['data'][-1],1)
    X86_pIndi_avg60s          = round(dictionary['X86_pIndi_avg60s']['data'][-1],1)
    X96_pDiff_avg60s          = round(dictionary['X96_pDiff_avg60s']['data'][-1],1)
    
    X66_pBMP_avg60s           = round(dictionary['X66_pBMP_avg60s']['data'][-1],1)
    X76_pMSP_avg60s           = round(dictionary['X76_pMSP_avg60s']['data'][-1],1)
    
    p_diff_MSP                = round(X76_pMSP_avg60s - X56_pMess_avg60s, 3)
    p_diff_BMP                = round(X66_pBMP_avg60s - X56_pMess_avg60s,3)
    
    valid_msp_rate_cor, ar        = calc_MSP_valid_cor(dictionary)
    valid_msp_rate_cor2, ar2      = calc_MSP_valid_cor2(dictionary)
    
    root_dir                  = file.split('\\')[-3]

    pressure                  = int(file.replace('\\', '_').split('.')[0].split('_')[-4])
    temperature               = int(file.replace('\\', '_').split('.')[0].split('_')[-3])
    voltage                   = int(file.replace('\\', '_').split('.')[0].split('_')[-2])
    sample                    = file.replace('\\', '_').split('.')[0].split('_')[-6]
    

    data_frame = pd.DataFrame([[sample, root_dir, pressure, temperature, voltage, X56_pMess_avg60s, X86_pIndi_avg60s, X96_pDiff_avg60s, p_diff_MSP, p_diff_BMP, X20_validBMP_rate_last60s, X21_validMSP_rate_last60s, valid_msp_rate_cor, valid_msp_rate_cor2 ]], \
                    columns = ['sample','root_dir','pressure','temperature', 'voltage', 'pMess',       'pIndi',        'pDiff',       'pDiff_MSP',  'pDiff_BMP', 'valid_BMP_rate',          'valid_MSP_rate', 'valid_msp_rate_cor', 'valid_msp_rate_cor2' ])
    return  data_frame


# =============================================================================
# 
# =============================================================================
   
# path       = r'Z:/work/ED1806903_20181025_4500_22_13500_111.dat'            

# dictionary = read_mdf(path)

# rate, frame = calc_MSP_valid_cor(dictionary)

# rate2, frame2 = calc_MSP_valid_cor2(dictionary)
































