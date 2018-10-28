# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:24:10 2018

@author: Carda Zdenek
"""
import numpy as np
import matplotlib.patches as mpatches





class Data():
    def __init__(self):

        self.root_dir_settings_read_data                            = None        
        self.root_dir_settings_root_dir                             = None
        
        self.excel_settings_save_path                               = None 
        self.excel_settings_save_data                               = None 
        
        self.line_calculation_settings_calculate                    = None
        self.line_calculation_settings_x_column                     = None
        self.line_calculation_settings_y_column                     = None
        self.line_calculation_settings_read_from_line               = None
        self.line_calculation_settings_read_to_line                 = None
        self.line_calculation_settings_shift_x_to_zero              = None
        self.line_calculation_settings_shift_y_to_zero              = None
        self.line_calculation_settings_shift_data_in_x_axis         = None
        self.line_calculation_settings_shift_data_in_y_axis         = None
        
        self.derivation_calculation_settings_calculate              = None
        self.derivation_calculation_settings_low_treshold           = None
        self.derivation_calculation_settings_high_treshold          = None 
        
        self.minimum_calculation_settings_calculate                 = None
        self.minimum_calculation_settings_method                    = None
        self.minimum_calculation_settings_low_treshold              = None
        self.minimum_calculation_settings_high_treshold             = None        
        
        self.maximum_calculation_settings_calculate                 = None
        self.maximum_calculation_settings_method                    = None
        self.maximum_calculation_settings_low_treshold              = None
        self.maximum_calculation_settings_high_treshold             = None 
      
        self.line_plot_settings_plot                                = None
        self.line_plot_settings_color                               = None
        self.line_plot_settings_line_style                          = None 
        self.line_plot_settings_line_width                          = None
        self.line_plot_settings_marker                              = None
        self.line_plot_settings_marker_size                         = None 
        
        self.line_label_plot_settings_plot                          = None
        self.line_label_plot_settings_text_pref                     = None
        self.line_label_plot_settings_text_post                     = None        
        self.line_label_plot_settings_text                          = None
        self.line_label_plot_settings_color                         = None
        self.line_label_plot_settings_line_style                    = None        
        self.line_label_plot_settings_line_width                    = None
        self.line_label_plot_settings_marker                        = None
        self.line_label_plot_settings_marker_special                = None
        self.line_label_plot_settings_marker_size                   = None

        self.derivation_plot_settings_plot                          = None
        self.derivation_plot_settings_color                         = None
        self.derivation_plot_settings_line_style                    = None
        self.derivation_plot_settings_line_width                    = None
        self.derivation_plot_settings_marker                        = None
        self.derivation_plot_settings_marker_size                   = None

        
        self.derivation_labels_plot_settings_plot                   = None
        self.derivation_labels_plot_settings_text_pref              = None
        self.derivation_labels_plot_settings_text_post              = None        
        self.derivation_labels_plot_settings_text                   = None
        self.derivation_labels_plot_settings_color                  = None
        self.derivation_labels_plot_settings_line_style             = None
        self.derivation_labels_plot_settings_line_width             = None
        self.derivation_labels_plot_settings_marker                 = None        
        self.derivation_labels_plot_settings_marker_special         = None
        self.derivation_labels_plot_settings_marker_size            = None
        
        self.minimum_values_plot_settings_plot                      = None
        self.minimum_values_plot_settings_color                     = None
        self.minimum_values_plot_settings_line_style                = None 
        self.minimum_values_plot_settings_line_width                = None 
        self.minimum_values_plot_settings_marker                    = None
        self.minimum_values_plot_settings_marker_size               = None
        
        self.minimum_labels_plot_settings_plot                      = None
        self.minimum_labels_plot_settings_text_pref                 = None
        self.minimum_labels_plot_settings_text_post                 = None        
        self.minimum_labels_plot_settings_text                      = None
        self.minimum_labels_plot_settings_color                     = None
        self.minimum_labels_plot_settings_line_style                = None
        self.minimum_labels_plot_settings_line_width                = None
        self.minimum_labels_plot_settings_marker_special            = None        
        self.minimum_labels_plot_settings_marker                    = None
        self.minimum_labels_plot_settings_marker_size               = None
        
        self.maximum_values_plot_settings_plot                      = None
        self.maximum_values_plot_settings_color                     = None
        self.maximum_values_plot_settings_line_style                = None
        self.maximum_values_plot_settings_line_width                = None
        self.maximum_values_plot_settings_marker                    = None
        self.maximum_values_plot_settings_marker_size               = None
        
        self.maximum_labels_plot_settings_plot                      = None
        self.maximum_labels_plot_settings_text_pref                 = None
        self.maximum_labels_plot_settings_text_post                 = None
        self.maximum_labels_plot_settings_text                      = None
        self.maximum_labels_plot_settings_color                     = None
        self.maximum_labels_plot_settings_line_style                = None
        self.maximum_labels_plot_settings_line_width                = None
        self.maximum_labels_plot_settings_marker                    = None
        self.maximum_labels_plot_settings_marker_special            = None
        self.maximum_labels_plot_settings_marker_size               = None  
        
        
        self.maximum_values                                         = []
        self.minimum_values                                         = []
        self.maximum_indexes                                        = []
        self.minimum_indexes                                        = []
        self.average_of_values                                      = None
        self.minimum_of_values                                      = None
        self.maximum_of_values                                      = None


        self.root_dir                                               = None
        self.all_files_paths                                        = None
        self.file_names                                             = None
        self.last_dirs_names                                        = None
        self.labels_line                                            = None
        self.labels_derivation                                      = None
        self.labels_minimum                                         = None
        self.labels_maximum                                         = None
        


        
    def calculate_results(self):
        
        self.maximum_of_values = np.max (np.array(self.maximum_values))         
        self.minimum_of_values = np.min (np.array(self.maximum_values))        
        self.average_of_values = np.mean(np.array(self.maximum_values))

    def round_results(self):
        self.maximum_of_values = np.round(self.maximum_of_values,1)
        self.minimum_of_values = np.round(self.minimum_of_values,1)     
        self.average_of_values = np.round(self.average_of_values,1) 
        self.maximum_values    = np.round(self.maximum_values,1) 


    def root_dir_settings(self, root_dir = "none", read_data = 0):
        self.root_dir_settings_root_dir                        = root_dir
        self.root_dir_settings_read_data                            = read_data

    def excel_settings(self, save_path = "none", save_data = False):
        self.excel_settings_save_path                               = save_path 
        self.excel_settings_save_data                               = save_data  
        
    def line_calculation_settings(self, calculate = True, x_column = 0, y_colum = 0, read_from_line = None, read_to_line = None, shift_x_to_zero = None, shift_y_to_zero = None,  shift_in_x_axis = None, shift_in_y_axis = None):
        self.line_calculation_settings_calculate                    = calculate
        self.line_calculation_settings_x_column                     = x_column
        self.line_calculation_settings_y_column                     = y_colum
        self.line_calculation_settings_read_from_line               = read_from_line
        self.line_calculation_settings_read_to_line                 = read_to_line
        self.line_calculation_settings_shift_x_to_zero              = shift_x_to_zero
        self.line_calculation_settings_shift_y_to_zero              = shift_y_to_zero
        self.line_calculation_settings_shift_data_in_x_axis         = shift_in_x_axis
        self.line_calculation_settings_shift_data_in_y_axis         = shift_in_y_axis                

    def derivation_calculation_settings(self, calculate=True, low_treshold=None, high_treshold=None):
        self.derivation_calculation_settings_calculate                 = calculate
        self.derivation_calculation_settings_low_treshold              = low_treshold
        self.derivation_calculation_settings_high_treshold             = high_treshold 


    def minimum_calculation_settings(self, calculate=True, method="simple", low_treshold=None, high_treshold=None):
        self.minimum_calculation_settings_calculate                 = calculate
        self.minimum_calculation_settings_method                    = method
        self.minimum_calculation_settings_low_treshold              = low_treshold
        self.minimum_calculation_settings_high_treshold             = high_treshold 
        
    def maximum_calculation_settings(self, calculate=True, method = "simple", low_treshold=None, high_treshold=None):        
        self.maximum_calculation_settings_calculate                 = calculate
        self.maximum_calculation_settings_method                    = method
        self.maximum_calculation_settings_low_treshold              = low_treshold
        self.maximum_calculation_settings_high_treshold             = high_treshold

    def line_plot_settings(self, plot="all", color="random", line_width=2, line_style = "-", marker="", marker_size=10):
        self.line_plot_settings_plot                                = plot
        self.line_plot_settings_color                               = color
        self.line_plot_settings_line_style                          = line_style
        self.line_plot_settings_line_width                          = line_width
        self.line_plot_settings_marker                              = marker
        self.line_plot_settings_marker_size                         = marker_size 
    
    def line_label_plot_settings(self, plot="each", text_pref = "", text="last_dir_name", text_post = "", color="line_color", line_width="line_width", line_style = "-", marker="o", special_marker="*", marker_size=10 ):
        self.line_label_plot_settings_plot                          = plot
        self.line_label_plot_settings_text_pref                     = text_pref
        self.line_label_plot_settings_text_post                     = text_post
        self.line_label_plot_settings_text                          = text
        self.line_label_plot_settings_color                         = color
        self.line_label_plot_settings_line_style                    = line_style
        self.line_label_plot_settings_line_width                    = line_width
        self.line_label_plot_settings_marker                        = marker
        self.line_label_plot_settings_marker_special                = special_marker
        self.line_label_plot_settings_marker_size                   = marker_size  
                
    def derivation_plot_settings(self, plot="all", color="random", line_width=2, line_style="-", marker="", marker_size=10):
        self.derivation_plot_settings_plot                          = plot
        self.derivation_plot_settings_color                         = color        
        self.derivation_plot_settings_line_style                    = line_style       
        self.derivation_plot_settings_line_width                    = line_width
        self.derivation_plot_settings_marker                        = marker
        self.derivation_plot_settings_marker_size                   = marker_size                
        
    def derivation_labels_plot_settings(self, plot="each", text_pref = "", text="last_dir", text_post = "", line_width = 1, line_style = "-", color="custom", marker="custom",special_marker="*", marker_size=10 ):
        self.derivation_labels_plot_settings_plot                   = plot
        self.derivation_labels_plot_settings_text_pref              = text_pref
        self.derivation_labels_plot_settings_text_post              = text_post 
        self.derivation_labels_plot_settings_text                   = text
        self.derivation_labels_plot_settings_color                  = color
        self.derivation_labels_plot_settings_line_style             = line_style        
        self.derivation_labels_plot_settings_line_width             = line_width
        self.derivation_labels_plot_settings_marker                 = marker
        self.derivation_labels_plot_settings_marker_special         = special_marker
        self.derivation_labels_plot_settings_marker_size            = marker_size           

    def minimum_values_plot_settings(self, plot="none", color="custom_color", line_width = 1, line_style = "-",  marker="o", marker_size=10):
        self.minimum_values_plot_settings_plot                      = plot
        self.minimum_values_plot_settings_color                     = color
        self.minimum_values_plot_settings_line_style                = line_style       
        self.minimum_values_plot_settings_line_width                = line_width
        self.minimum_values_plot_settings_marker                    = marker
        self.minimum_values_plot_settings_marker_size               = marker_size        

    def minimum_labels_plot_settings(self, plot="each", text_pref = "", text="last_dir", text_post = "", line_width = 1, line_style = "-", color="custom", marker="custom", special_marker="*", marker_size=10):
        self.minimum_labels_plot_settings_plot                      = plot
        self.minimum_labels_plot_settings_text_pref                 = text_pref
        self.minimum_labels_plot_settings_text_post                 = text_post 
        self.minimum_labels_plot_settings_text                      = text
        self.minimum_labels_plot_settings_color                     = color
        self.minimum_labels_plot_settings_line_style                = line_style
        self.minimum_labels_plot_settings_line_width                = line_width
        self.minimum_labels_plot_settings_marker                    = marker
        self.minimum_labels_plot_settings_marker_special            = special_marker
        self.minimum_labels_plot_settings_marker_size               = marker_size
        
    def maximum_values_plot_settings(self, plot="none", line_width = 1, line_style = "-", color="custom_color", marker="o", marker_size=10):
        self.maximum_values_plot_settings_plot                      = plot
        self.maximum_values_plot_settings_color                     = color
        self.maximum_values_plot_settings_line_style                = line_style
        self.maximum_values_plot_settings_line_width                = line_width
        self.maximum_values_plot_settings_marker                    = marker
        self.maximum_values_plot_settings_marker_size               = marker_size        

    def maximum_labels_plot_settings(self, plot="each", line_width = 1, line_style = "-", text_pref = "", text="last_dir", text_post = "", color="k", marker="o", special_marker="*", marker_size=10):
        self.maximum_labels_plot_settings_plot                      = plot
        self.maximum_labels_plot_settings_text_pref                 = text_pref
        self.maximum_labels_plot_settings_text_post                 = text_post
        self.maximum_labels_plot_settings_text                      = text
        self.maximum_labels_plot_settings_color                     = color
        self.maximum_labels_plot_settings_line_style                = line_style
        self.maximum_labels_plot_settings_line_width                = line_width
        self.maximum_labels_plot_settings_marker                    = marker
        self.maximum_labels_plot_settings_marker_special            = special_marker
        self.maximum_labels_plot_settings_marker_size               = marker_size
        


""" 
#===============================================================================
# COLORMAP
#===============================================================================
"""
class ColorMap():
    """custom color map object, that rotates throw custom color sequence
    
    Parameters
    ----------    
    param :  
        none   
  
    Returns
    -------
    out:
        None 
        
    Notes
    -----
    None

    Examples
    --------
    None       
   
    """
    def __init__(self):            
        self.colors = []
        self.current_color    = None
        self.line_pointer     = 0
        self.der_pointer      = 0
        self.min_pointer      = 0
        self.max_pointer      = 0
        self.colors           = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon', 'gold', 'darkred', 'darkblue']
        self.number_of_colors = len(self.colors)

        return

    def assign_new_c_map(self, c_map):
        """Assings new custom color map
        
        Parameters
        ----------    
        c_map : list 
            custom list of colors - ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']  
    
        Returns
        -------
        out:
            None 
            
        Notes
        -----
        None
    
        Examples
        --------
        None       
       
        """
        self.colors = c_map
        self.number_of_colors = len(c_map) 
        return
    
    def get_line_color(self):
        """Returns curent color in rotation and points to next color
        
        Parameters
        ----------    
        param :  
            none 
    
        Returns
        -------
        out: string
            curent color 
            
        Notes
        -----
        None
    
        Examples
        --------
        None       
       
        """
        if self.line_pointer == self.number_of_colors-1:
            self.line_pointer = 0
            
        self.current_color = self.colors[self.line_pointer]
        self.line_pointer += 1
        return self.current_color
        
    def get_der_color(self):
        """Returns curent color in rotation and points to next color
        
        Parameters
        ----------    
        param :  
            none 
    
        Returns
        -------
        out: string
            curent color 
            
        Notes
        -----
        None
    
        Examples
        --------
        None       
       
        """
        if self.der_pointer == self.number_of_colors-1:
            self.der_pointer = 0
            
        self.current_color = self.colors[self.der_pointer]
        self.der_pointer += 1
        return self.current_color
    
    def get_min_color(self):
        """Returns curent color in rotation and points to next color
        
        Parameters
        ----------    
        param :  
            none 
    
        Returns
        -------
        out: string
            curent color 
            
        Notes
        -----
        None
    
        Examples
        --------
        None       
       
        """
        if self.min_pointer == self.number_of_colors-1:
            self.min_pointer = 0
            
        self.current_color = self.colors[self.min_pointer]
        self.min_pointer += 1
        return self.current_color
    
    def get_max_color(self):
        """Returns curent color in rotation and points to next color
        
        Parameters
        ----------    
        param :  
            none 
    
        Returns
        -------
        out: string
            curent color 
            
        Notes
        -----
        None
    
        Examples
        --------
        None       
       
        """
        if self.max_pointer == self.number_of_colors-1:
            self.max_pointer = 0
            
        self.current_color = self.colors[self.max_pointer]
        self.max_pointer += 1
        return self.current_color