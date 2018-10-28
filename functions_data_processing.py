
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:26:39 2018
@author: Zdenek
"""
import numpy as np


"""
# =============================================================================
# NESTED LIST TO NUMPY ARR
# =============================================================================
"""
def nested_list_to_numpy_arr(nested_list):
    
    if len (nested_list) > 0 :        
        number_of_lists = len (nested_list)
        length_of_lists = len (nested_list[0])
        numpy_2d_array  = np.zeros( (number_of_lists,length_of_lists ), dtype=np.float64  )
        
        for list_number, _list in enumerate(nested_list):
            for field_number, field in enumerate(_list):
                numpy_2d_array[list_number][field_number] = np.float( field.replace(',','.')  )
    return numpy_2d_array
# =============================================================================
# TEST
#nested_list = [['1,2','2,8'], ['3,5', '4,9']]
#array       =  nested_list_to_numpy_arr(nested_list)
# =============================================================================

"""
# =============================================================================
# GET NEAREST INDEX OF VALUE
# =============================================================================
"""
def get_nearest_index_of_value(array, value):
    index  = np.abs(array - value).argmin()    
    return index   
# =============================================================================
# TEST
# array = np.arange(0, 100, 0.01)
# print( get_index_of_value(array, 39))
# =============================================================================




# =============================================================================
# calculate min and max of given array
# =============================================================================
def minimum_index_calculation(x_column, y_column, low_value_treshold, high_value_treshold): 
    if low_value_treshold == None:
        low_treshold_index = 0
    else:
        low_treshold_index  = np.abs(x_column - low_value_treshold).argmin()          
    if high_value_treshold == None:
        high_treshold_index = x_column.size
    else:
        high_treshold_index = np.abs(x_column - high_value_treshold).argmin()

    minimum_index = np.abs(y_column[low_treshold_index : high_treshold_index]).argmin() + low_treshold_index         
    minimum_value = y_column[minimum_index]  
    
    return minimum_index, minimum_value








def minimum_index_calculation_from_derivation(x_column, y_column, low_value_treshold, high_value_threshold):
    if low_value_treshold == None:
        low_treshold_index = 0
    else:
        low_treshold_index  = np.abs(x_column - low_value_treshold).argmin()          
    if high_value_threshold == None:
        high_treshold_index = x_column.size
    else:
        high_treshold_index = np.abs(x_column - high_value_threshold).argmin() 
 
    derivation          = derivation_calculation(x_column, y_column, low_treshold_index, high_treshold_index)  
  
    minimum_index = np.argmin(derivation) + low_treshold_index         
    minimum_value = y_column[minimum_index] 
        
    try:
        while y_column[minimum_index + 1] < y_column[minimum_index]:
            if minimum_index >= low_treshold_index and minimum_index <= high_treshold_index:                
                minimum_index += 1 
                minimum_value = y_column[minimum_index]
            else:
                break
    except Exception:
        print("Reached end of line at minimum search")   
            
    return minimum_index, minimum_value







def maximum_index_calculation(x_column, y_column, low_value_treshold, high_value_treshold): 
    
    if low_value_treshold == None:
        low_treshold_index = 0
    else:
        low_treshold_index  = np.abs(x_column - low_value_treshold).argmin()          
    if high_value_treshold == None:
        high_treshold_index = x_column.size
    else:
        high_treshold_index = np.abs(x_column - high_value_treshold).argmin()

    maximum_index = np.abs(y_column[low_treshold_index : high_treshold_index]).argmax() + low_treshold_index         
    maximum_value = y_column[maximum_index]  
    
    return maximum_index, maximum_value    
  
    
def maximum_index_calculation_derivative(x_column, y_column, low_value_treshold, high_treshold_index): 
    
    if low_value_treshold == None:
        low_treshold_index = 0
    else:
        low_treshold_index  = np.abs(x_column - low_value_treshold).argmin()          
    maximum_index = np.abs(y_column[low_treshold_index : high_treshold_index]).argmax() + low_treshold_index         
    maximum_value = y_column[maximum_index]  
    
    return maximum_index, maximum_value  






def derivation_calculation(x_column, y_column, low_index_treshold, high_index_treshold):            
    if low_index_treshold  == None:
        low_index_treshold = 0
    if high_index_treshold == None:
        low_index_treshold = x_column.size 
    differentiative_array = np.zeros(high_index_treshold - low_index_treshold)
    
    for i in np.arange(differentiative_array.size):
        try:
            differentiative_array[i] = (y_column[i + low_index_treshold+1] - y_column[i + low_index_treshold-1]) / (x_column[i + low_index_treshold+1] - x_column[i + low_index_treshold-1])
        except Exception:
            pass                       
    return differentiative_array


def derivation_calculation_from_value(x_column, y_column, low_value_treshold, high_value_treshold):   
    if low_value_treshold == None:
        low_index_treshold = 0
    else:
        low_index_treshold  = np.abs(x_column - low_value_treshold).argmin()          
    if high_value_treshold == None:
        high_index_treshold = x_column.size
    else:
        high_index_treshold = np.abs(x_column - high_value_treshold).argmin()

    differentiative_array = np.zeros(high_index_treshold - low_index_treshold)
    
    for i in np.arange(differentiative_array.size):
        try:
            differentiative_array[i] = (y_column[i + low_index_treshold+1] - y_column[i + low_index_treshold-1]) / (x_column[i + low_index_treshold+1] - x_column[i + low_index_treshold-1])
        except Exception:
            pass                       
    return differentiative_array, low_index_treshold, high_index_treshold

            

def max_min_values_calculation(numpy_2d_array, x_column, y_column, use_search_limits, min_search_limit_value, max_search_limit_value, use_diff_method):
# calculate start and end index limits for search of connector lock "click shut = zacvaku" on X column array      
    min_search_limit_index = 0 
    max_search_limit_index = numpy_2d_array[0].size

    if use_search_limits:
        min_search_limit_index     =  np.abs(numpy_2d_array[x_column] - min_search_limit_value).argmin()        
        max_search_limit_index     =  np.abs(numpy_2d_array[x_column] - max_search_limit_value).argmin()        
    else:
        pass
    
    differentiative_array  =  np.zeros(max_search_limit_index - min_search_limit_index)
           
    # calculate central numerical dervative 
    if use_diff_method:
        for i in np.arange(differentiative_array.size):
            try:
                differentiative_array[i] = (numpy_2d_array[y_column][i + min_search_limit_index+1] - numpy_2d_array[y_column][i + min_search_limit_index-1]) / \
                                           (numpy_2d_array[x_column][i + min_search_limit_index+1] - numpy_2d_array[x_column][i + min_search_limit_index-1])
                minimum_value_index = np.argmin(differentiative_array ) + min_search_limit_index
            except Exception:
                pass
            
    # move to the right on values array a bit to get to minimum_value_index index
        try:
            while numpy_2d_array[y_column][minimum_value_index + 1] < numpy_2d_array[y_column][minimum_value_index]:
                if minimum_value_index >= min_search_limit_index and minimum_value_index <= max_search_limit_index:                
                    minimum_value_index += 1 
                else:
                    break
        except Exception:
            print("Reached end of line at minimum search")
            
        maximum_value_index = np.argmax( numpy_2d_array[y_column][0:minimum_value_index])
        
# get maximum index value 
    else :                                              
        maximum_value_index = np.argmax( numpy_2d_array[y_column][min_search_limit_index:max_search_limit_index]) + min_search_limit_index
        minimum_value_index = np.argmin( numpy_2d_array[y_column][min_search_limit_index:max_search_limit_index]) + min_search_limit_index   
    return minimum_value_index, maximum_value_index, min_search_limit_index, max_search_limit_index, differentiative_array                       
