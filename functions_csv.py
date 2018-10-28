# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:12:01 2018

@author: Zdenek
"""
import csv
import functions_io as fio

""" 
===============================================================================
 READ_DATA_FROM_CSV_FILE
===============================================================================
"""

def print_csv_header_tail(filename, print_header = 10, print_tail = 10, delimiter = ";", quotechar = '"'):

# counts number of rows in csv file
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        rows_number = len(list(csv_reader))   
# Print header
    if print_header > 0:
        print("-------------CSV HEADER-------------------")
        with open(filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar) 
            for i, line in enumerate(csv_reader):
                if i >= print_header:
                    break
                print("line: {}  value: {}".format(i, line))
        print()    
# Print tail 
    if print_tail > 0:
        print("-------------CSV TAIL-------------------")
        with open(filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar) 
            for i, line in enumerate(csv_reader):
                if i >= rows_number - print_header:
                    print("line: {}  value: {}".format(i, line))    
        print() 
    

def read_data_from_csv_file(filename, columns, read_from_line = None, read_to_line = None, print_header_tail = 10, delimiter = ";", quotechar = '"'):
    """Reads data from csv file
    
    Parameters
    ----------    
    filename : string 
        full path to csv file   
    columns : list of ints
        columns that should be readed        
    read_from_line : int
        first line to read
    read_to_line : int
        last line to read       
    delimiter : string
        usually ; 
    quotechar : string
        usually "
        
    Returns
    -------
    out : nested list 
        nested list of red data 
        
    Notes
    -----
    None

    Examples
    --------
    None       
   
    """ 
# Create nested list, where data is stored
    columns_list = []    
    for column in columns:
        columns_list.append([])
# counts number of rows in csv file
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        rows_number = len(list(csv_reader))     
# Calculates read from line and read to line values
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar) 
        
        if read_from_line == None:
           column_size = len(columns)  
                  
           for line_number, row in enumerate(csv_reader): 
               if len(row) < column_size:
                   pass
               else:
                   print(row)
                   read_from_line = line_number 
                   break      
        elif read_from_line != None: 
            pass
        else:
            pass        
        if read_to_line == None:
           read_to_line = rows_number
        elif read_to_line != None: 
           read_to_line = min(rows_number, read_to_line)
        else:
            pass        
# aquire data from csv
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)  
            
        for line_number, row in enumerate(csv_reader):  
            if line_number >= read_from_line and line_number <= read_to_line:                 
    # Columns in rows               
                for number,  column in enumerate(columns):
                    columns_list[number].append(row[column])
            else:
                pass                        
# print tail of the list            
    if print_header_tail > 0:
        print("-----------LIST HEADER-----------")
        for i, row in enumerate(columns_list[0]):
            if i >= print_header_tail: 
                break
            dummy = []
            for column in columns_list:
                dummy.append(column[i])
            print("line: {} values {}".format(i, dummy))
        print()
    else:
        pass
# print header of the list            
    if print_header_tail > 0:
        print("-----------LIST TAIL-----------")    
        for i, row in enumerate(columns_list[0]):
            if i > len(columns_list[0]) - print_header_tail: 
                dummy = []
                for column in columns_list:
                    dummy.append(column[i])
                print("line: {} values {}".format(i, dummy)) 
        print()
    else:
        pass                
    return columns_list

# =============================================================================
# TEST
#directory = fio.get_current_script_dir()
#filename  = fio.get_all_files_from_subdirectories(directory, contains=["csv_test_files"], extension=["csv"], print_path = False)[0]
#
#print_csv_header_tail(filename)
#data = read_data_from_csv_file(filename, [0,1,2], 5, 100, 5)
# =============================================================================


""" 
===============================================================================
 WRITE_DATA_TO_CSV_FILE
===============================================================================
"""
def write_data_to_csv_file(filename, data, delimiter = ";", quotechar = '"'):
    """Writes data to csv file
    
    Parameters
    ----------    
    filename : string 
        full file save path   
    data : nested list
        lists are readed in this way - list[0].row[0] ; list[1].row[0] and next row follows          
    delimiter : string
        usually ; 
    quotechar : string
        usually "
        
    Returns
    -------
    out: 
        none    
    Notes
    -----
    None

    Examples
    --------
    None       
   
    """  
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        rows = len(data[0])
        for row in range(rows):  
           line_to_write = []
           for column in range(len(data)):
               line_to_write.append(data[column][row])  
           spamwriter.writerow(line_to_write)
    return
# =============================================================================
# TEST
#nested_list = [ [1,2,3] , [4,5,6], [7,8,9] ]  
#directory   = fio.get_current_script_dir()
#directory   = r"{}/test_csv.csv".format(directory)
#write_data_to_csv_file(directory, nested_list)
# =============================================================================   





