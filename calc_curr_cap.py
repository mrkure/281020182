# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:26:25 2018

@author: 
"""
import numpy as np
import matplotlib.pyplot as plt



import csv

# =============================================================================
# READS DATA FROM INPUT CSV FILE, COLUMNS PARAMETER IS LIST OF REQUIRED CULUMNS                                                                                                   
# =============================================================================

def read_data_from_csv_file(filename, columns, read_from_line, read_to_line, delimiter, quotechar):
# counts number of rows in csv file
    with open(filename) as csvfile:
         csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
         rows_number = len(list(csv_reader))      
# we are using same counting as it is in excell, then for python we need to shift rows to -1
    read_from_line -= 1
    if read_to_line != -1:
        read_to_line -= 1        
# set limit to last readed line - if read_to_line == -1 then file will be readed to last line         
    if read_to_line == -1:
       read_to_line = rows_number
    read_to_line = min(rows_number, read_to_line)    
# Create list of lists, where data is stored
    columns_list = []    
    for column in columns:
        columns_list.append([])
# Read data into list's lists               
    with open(filename) as csvfile:
         csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
# Rows  
         for line_number, row in enumerate(csv_reader):  
             if line_number >= read_from_line and line_number <= read_to_line:                 
# Columns in rows               
                 for number,  column in enumerate(columns):
                     columns_list[number].append(row[column])
    return columns_list


def write_data_to_csv_file(filename, data, delimiter, quotechar):
    
    pass
  
a = 1,2,3,4,5,6,7,8,9
b = 'a','b','c','d','e','f','g','h','i',    
c = 100,200,300,400,500,600,700,800,900 

path = r"U:\Test.csv"

#with open(path, 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='"')
##    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


with open(path, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for a, b, c in zip(a, b, c):
        spamwriter.writerow([a, b, c])


#def convert_list_of_lists_to_2d_numpy_array(list_of_lists):
#    
#    if len (list_of_lists) > 0 :        
#        number_of_lists = len (list_of_lists)
#        length_of_lists = len (list_of_lists[0])
#        numpy_2d_array  = np.zeros( (number_of_lists,length_of_lists ), dtype=np.float64  )
#        
#        for list_number, _list in enumerate(list_of_lists):
#            for field_number, field in enumerate(_list):
#                numpy_2d_array[list_number][field_number] = np.float( field.replace(',','.')  )
#        return numpy_2d_array
#
#
#
#
#path  = r"X:/Dnox/Erprobung/13_Data_transfer/Vadlejch/Maximum_Current_Capability.csv"
#
#
#data = read_data_from_csv_file(path, [1,3,4,5], 2, 18, ";", '"')
#
#
#arr = convert_list_of_lists_to_2d_numpy_array(data)
#
#
#current = arr[0]
#tt1    = arr[1]
#tt2      = arr[2]
#ta      = arr[3]
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
#deltat = tt1 - ta
#
#t = 140 - deltat

#
#
#
#plt.plot(t, current)
#
#
#
#
#


