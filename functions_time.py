# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:56:06 2018

@author: CAZ2BJ
"""
import numpy as np
import matplotlib.pyplot as plt


import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp
import datetime as dt

def time_stamp_to_time_diff(time_stamp, formatt = "%H:%M:%S"):
    """Converts timestamp sequence ie.[12:10:34, 12:12:15 ... ] to time difference sequence ie. [0, 56 ...]    
    
    Parameters
    ----------       
    time_stamp : sequence
        time_stamp sequence        
    formatt : string
        time format string
    Returns
    -------
    out : list 
        list of time difference values in seconds
    """
    times = []

    start = dt.datetime.strptime(time_stamp[0], formatt)
       
    for time in time_stamp:
        current = dt.datetime.strptime(time, formatt)
        timedelta = current - start 
        times.append(timedelta.total_seconds())
    return times
# =============================================================================
# TEST
#times = ['12:20:21', '12:25:32', '12:30:31']
#results = time_stamp_to_time_diff(times)
# =============================================================================


def date_time_stamp_to_time_diff(date_stamp, time_stamp):
    """Converts timestamp sequence ie.[12:10:34, 12:12:15 ... ] to time difference sequence ie. [0, 56 ...]    
    
    Parameters
    ---------- 
    date_stamp : sequence
        date_stamp sequence ['13.07.2018', '13.07.2018', '14.07.2018']      
    time_stamp : sequence
        time_stamp sequence ['12:20:21', '12:25:32', '12:30:31']       
    Returns
    -------
    out : list 
        list of time difference values in seconds
    """
    times = []
    
    date = date_stamp[0].split('.')
    time = time_stamp[0].split(':')
    
    start = dt.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))
    
    for date, time in zip(date_stamp, time_stamp):
        date = date.split('.')
        time = time.split(':')
        
        current = dt.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))
        timedelta = current - start 
        times.append(timedelta.total_seconds())
    return times
# =============================================================================
# TEST
#times = ['12:20:21', '12:25:32', '12:30:31']
#days  = ['13.07.2018', '13.07.2018', '14.07.2018']
#results = date_time_stamp_to_time_diff(days, times)
# =============================================================================

































