# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:21:37 2017

@author: 
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# =============================================================================
# INSERT DATA HERE
# =============================================================================
test_start       = dt.datetime( day= 12, month=4, year=2018, hour=15, minute=0 )
test_duration    = 480 # hours





# =============================================================================
# CALCULATION
# =============================================================================
# Hour, day, week weights
hour  = 1
day   = hour  *24
week  = day * 7

# Weeks calculation
weeks = np.floor(test_duration/week)
# Days calculation
dummy = test_duration - weeks * week
days = np.floor(dummy/day)
# Hours calculation
dummy -= days * day
hours = dummy%day
# End date and time calculation
test_end         = test_start  + dt.timedelta(hours = test_duration)


print( "\n\nTest start date and time \n{}.{}.{}  {}:{}".format(test_start.day, test_start.month, test_start.year, test_start.hour, test_start.minute ) )
print("-----------------------------------------")
print("Test duration in hours \n{} hours ".format(test_duration))
print("-----------------------------------------")
print("Test duration in days \n{} days and {} hours ".format(int(days + weeks * 7), int(hours)))
print("-----------------------------------------")
print("Test duration in weeks \n{} weeks {} days and {} hours ".format(int(weeks), int(days), int(hours)))
print("-----------------------------------------")
print( "Test end date and time \n{}.{}.{}  {}:{}".format(test_end.day, test_end.month, test_end.year, test_end.hour, test_end.minute ) )

