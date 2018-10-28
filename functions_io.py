# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:11:27 2018

@author: Zdenek
"""
import re
import os
import os.path

def terminate_question(raise_question_boolean, question):
    proceed = True
    if raise_question_boolean == 0:
        proceed = input(question)
    else:
        pass
    if proceed != '1' and proceed != 'y':
        raise SystemExit(0)
    else: pass


def get_root_dirs(input_files_root_dir, contains=[], not_contains=[], print_path = False):
    """Returns all root dirs in input dir    
    
    Parameters
    ----------       
    input_files_root_dir : string
        upmost directory path to start the search        
    contains : list of strings
        strings that should be included in the whole filepath, use | symbol for or statement, for example ['a|b']
    not_contains : list of strings
        strings that should not be included in the whole filepath, use | symbol for or statement, for example ['a|b']
    print_path : bool
        print found path strings
    Returns
    -------
    out : list of strings
        list of whole file paths
    """
    full_paths_list           = []  
    input_files_root_dir      = os.path.normpath(input_files_root_dir)
   
    for root, dirs, files in os.walk(input_files_root_dir):
        for dirr in dirs:
            accept_file = True
            full_path = os.path.join(root, dirr)

            for string in contains:
                if not re.findall(string, dirr):
                    accept_file = False
                else:pass
            
            for string in not_contains:
                if re.findall(string, dirr):
                    accept_file = False
                else:pass
            
            if accept_file:
                full_paths_list.append(full_path)
            else:pass 
        
        break
    full_paths_list.sort()
    if print_path:
        for i in full_paths_list:
            print (i)
    return  full_paths_list
# =============================================================================
# TEST
#path = r"D:/root"
#dirs = get_root_dirs(path, contains=[r'^\d{1,3}_+'], not_contains=[], print_path = True) 
# =============================================================================
    
""" 
===============================================================================
 GET_ALL_FILES_FROM_SUBDIRECTORIES
===============================================================================
"""
def get_files(input_files_root_dir, extension=[], contains=[], not_contains=[], search_subdirs = True, print_path = False):
    """Returns all files in input dir and also all files in all subdirs with selected extension and substring    
    
    Parameters
    ----------       
    input_files_root_dir : string
        upmost directory to start the search        
    extension : list of strings
        allowed file extensions - if empty, all are allowed
    contains : list of strings
        strings that should be included in the whole filepath, use | symbol for or statement, for example ['a|b']
    not_contains : list of strings
        strings that should not be included in the whole filepath, use | symbol for or statement, for example ['a|b']
    print_path : bool
        print found path strings
    search_subdirs : Bool
        sets if subdirs or only root dir should be searched for files
    Returns
    -------
    out : list of strings
        list of whole file paths
    """
    full_paths_list           = []  
    input_files_root_dir      = os.path.normpath(input_files_root_dir)
   
    for root, dirs, files in os.walk(input_files_root_dir):
        for file in files:

            accept_file = False
            full_path = os.path.join(root, file)

            path_without_extension = os.path.normpath(os.path.splitext(full_path)[0])            
            
            ext = os.path.splitext(full_path)[1]

            if len(extension) == 0:
                accept_file = True
            else: pass       
        
            for string in extension:
                if '.{}'.format(string) == ext:
                    accept_file = True
                else: pass
            
            for string in contains:
                if not string in path_without_extension:
                    accept_file = False
                else: pass
            
            for string in not_contains:
                if string in path_without_extension:
                    accept_file = False
                else: pass
            
            if accept_file:
                full_paths_list.append(full_path)
            else: pass 
        
        full_paths_list.sort()
        if not search_subdirs:
            break
        
    if print_path:
        for i in full_paths_list:
            print (i)
            
    return  full_paths_list
# =============================================================================
#TEST
#path = r"U:\delete\aa"
#files = get_files(path, contains=['p'], not_contains=[], search_subdirs = True, extension = [],  print_path = True) 
# =============================================================================
#def get_filesssss(input_files_root_dir, extension=[], contains=[], not_contains=[], search_subdirs = True, print_path = False):
#    """Returns all files in input dir and also all files in all subdirs with selected extension and substring    
#    
#    Parameters
#    ----------       
#    input_files_root_dir : string
#        upmost directory to start the search        
#    extension : list of strings
#        allowed file extensions - if empty, all are allowed
#    contains : list of strings
#        strings that should be included in the whole filepath, use | symbol for or statement, for example ['a|b']
#    not_contains : list of strings
#        strings that should not be included in the whole filepath, use | symbol for or statement, for example ['a|b']
#    print_path : bool
#        print found path strings
#    search_subdirs : Bool
#        sets if subdirs or only root dir should be searched for files
#    Returns
#    -------
#    out : list of strings
#        list of whole file paths
#    """
#    full_paths_list           = []  
#    input_files_root_dir      = os.path.normpath(input_files_root_dir)
#
#    for root, dirs, files in os.walk(input_files_root_dir):
#        for file in files:
#            accept_file = False
#            full_path = os.path.join(root, file)
#            ext = os.path.splitext(full_path)[1]
#
#            if len(extension) == 0:
#                accept_file = True
#            else: pass       
#            for string in extension:
#                if '.{}'.format(string) == ext:
#                    accept_file = True
#                else: pass
#            
#            for string in contains:
#                if not string in full_path:
#                    accept_file = False
#                else: pass
#            
#            for string in not_contains:
#                if string in full_path:
#                    accept_file = False
#                else: pass
#            
#            if accept_file:
#                full_paths_list.append(full_path)
#            else: pass 
#        
#        full_paths_list.sort()
#        if not search_subdirs:
#            break
#        
#    if print_path:
#        for i in full_paths_list:
#            print (i)
#            
#    return  full_paths_list, dirs
# =============================================================================
#TEST
#path = r"X:\Dnox\Tesla\2018"
#files, dirs = get_filesssss(path, contains=['E'], not_contains=[], search_subdirs = False, extension = ['pdf'],  print_path = True) 
# =============================================================================
#filess = []
#
#ss = ''
#gg = '' 
#import PyPDF2
#print()
##dirs = ['E1700071-02']
#o = 0 
#u = 0
#
#for dirr in dirs:
#    files, dirs = get_filesssss('{}/{}'.format(path, dirr), contains=[], not_contains=['Investigation', 'investigation'], search_subdirs = False, extension = ['pdf'],  print_path = False) 
#    if files:
#        o = o + 1
#        pdfFileObj = open(files[0], 'rb')
#         
#        # creating a pdf reader object
#        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#         
#        # printing number of pages in pdf file
#        #print(pdfReader.numPages)
#         
#        # creating a page object
#        pageObj = pdfReader.getPage(0).extractText()
##        print(pageObj)
##        print()
#        i = 0 
##        if 'a' in pageObj: 
#        for line in pageObj.split('\n'):
#            i = i + 1
#            ss = ss + line
#            if i == 27: 
#                if len(ss) > 100:
#                    ss = ss[:100]                    
#                ss = re.sub('.+?(?=E18)', '', ss)
#                ss = re.sub('©.*', '', ss)
##                    ss = re.sub('EDX.*', '', ss)
#                ss = re.sub('Bosch.*', '', ss)
#                ss = re.sub('Robert.*', '', ss)
#                ss = re.sub('s well.*', '', ss)
#                ss = re.sub('disposal.*', '', ss)
#                ss = re.sub('reproduction.*', '', ss)
#                ss = re.sub('reproduction.*', '', ss)
#                ss = re.sub('Page.*', '', ss)
#                ss = re.sub('test.*', 'test', ss)
#                
##                    if 'a' in ss or 'a' in ss:
#                u = u + 1
#                print(files[0])
#                print(ss)                
#                print()
#
#        
#            if i >27:
#                ss = ''
#                gg = ''        
#                break        
#    
##                print(files[0])
#
#
#
#print('number of tests : {}'.format(u))
#
#print('number of files : {}'.format(o))
#
#
#
#
#
#
#
#
#
    
