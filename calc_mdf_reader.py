# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:19:23 2018

@author: CAZ2BJ
"""

import mdfreader
import numpy as np
import pandas as pd

path       = r'X:\Dnox\Erprobung\13_Data_transfer\Carda\PMM_test_namery\E9999999\ED184321_20181005__8500_40_13500_111.dat'

def find_rising_edges(array):
    new_array = np.append(array[0],np.diff(array))
    new_array[new_array != 1] = 0
    return new_array

def find_indicies_of_centres(array):
    rising_edges_indicies = np.where(array == 1)[0]
    diffs_between_edges   = np.diff(rising_edges_indicies)
    centres_indicies      = (diffs_between_edges/2).astype(int) + rising_edges_indicies[0:-1]
    return centres_indicies
    


def get_channels_summary(file, save = 0):
    data_file  = mdfreader.mdf(path,noDataLoading=False)
    info       = mdfreader.mdfinfo() 
    channels   = info.listChannels(path)   
    channels   = info.listChannels(path) # returns only the list of channels    info=mdfreader.mdfinfo()
    frames = []
    values = []
    keys   = []
    dictionary = {}
    [dictionary.update({channel:data_file.getChannel(channel)}) for channel in channels]
    for dic in dictionary:
        inner =  dictionary[dic]
        try:
            for x, y in inner.items():

                if y is None:
                    values.append('None')
                elif isinstance(y, str):
                    values.append(y)
                elif np.isscalar(y):
                    values.append(1)
                elif np.isscalar(y) == False:
                    values.append(len(y))    
                else:
                    values.append(y)
                keys.append(x)

            frame = pd.DataFrame([values], columns = keys)
            frame = pd.DataFrame([[dic]+values], columns = ['Variable'] + keys)

            frames.append(frame)
            keys   = []
            values = [] 
        except:
            print(dic,' failed')
    result_frame = pd.concat(frames, ignore_index=True) 
    if save:
        file = file.split('.')[0] + '.xlsx'
        writer = pd.ExcelWriter(file, engine='xlsxwriter')
        result_frame.to_excel(writer,'Sheet1', index=False)
        writer.save()     
    return result_frame


path       = r'Z:/work/ED1806903_20181025_4500_22_13500_111.dat'            
# frame = get_channels_summary(path,0)

def read_mdf_file(file):
    data_file  = mdfreader.mdf(path,noDataLoading=False)
    info       = mdfreader.mdfinfo()


    channels   = info.listChannels(path) # returns only the list of channels    info=mdfreader.mdfinfo()

    dictionary = {}
    [dictionary.update({channel:data_file.getChannel(channel)}) for channel in channels]
    return dictionary

dictionary = read_mdf_file(path)
# data_file  = mdfreader.mdf(path,noDataLoading=False)
# info       = mdfreader.mdfinfo()


# channels   = info.listChannels(path) # returns only the list of channels    info=mdfreader.mdfinfo()

# dictionary = {}
# [dictionary.update({channel:data_file.getChannel(channel)}) for channel in channels]
#
#
#t_msp = dictionary['UrSolnPmp_tiMSP']['data']
#i_msp = dictionary['UrSolnPmp_iMSP']['data']
#ps_flag = dictionary['UrSolnPmp_flgPs']['data']
#opmode = dictionary['UrSolnPmp_stOpMode_MP']['data']
#
#
#
#ps_flag_rising_edges = find_rising_edges(ps_flag)
#centre_indicies      = find_indicies_of_centres(ps_flag_rising_edges)
#
#time_values    = t_msp[centre_indicies]
#time_values[time_values != 0.1] = 1
#time_values[time_values == 0.1] = 0
#
#current_values = i_msp[centre_indicies]
#current_values[current_values != 0] = 1
#
#
## last ps_flag is not used
#ps_flag_count   = sum(ps_flag_rising_edges) - 1
#msp_valid_count = sum(time_values  * current_values)
#
#valid_msp_rate = msp_valid_count * 100/ps_flag_count
#
#test = np.zeros(len(t_msp))
#test[centre_indicies] = 999
#
#ll = [t_msp, i_msp, ps_flag,opmode, ps_flag_rising_edges, test]
#ar = np.array(ll)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#





