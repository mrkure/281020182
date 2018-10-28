# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:03:26 2018

@author: CAZ2BJ
"""
import os
import numpy as np
import matplotlib.pyplot as plt

import functions_io as fio
import functions_csv as fcsv
import functions_plot as fplot
import functions_excel as fexcel
import functions_data_processing as fdp

def remove_empty_folders(path, remove_dir_level, removeRoot=True):  # remove_dir_level = 0 dir, 1 - first inner dirs ...
    remove_dir_level = remove_dir_level + 1  

    if not os.path.isdir(path):
        return

    files = os.listdir(path)                                        # search for dirs of files
    
    if len(files):                                                  # if dirs or files have been found
        for f in files:                                             # for dir or file in dirs_and_files
            fullpath = os.path.join(path, f)                        # create full_path
            if os.path.isdir(fullpath):                             # if current file or dir is DIR
                remove_empty_folders(fullpath, remove_dir_level)    # run recursively another instance of function 
  
    files = os.listdir(path)
    if len(files) == 0 and removeRoot and remove_dir_level  > 3:
        print ("Removing empty folder:", path)
        os.rmdir(path)

    else:
        pass
 
    


files = [r'X:\Dnox\Tesla\2014', r'X:\Dnox\Tesla\2015', r'X:\Dnox\Tesla\2016', r'X:\Dnox\Tesla\2017']

for file in files:
    remove_empty_folders(file,1)
