""" 
===============================================================================
 REMOVE_EMPTY_FOLDERS
===============================================================================
"""
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
 
# =============================================================================
# TEST    
# =============================================================================

""" 
===============================================================================
 GET_PART_OF_GIVEN_OS_PATH
===============================================================================
"""
def get_part_of_path(input_dir_name, nth_part):
    """Returns part of given file path
    
    Parameters
    ----------       
    input_dir_name : string
        input directory name        
    nth_part : number
        for example: -2 = last dir, -1 = file name
    Returns
    -------
    out : string
        selected part of input path
    """
    input_dir_name = os.path.normpath(input_dir_name)
    dir_name       = input_dir_name.split(os.sep)[nth_part]   
    return dir_name
# =============================================================================
#TEST     
path1 = r"X:\Dnox\Tesla\2018\E1800002-01\data\recording\hydra_data\ED1800052\BMPviskositatskorrektur\file1.txt"
#print(path1)
#print(get_part_of_path(path1, -1))
#print(get_part_of_path(path1, -2))
#print(get_part_of_path(path1, -3))
# =============================================================================

""" 
===============================================================================
 GET_PARTS_OF_GIVEN_OS_PATH_LIST
===============================================================================
"""
def get_parts_of_paths_list(full_paths_list, nth):
    """Returns part of given file path
    
    Parameters
    ----------    
   
    full_paths_list : list of strings
        input directory names list        
    nth : number
        for example: -2 = last dir, -1 = file name
    Returns
    -------
    out : list of strings
        list of selected parts of input paths list
    """
    name_list  = []     
    for path in full_paths_list:
        name_list.append( get_part_of_path(path, nth) )        
    return name_list
# =============================================================================
# #TEST
#path1 = r"X:\Dnox\Tesla\2018\E1800002-01\data\recording\hydra_data\ED1800052\BMPviskositatskorrektur\file1.txt"
#print(get_parts_of_given_os_path_list(path_list, -1))
#print(get_parts_of_given_os_path_list(path_list, -2))
#print(get_parts_of_given_os_path_list(path_list, -3))
# =============================================================================

""" 
#===============================================================================
# GET CURRENT SCIPT DIR
#===============================================================================
""" 
def get_script_dir(_object):
    """Returns dir path to current script
    
    Parameters
    ----------       
    script attribute:  
        use script attribute __file__ as a parameter
    Returns
    -------
    out : string
        Returns dir path to current script
    """
    script_path = os.path.normpath(os.path.abspath(_object)) 
    return os.path.split(script_path)[0]  

# =============================================================================
# #TEST
#print(get_script_dir(__file__))
# =============================================================================
