ata# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 13:25:11 2018

@author: Carda Zdenek
"""

import functions_io as fio
import functions_mts as fmts
import functions_csv as fcsv
import functions_excel as fexcel
import functions_data_processing as fdp
import functions_plot as fplot
import numpy as np
import matplotlib.pyplot as plt
data = []
handler_map = {}

# =============================================================================
# PLOT BEHAVIOUR SETTINGS
# =============================================================================
USE_LIMIT_LINE                   =  0
USE_AXES_LIMITS                  =  0
USE_GRID                         =  1
SAVE_GRAPH                       =  1
GRAPH_SAVE_PATH                  =  r"X:/Dnox/Tesla/2017/E1700224-08/data/recording/graph.png" 
FIGURE_BACKGROUND_COLOR          = "w"
AXES_BACKGROUND_COLOR            = "w"
GRID_COLOR                       = "k"

# =============================================================================
# LIMIT LABEL ONE AND LINE SETTINGS 
# =============================================================================
LIMIT_LINE_VALUE                 = 75
LIMIT_LINE_COLOR                 = "red"
LIMIT_LABEL                      = "Limit: {} N".format(LIMIT_LINE_VALUE)
# =============================================================================
# PLOT SETTINGS
# =============================================================================



# --------------------------- GRAPH LABELS ------------------------------------
X_AXIS_TITLE                     = "Time[s]"
Y_AXIS_TITLE                     = "Force [N]"
GRAPH_TITLE                      = ""
# -------------------- AXES AND GRAPH LABELS SIZE SETTINGS --------------------
FIGURE_HORIZONTAL_DIMENSION          = 1400/96
FIGURE_VERTICAL_DIMENSION            = 600/96

X_AXIS_LIMITS                    = 0,   10
Y_AXIS_LIMITS                    = 0,   200
X_AXIS_TICKS                     = -1
Y_AXIS_TICKS                     = -1

ALL_TITLES_SIZE_OFFSET           = 4  
X_AXIS_TITLE_SIZE                = 16 
Y_AXIS_TITLE_SIZE                = 16 

X_TICKS_SIZE                     = 14 
Y_TICKS_SIZE                     = 14 

GRAPH_TITLE_SIZE                 = 16 

LEGEND_SIZE                      = 10 
LEGEND_POSITION                  = 2
NUMBER_OF_COLUMNS                = 3
plt.figure(facecolor=FIGURE_BACKGROUND_COLOR , figsize=(FIGURE_HORIZONTAL_DIMENSION, FIGURE_VERTICAL_DIMENSION)) 
axes  = plt.axes(facecolor = AXES_BACKGROUND_COLOR)
   
fplot.set_rc_params()


# =============================================================================
# ROOT DIR SETTINGS  X:\Dnox\Tesla\2017\E1700277-01\data\recording\Assembly_force_not_lubricated
# =============================================================================
d = fmts.Data()
d.root_dir_settings                (  root_dir  = r"X:/Dnox/Tesla/2017/E1700224-08/data/recording/ecr" )
d.excel_settings                   (  save_path = r"X:/Dnox/Tesla/2017/E1700224-08/data/recording/results.xlsx"   )

d.line_calculation_settings        (  calculate = True, x_column = 2, y_colum = 1, read_from_line = 10, read_to_line = None, shift_x_to_zero = None, shift_y_to_zero = True, shift_in_x_axis = None, shift_in_y_axis = None  )

d.line_plot_settings               (  plot="each", color="g",  line_width=1, line_style = "-", marker="",  marker_size=10 )
d.line_label_plot_settings         (  plot="none", text_pref = "", text="ecr", text_post = "", line_width=3, line_style = "-", marker="", special_marker="-", marker_size=10  )

d.derivation_calculation_settings  (  calculate=0, low_treshold= None, high_treshold= None )
d.derivation_plot_settings         (  plot="none", color="blue",  line_width=1, line_style ="-.", marker="",  marker_size=10 )
d.derivation_labels_plot_settings  (  plot="one", text_pref = "", text="ecr", text_post = " der", line_width=1, line_style = "-.", marker="", special_marker="-.", marker_size=10 ) 

d.minimum_calculation_settings     (  calculate=0, method="derivate", low_treshold=5, high_treshold= 8)
d.minimum_values_plot_settings     (  plot="each", color="random",  line_width=10, line_style = "-", marker="*", marker_size=10 )  
d.minimum_labels_plot_settings     (  plot="each", text_pref = "", text="Minimum", text_post = " Ass. min", line_width=0, line_style = "", marker="*", special_marker="x", marker_size=10 )

d.maximum_calculation_settings     (  calculate=1, method="simple", low_treshold=None, high_treshold=None ) 
d.maximum_values_plot_settings     (  plot="each", color="k",  line_width=1, line_style = "-", marker="o", marker_size=10 )
d.maximum_labels_plot_settings     (  plot="one", text_pref = "", text="ecr samples - maximum force", text_post = "", line_width=0, line_style = "", marker="o", special_marker="o", marker_size=10 )
data.append(d)
# =============================================================================
# MAIN LOOP
# =============================================================================

c_map = fmts.ColorMap()  
c_map.assign_new_c_map ( plt.get_cmap("tab10").colors )
a_paths = []

for cur_data in data:
    
    if cur_data.line_calculation_settings_calculate == False:continue
    else: pass
    
    cur_data.root_dir        = fio.get_part_of_path(cur_data.root_dir_settings_root_dir, -1)    
    cur_data.all_files_paths = fio.get_files(cur_data.root_dir_settings_root_dir,["csv"],[],[])
    a_paths                  = fio.get_files(cur_data.root_dir_settings_root_dir)       
    cur_data.file_names      = fio.get_parts_of_paths_list(cur_data.all_files_paths, -1)
    cur_data.last_dirs_names = fio.get_parts_of_paths_list(cur_data.all_files_paths, -2) 

#    root_dir        = fio.get_part_of_given_os_path(cur_data.root_dir_settings_root_dir, -1)    
#    all_files_paths = fio.get_files_from_dirs(cur_data.root_dir_settings_root_dir,[],[], ["csv"])
#    a_paths                  = fio.get_files_from_dirs(cur_data.root_dir_settings_root_dir)       
#    file_names      = fio.get_parts_of_given_os_path_list(cur_data.all_files_paths, -1)
#    last_dirs_names = fio.get_parts_of_given_os_path_list(cur_data.all_files_paths, -2)
    
    
    if  cur_data.line_label_plot_settings_text   == "file_name":
        cur_data.labels_line              = ["{}{}{}".format(cur_data.line_label_plot_settings_text_pref, i, cur_data.line_label_plot_settings_text_post) for i in cur_data.file_names]
    elif cur_data.line_label_plot_settings_text  == "last_dir":
        cur_data.labels_line              = ["{}{}{}".format(cur_data.line_label_plot_settings_text_pref, i, cur_data.line_label_plot_settings_text_post) for i in cur_data.last_dirs_names]        
    else:
        cur_data.labels_line              = ["{}{}{}".format(cur_data.line_label_plot_settings_text_pref, cur_data.line_label_plot_settings_text, cur_data.line_label_plot_settings_text_post) for i in cur_data.file_names]

    if  cur_data.derivation_labels_plot_settings_text   == "file_name":
        cur_data.labels_derivation        = ["{}{}{}".format(cur_data.derivation_labels_plot_settings_text_pref, i, cur_data.derivation_labels_plot_settings_text_post) for i in cur_data.file_names]
    elif cur_data.derivation_labels_plot_settings_text  == "last_dir":
        cur_data.labels_derivation        = ["{}{}{}".format(cur_data.derivation_labels_plot_settings_text_pref, i, cur_data.derivation_labels_plot_settings_text_post) for i in cur_data.last_dirs_names]        
    else:
        cur_data.labels_derivation        = ["{}{}{}".format(cur_data.derivation_labels_plot_settings_text_pref, cur_data.derivation_labels_plot_settings_text, cur_data.derivation_labels_plot_settings_text_post) for i in cur_data.file_names]


    if  cur_data.maximum_labels_plot_settings_text   == "file_name":
        cur_data.labels_maximum           = ["{}{}{}".format(cur_data.maximum_labels_plot_settings_text_pref, i, cur_data.maximum_labels_plot_settings_text_post) for i in cur_data.file_names]
    elif cur_data.maximum_labels_plot_settings_text  == "last_dir":
        cur_data.labels_maximum           = ["{}{}{}".format(cur_data.maximum_labels_plot_settings_text_pref, i, cur_data.maximum_labels_plot_settings_text_post) for i in cur_data.last_dirs_names]        
    else:
        cur_data.labels_maximum           = ["{}{}{}".format(cur_data.maximum_labels_plot_settings_text_pref, cur_data.maximum_labels_plot_settings_text, cur_data.maximum_labels_plot_settings_text_post) for i in cur_data.file_names]


    if  cur_data.minimum_labels_plot_settings_text   == "file_name":
        cur_data.labels_minimum           = ["{}{}{}".format(cur_data.minimum_labels_plot_settings_text_pref, i, cur_data.minimum_labels_plot_settings_text_post) for i in cur_data.file_names]
    elif cur_data.minimum_labels_plot_settings_text  == "last_dir":
        cur_data.labels_minimum           = ["{}{}{}".format(cur_data.minimum_labels_plot_settings_text_pref, i, cur_data.minimum_labels_plot_settings_text_post) for i in cur_data.last_dirs_names]        
    else:
        cur_data.labels_minimum           = ["{}{}{}".format(cur_data.minimum_labels_plot_settings_text_pref, cur_data.minimum_labels_plot_settings_text, cur_data.minimum_labels_plot_settings_text_post) for i in cur_data.file_names]


    for number, file in enumerate(cur_data.all_files_paths):
        print("Processing sample..........{}".format(cur_data.last_dirs_names[number]))        
        
        list_of_lists  = fcsv.read_data_from_csv_file(file, [cur_data.line_calculation_settings_x_column,cur_data.line_calculation_settings_y_column], cur_data.line_calculation_settings_read_from_line, cur_data.line_calculation_settings_read_to_line,0, ";", '"')        
        numpy_2d_array = fdp.nested_list_to_numpy_arr(list_of_lists)
        

        if cur_data.line_calculation_settings_shift_x_to_zero:
            shift = numpy_2d_array[0][0]
            numpy_2d_array[0] -= shift 
            
        if cur_data.line_calculation_settings_shift_y_to_zero:
            shift = numpy_2d_array[1][0]
            numpy_2d_array[1] -= shift 
    
        if cur_data.line_calculation_settings_shift_data_in_x_axis != None : 
            numpy_2d_array[0] += cur_data.line_calculation_settings_shift_data_in_x_axis
            
        if cur_data.line_calculation_settings_shift_data_in_y_axis != None : 
            numpy_2d_array[1] += cur_data.line_calculation_settings_shift_data_in_y_axis            

        if cur_data.derivation_calculation_settings_calculate:
            derivation, low, high = fdp.derivation_calculation_from_value(numpy_2d_array[0],numpy_2d_array[1], cur_data.derivation_calculation_settings_low_treshold, cur_data.derivation_calculation_settings_high_treshold)
    
        if cur_data.minimum_calculation_settings_calculate:
            if cur_data.minimum_calculation_settings_method == "derivate":
                minimum_index, minimum_value = fdp.minimum_index_calculation_from_derivation(numpy_2d_array[0], numpy_2d_array[1], cur_data.minimum_calculation_settings_low_treshold, cur_data.minimum_calculation_settings_high_treshold)
            else:
                minimum_index, minimum_value = fdp.minimum_index_calculation(numpy_2d_array[0],  numpy_2d_array[1], cur_data.minimum_calculation_settings_low_treshold, cur_data.minimum_calculation_settings_high_treshold)

        if cur_data.maximum_calculation_settings_calculate:
            if cur_data.maximum_calculation_settings_method == "derivate":
                maximum_index, maximum_value = fdp.maximum_index_calculation_derivative(numpy_2d_array[0], numpy_2d_array[1], cur_data.maximum_calculation_settings_low_treshold, minimum_index) 
            else:
                maximum_index, maximum_value = fdp.maximum_index_calculation(numpy_2d_array[0], numpy_2d_array[1], cur_data.maximum_calculation_settings_low_treshold, cur_data.maximum_calculation_settings_high_treshold) 
        else:
            pass                                                
                
        # =============================================================================
        # LINE PLOT FOR EACH LINE
        # =============================================================================         
        if cur_data.line_plot_settings_plot == "each" and cur_data.line_plot_settings_color == "random":             
            line, = axes.plot(numpy_2d_array[0], numpy_2d_array[1], c = c_map.get_line_color(), linewidth=cur_data.line_plot_settings_line_width, ls=cur_data.line_plot_settings_line_style, marker=cur_data.line_plot_settings_marker, ms=cur_data.line_plot_settings_marker_size)
        elif cur_data.line_plot_settings_plot == "each" and cur_data.line_plot_settings_color != "random":             
            line, = axes.plot(numpy_2d_array[0], numpy_2d_array[1], color =cur_data.line_plot_settings_color, linewidth=cur_data.line_plot_settings_line_width, ls=cur_data.line_plot_settings_line_style, marker=cur_data.line_plot_settings_marker, ms=cur_data.line_plot_settings_marker_size)
        else:
            pass
        # =============================================================================
        # LINE-LABEL PLOT FOR EACH LINE
        # =============================================================================        
        if cur_data.line_label_plot_settings_plot == "each" and cur_data.line_plot_settings_plot == "each":                                         
            fplot.add_label (cur_data.labels_line[number], line.get_color(), cur_data.line_label_plot_settings_line_width, cur_data.line_label_plot_settings_line_style, cur_data.line_label_plot_settings_marker, cur_data.line_label_plot_settings_marker_size)   
        else:
            pass        
        # =============================================================================
        # DERIVATION LINE PLOT FOR EACH LINE
        # =============================================================================
        if cur_data.derivation_plot_settings_plot == "each" and cur_data.derivation_plot_settings_color == "random" and cur_data.derivation_calculation_settings_calculate: 
            line2, = axes.plot(numpy_2d_array[0][low:high], derivation, color = c_map.get_der_color(), linewidth=cur_data.derivation_plot_settings_line_width, ls=cur_data.derivation_plot_settings_line_style, marker=cur_data.derivation_plot_settings_marker, ms=cur_data.derivation_plot_settings_marker_size)    
        elif cur_data.derivation_plot_settings_plot == "each" and cur_data.derivation_plot_settings_color != "random" and cur_data.derivation_calculation_settings_calculate:  
            line2, = axes.plot(numpy_2d_array[0][low:high], derivation, color =cur_data.derivation_plot_settings_color, linewidth=cur_data.derivation_plot_settings_line_width, ls=cur_data.derivation_plot_settings_line_style, marker=cur_data.derivation_plot_settings_marker, ms=cur_data.derivation_plot_settings_marker_size)            
        else:
            pass
        # =============================================================================
        # DERIVATION LINE-LABEL PLOT FOR EACH LINE
        # =============================================================================       
        if cur_data.derivation_labels_plot_settings_plot == "each" and cur_data.derivation_plot_settings_plot == "each" and cur_data.derivation_calculation_settings_calculate:                                      
            fplot.add_label (cur_data.labels_derivation[number], line2.get_color(), cur_data.derivation_labels_plot_settings_line_width, cur_data.derivation_labels_plot_settings_line_style, cur_data.derivation_labels_plot_settings_marker, cur_data.derivation_labels_plot_settings_marker_size)   
        else:
            pass
        # =============================================================================
        # MINIMUM VALUES PLOT FOR EACH LINE
        # ============================================================================= 
        if cur_data.minimum_values_plot_settings_plot == "each" and cur_data.minimum_values_plot_settings_color == "random" and cur_data.minimum_calculation_settings_calculate: 
            line3, = axes.plot(numpy_2d_array[0][minimum_index], numpy_2d_array[1][minimum_index], color =c_map.get_min_color(), linewidth=cur_data.minimum_values_plot_settings_line_width, ls=cur_data.minimum_values_plot_settings_line_style, marker=cur_data.minimum_values_plot_settings_marker, ms=cur_data.minimum_values_plot_settings_marker_size, zorder=4)    
        elif cur_data.minimum_values_plot_settings_plot == "each" and cur_data.minimum_values_plot_settings_color != "random" and cur_data.minimum_calculation_settings_calculate:  
            line3, = axes.plot(numpy_2d_array[0][minimum_index], numpy_2d_array[1][minimum_index], color = cur_data.minimum_values_plot_settings_color, linewidth=cur_data.minimum_values_plot_settings_line_width, ls=cur_data.minimum_values_plot_settings_line_style, marker=cur_data.minimum_values_plot_settings_marker, ms=cur_data.minimum_values_plot_settings_marker_size, zorder=4)    
        else:
            pass
        # =============================================================================
        # MINIMUM POINTS-LABEL PLOT FOR EACH LINE
        # ============================================================================= 
        if cur_data.minimum_values_plot_settings_plot == "each" and cur_data.minimum_labels_plot_settings_plot == "each" and cur_data.minimum_calculation_settings_calculate:                                      
            fplot.add_label (cur_data.labels_minimum[number], line3.get_color(), cur_data.minimum_labels_plot_settings_line_width, cur_data.minimum_labels_plot_settings_line_style,  cur_data.minimum_labels_plot_settings_marker, cur_data.minimum_labels_plot_settings_marker_size)   
        else:
            pass        
        # =============================================================================
        # MAXIMUM VALUES PLOT FOR EACH LINE
        # ============================================================================= 
        if cur_data.maximum_values_plot_settings_plot == "each" and cur_data.maximum_values_plot_settings_color == "random" and cur_data.maximum_calculation_settings_calculate: 
            line4, = axes.plot(numpy_2d_array[0][maximum_index], numpy_2d_array[1][maximum_index], color =c_map.get_max_color(), linewidth=cur_data.maximum_values_plot_settings_line_width, ls=cur_data.maximum_values_plot_settings_line_style, marker=cur_data.maximum_values_plot_settings_marker, ms=cur_data.maximum_values_plot_settings_marker_size, zorder=4)    
        elif cur_data.maximum_values_plot_settings_plot == "each" and cur_data.maximum_values_plot_settings_color != "random" and cur_data.maximum_calculation_settings_calculate:  
            line4, = axes.plot(numpy_2d_array[0][maximum_index], numpy_2d_array[1][maximum_index], color = cur_data.maximum_values_plot_settings_color, linewidth=cur_data.maximum_values_plot_settings_line_width, ls=cur_data.maximum_values_plot_settings_line_style, marker=cur_data.maximum_values_plot_settings_marker, ms=cur_data.maximum_values_plot_settings_marker_size, zorder=4)    
        else:
            pass
        # =============================================================================
        # MAXIMUM POINTS-LABEL PLOT FOR EACH LINE
        # ============================================================================= 
        if cur_data.maximum_labels_plot_settings_plot == "each" and cur_data.maximum_values_plot_settings_plot == "each" and cur_data.maximum_calculation_settings_calculate:                                      
            fplot.add_label (cur_data.labels_maximum[number] , line4.get_color(), cur_data.maximum_labels_plot_settings_line_width, cur_data.maximum_labels_plot_settings_line_style, cur_data.maximum_labels_plot_settings_marker, cur_data.maximum_labels_plot_settings_marker_size )         
        else:
            pass        
 
        # =============================================================================
        # STORE DATA AFTER LAST EACH FILE
        # =============================================================================
        
        if cur_data.minimum_calculation_settings_calculate: 
            cur_data.minimum_values.append(minimum_value)
            cur_data.minimum_indexes.append(minimum_index)
        if cur_data.maximum_calculation_settings_calculate:
            cur_data.maximum_values.append(maximum_value) 
            cur_data.maximum_indexes.append(maximum_index)
        else:
            pass
            
    # =============================================================================
    # LINE-LABEL PLOT ONCE FOR ROOT DIR
    # =============================================================================        
    if cur_data.line_plot_settings_plot == "each" and cur_data.line_plot_settings_color == "random" and cur_data.line_label_plot_settings_plot == "one":        
        fplot.add_special_label( cur_data.labels_line[0], cur_data.line_label_plot_settings_marker_special)
    elif cur_data.line_plot_settings_plot == "each" and cur_data.line_plot_settings_color != "random" and cur_data.line_label_plot_settings_plot == "one":  
        fplot.add_label ( cur_data.labels_line[0], line.get_color(), cur_data.line_label_plot_settings_line_width, cur_data.line_label_plot_settings_line_style, cur_data.line_label_plot_settings_marker, cur_data.line_label_plot_settings_marker_size)    
    else:
        pass                                 
    # =============================================================================
    # Derivation-LABEL PLOT ONCE FOR ROOT DIR
    # =============================================================================        
    if  cur_data.derivation_calculation_settings_calculate and cur_data.derivation_plot_settings_plot == "each" and cur_data.derivation_plot_settings_color == "random" and cur_data.derivation_labels_plot_settings_plot == "one": 
        fplot.add_special_label(cur_data.labels_derivation[0], cur_data.derivation_labels_plot_settings_marker_special)
    elif cur_data.derivation_calculation_settings_calculate and cur_data.derivation_plot_settings_plot == "each" and cur_data.derivation_plot_settings_color != "random" and cur_data.derivation_labels_plot_settings_plot == "one": 
        fplot.add_label (cur_data.labels_derivation[0] , line2.get_color(), cur_data.derivation_labels_plot_settings_line_width, cur_data.derivation_labels_plot_settings_line_style, cur_data.derivation_labels_plot_settings_marker, cur_data.derivation_labels_plot_settings_marker_size)      
    else:
        pass    
    # =============================================================================
    # MINIMUM-LABEL PLOT ONCE FOR ROOT DIR
    # =============================================================================
    if cur_data.minimum_calculation_settings_calculate and cur_data.minimum_values_plot_settings_plot == "each" and cur_data.minimum_values_plot_settings_color == "random" and cur_data.minimum_labels_plot_settings_plot == "one":        
        fplot.add_special_label(cur_data.labels_minimum[0], cur_data.minimum_labels_plot_settings_marker_special)
    elif cur_data.minimum_calculation_settings_calculate and cur_data.minimum_values_plot_settings_plot == "each" and cur_data.minimum_values_plot_settings_color != "random" and cur_data.minimum_labels_plot_settings_plot == "one":
        fplot.add_label ( cur_data.labels_minimum[0], cur_data.minimum_values_plot_settings_color, cur_data.minimum_labels_plot_settings_line_width, cur_data.minimum_labels_plot_settings_line_style, cur_data.minimum_labels_plot_settings_marker, cur_data.minimum_labels_plot_settings_marker_size)                              
    else:
        pass
    # =============================================================================
    # MAXIMUM-LABEL PLOT ONCE FOR ROOT DIR
    # =============================================================================
    if cur_data.maximum_calculation_settings_calculate and cur_data.maximum_values_plot_settings_plot == "each" and cur_data.maximum_values_plot_settings_color == "random" and cur_data.maximum_labels_plot_settings_plot == "one":        
        fplot.add_special_label(cur_data.labels_maximum[0], cur_data.maximum_labels_plot_settings_marker_special)        
    elif cur_data.maximum_calculation_settings_calculate and cur_data.maximum_values_plot_settings_plot == "each" and cur_data.maximum_values_plot_settings_color != "random" and cur_data.maximum_labels_plot_settings_plot == "one":
        fplot.add_label (cur_data.labels_maximum[0] , cur_data.maximum_values_plot_settings_color, cur_data.maximum_labels_plot_settings_line_width, cur_data.maximum_labels_plot_settings_line_style, cur_data.maximum_labels_plot_settings_marker, cur_data.maximum_labels_plot_settings_marker_size)                              
    else:
        pass

    # =============================================================================
    # CALCULATE MIN, MAX AND AVERAGE VALUE OF DATA
    # =============================================================================
    if cur_data.minimum_calculation_settings_calculate and cur_data.maximum_calculation_settings_calculate:
        
        cur_data.calculate_results()  
        print()
        print("Root dir : {}".format(cur_data.root_dir))
        for number, dir_name, file_name, maximum_value, file in zip( np.arange(len(cur_data.last_dirs_names)), cur_data.last_dirs_names, cur_data.file_names,  cur_data.maximum_values, cur_data.all_files_paths ):                    
            print("{} : {}".format(dir_name, maximum_value))
        print()
        print( "Maximum of values: {}".format(cur_data.maximum_of_values) )
        print( "Minimum of values: {}".format(cur_data.minimum_of_values) )
        print( "Average of values: {}".format(cur_data.average_of_values) )
        print("---------------------------")
        print()        
        cur_data.round_results()
   
    # =============================================================================
    # SAVE DATA TO EXCEL FILE
    # =============================================================================    
    excel = fexcel.Excel()
    w1, w2 = excel.create_workbook(cur_data.excel_settings_save_path)
    excel.write_to_active_worksheet(1,1,"Sample ID")
    next_row = excel.write_range_to_active_worksheet(2,1,cur_data.last_dirs_names)
    excel.write_to_active_worksheet(next_row+1,1,"Maximum value")
    excel.write_to_active_worksheet(next_row+2,1,"Minimum value")
    excel.write_to_active_worksheet(next_row+3,1,"Average value")
            
    excel.write_to_active_worksheet(1,2,"Maximum force")
    next_row = excel.write_range_to_active_worksheet(2,2,cur_data.maximum_values)
    excel.write_to_active_worksheet(next_row+1,2,cur_data.maximum_of_values)
    excel.write_to_active_worksheet(next_row+2,2,cur_data.minimum_of_values)
    excel.write_to_active_worksheet(next_row+3,2,cur_data.average_of_values)  
    
    excel.worksheet.column_dimensions["A"].width = 15
    excel.worksheet.column_dimensions["B"].width = 15
    excel.write_to_active_worksheet(1,4,"File_path")
    next_row = excel.write_range_to_active_worksheet(2,4,cur_data.all_files_paths, True)
   
# =============================================================================
# END OF MAIN LOOP         
# =============================================================================



# =============================================================================
# INSERT CUSTOM CODE HERE
# =============================================================================

#axes.plot(      np.arange( len( data[1].maximum_values ))  ,     data[1].maximum_values  , "ro"     )
#axes.plot(      np.ones( len( data[1].maximum_values ))  ,       data[1].maximum_values  , "bo"     )
#axes.plot(      np.ones( len( data[1].minimum_values ))  ,       data[1].minimum_values  , "go"     )




# =============================================================================
# GENERAL PLOT SETTINGS APPLICATION
# =============================================================================
X_AXIS_TITLE_SIZE += ALL_TITLES_SIZE_OFFSET
Y_AXIS_TITLE_SIZE += ALL_TITLES_SIZE_OFFSET
X_TICKS_SIZE      += ALL_TITLES_SIZE_OFFSET
Y_TICKS_SIZE      += ALL_TITLES_SIZE_OFFSET
GRAPH_TITLE_SIZE  += ALL_TITLES_SIZE_OFFSET
LEGEND_SIZE       += ALL_TITLES_SIZE_OFFSET

    
if USE_LIMIT_LINE:
    plt.plot( [X_AXIS_LIMITS[0],X_AXIS_LIMITS[1] ], [LIMIT_LINE_VALUE, LIMIT_LINE_VALUE], LIMIT_LINE_COLOR, label=LIMIT_LABEL) 
                                               
if USE_AXES_LIMITS:
    plt.xlim( X_AXIS_LIMITS)  
    plt.ylim( Y_AXIS_LIMITS)  
    
if X_AXIS_TICKS != -1:
    plt.xticks(np.arange(  X_AXIS_LIMITS[0]  , X_AXIS_LIMITS[1]+1, X_AXIS_TICKS))

if Y_AXIS_TICKS != -1:
    plt.yticks(np.arange(  Y_AXIS_LIMITS[0]  , Y_AXIS_LIMITS[1]+1, Y_AXIS_TICKS))
           
if USE_GRID :
    plt.grid(color = GRID_COLOR)

axes.legend(ncol = NUMBER_OF_COLUMNS, loc=LEGEND_POSITION, fontsize=LEGEND_SIZE, handler_map=handler_map)     
plt.xlabel(X_AXIS_TITLE, size=X_AXIS_TITLE_SIZE)
plt.ylabel(Y_AXIS_TITLE , size=Y_AXIS_TITLE_SIZE)
plt.title(GRAPH_TITLE, size=GRAPH_TITLE_SIZE)
plt.xticks(fontsize=X_TICKS_SIZE, rotation=0)
plt.yticks(fontsize=Y_TICKS_SIZE, rotation=0)
plt.tight_layout()
 

      
if SAVE_GRAPH:
    plt.savefig(GRAPH_SAVE_PATH, format='png', facecolor=FIGURE_BACKGROUND_COLOR )   















