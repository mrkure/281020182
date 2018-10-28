# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:54:54 2018

@author: Zdenek
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
handler_map = {}

""" 
===============================================================================
 SET PLOT CONFIG 
===============================================================================
"""
def set_plot_config(xa_label='', ya_label='', title='', xlim = [None, None], ylim = [None,None]):      
    """ Sets many of comonly used plot parameters to standartized values
    
    Parameters
    ----------             
    xa_label : string
        x axis label
    ya_label : string
        y axis label       
    title : string
        title label           
    xlim : list
        x axis limits 
    ylim : list
        y axis limits
    Returns
    -------
    out: 
        none 
    """
    plt.xlabel(xa_label)
    plt.ylabel(ya_label)
    plt.title(title)
     
    plt.xlim(xlim[0],xlim[1])
    plt.ylim(ylim[0],ylim[1])     
    return

# =============================================================================
# TEST
#plt.plot([1,2,3], [1,2,3], 'ro-', label = 'legend label')
#set_plot_config(xa_label='xlabel', ya_label='ylabel', title='title', xlim = [None,100 ], ylim = [None, 100])
# =============================================================================
    
""" 
===============================================================================
 SET RC PARAMS 
===============================================================================
"""
def set_rc_params(font_size_offset = 0, figsize = (1400,600), linewidth = 2, markersize = 6):
    """ Sets comonly used plot parameters to standartized values 

    Parameters
    ----------             
    font_size_offset : integer
        desired offset for titles, ticks, and legend fontsize values
    figsize : tuple of integers
        size of figure in pixels(based on 96dpi monitors)    
    linewidth : integer
        line width           
    markersize : integer
        size of marker
    Returns
    -------
    out: 
        none 
    """
    figsize = (figsize[0]/96, figsize[1]/96)
    mpl.rc('lines', linewidth = linewidth,  markersize = markersize)
    mpl.rc('axes',  titlesize = 16+font_size_offset, labelsize = 14 + font_size_offset, grid = False )
    mpl.rc('xtick', labelsize = 14 + font_size_offset )
    mpl.rc('ytick', labelsize = 14 + font_size_offset ) 
    mpl.rc('legend', fontsize = 14 + font_size_offset )
    mpl.rc('figure', dpi = 96, figsize = figsize, autolayout = True)  
    return
# =============================================================================
# TEST
#set_rc_params(2, (1400,600),4,7)
#plt.plot([1,2,3], [1,2,3], 'ro-', label = 'legend label')
#set_plot_config(xa_label='xlabel', ya_label='ylabel', title='title', xlim = [None,100 ], ylim = [None, 100])
#plt.savefig('D:/a.png')  
#plt.legend()        
# =============================================================================

""" 
===============================================================================
 REMOVE_NONVALID_DATA 
===============================================================================
"""
def remove_nonvalid_data(data, positions):
    """Function removes nan values from nested lists and also removes empty lists from input data, next it removes corresponding values from positions list. Function should be used for boxplot, and violin plots to prevent errors.
    
    Parameters
    ----------       
    data : nested list
        data that should be drawn in violin or boxplot or such plot      
    positions : list 
        positions where data should be drawn
    positions : array like, number
        positions, where violins should be drawn       

    Returns
    -------
    data: nested list
        modified input data nested list 
    positions: list
        modified input parameters list        
    """
    for index, array in enumerate(data):
        data[index] = [x for x in array if (np.isnan(x) == False)]
    pos = []    
    for index, (array, position) in enumerate( zip(data, positions)):
    
        if len(array):

            pos.append(positions[index])
            
    data    = [x for x in data if len(x)] 
    return data,  pos 

# =============================================================================
# TEST
#data = [   [np.nan], [1,2, np.nan, 3], [], [1,np.nan]  ]    
#positions = [1,2,3,4]
#data, positions = remove_nonvalid_data(data, positions)
# =============================================================================

""" 
===============================================================================
 PLOT_VIOLIN
===============================================================================
"""
def plot_violin(arrays, positions, show_means = True, show_medians = False, line_color = "k", med_color = "k", mean_color = "k",  lw = 2,  body_color = "b", opacity = 0.2):
    """Draws violin plot of inserted data sets
    
    Parameters
    ----------             
    arrays : nested array like 
        data that should be drawn, one list is one set of data
    positions : array like, number
        positions, where violins should be drawn
    show_means : boolean
        determines if mean should be drawn
    show_medians : boolean
        determines if medians should be drawn
    line_color : string
        color of the violin plot skeleton
    med_color : string
        color of median line
    mean_color : string
        color of mean line
    lw : int
        width of violin skeleton lines
    body color : string
        color of violin body
    opacity : float
        violin opacity
    Returns
    -------
    out:
        None 
    """    
    arrays, positions = remove_nonvalid_data(arrays, positions)
    t = 0
    for ar in arrays:
        if len(ar):
            t=1
        else:
            pass
    if t == False:
        return        

    violin_parts = plt.violinplot(arrays, positions, showmeans = show_means, showextrema = True, showmedians = show_medians)

    line_width = lw
        
    color_violin_body        = body_color
    color_violin_body_edge   = body_color
    line_w_violin_body_edge  = 2
    opacity_violin_body      = opacity
    
    violin_parts['cmins'].set_facecolor(line_color)
    violin_parts['cmins'].set_edgecolor(line_color)
    violin_parts['cmins'].set_linewidth(line_width)
    violin_parts['cmins'].set_zorder(10)

    violin_parts['cmaxes'].set_facecolor(line_color)  
    violin_parts['cmaxes'].set_edgecolor(line_color)  
    violin_parts['cmaxes'].set_linewidth(line_width)
    violin_parts['cmaxes'].set_zorder(10)
    
    if show_means:  
        violin_parts['cmeans'].set_facecolor(mean_color)  
        violin_parts['cmeans'].set_edgecolor(mean_color)  
        violin_parts['cmeans'].set_linewidth(line_width)
        violin_parts['cmeans'].set_zorder(10)
    
    if show_medians:
        violin_parts['cmedians'].set_facecolor(med_color) 
        violin_parts['cmedians'].set_edgecolor(med_color) 
        violin_parts['cmedians'].set_linewidth(line_width)
        violin_parts['cmedians'].set_zorder(10)
    
    violin_parts['cbars'].set_facecolor(line_color)   
    violin_parts['cbars'].set_edgecolor(line_color)  
    violin_parts['cbars'].set_linewidth(line_width)
    violin_parts['cbars'].set_zorder(10)
    
    for vp in violin_parts['bodies']:
        vp.set_facecolor(color_violin_body)
        vp.set_edgecolor(color_violin_body_edge)
        vp.set_linewidth(line_w_violin_body_edge)
        vp.set_alpha(opacity_violin_body)
    return
# =============================================================================
# TEST
#data1 = [1,2,3,4,5]
#data2 = [9,8,7,6,5]      
#plot_violin([data1,data2], [1,2], opacity = 0.1)   
#plt.plot([1,2],[1,2])      
# =============================================================================

""" 
===============================================================================
 PLOT_SWARM
===============================================================================
"""
def plot_swarm(arrays, positions, color="red", marker = "o", ms = 10, diff=0.1):
    """Draws swarm plot of inserted data sets
    
    Parameters
    ----------      
    axes : axes structure
        plt axes structure        
    arrays : nested array like 
        data that should be drawn, one list is one set of data
    positions : array like, number
        positions, where boxes should be drawn
    colors : string
        color of the swarm points
    diff : float
        seed for random difference between x positions of drawn points       

    Returns
    -------
    out:
    """      
    arrays, positions = remove_nonvalid_data(arrays, positions)
    t = 0
    for ar in arrays:
        if len(ar):
            t=1
        else:
            pass
    if t == False:
        return
    
    for array, position, in zip(arrays, positions):
        rand = np.random.uniform(low = position -diff, high = position + diff, size =  len(array))
        plt.plot( rand, array, linewidth = 0, c= color, marker = marker, ms = ms)        
    return            
# =============================================================================
# TEST    
#data1  = [1,2,3,4,5]
#data2 = [9,8,7,6,5,4]
#plot_swarm([data1, data2], [88,99], color="g", marker= '*')
# =============================================================================

""" 
===============================================================================
 PLOT_BOX
===============================================================================
"""    
def plot_box(arrays, positions, box_color = "k", whis = 1000):
    """Draws boxplot of inserted data sets. Contains function for removing nan and empty values.
    
    Parameters
    ----------      
    axes : axes structure
        plt axes structure        
    arrays : nested array like 
        data that should be drawn, one list is one set of data
    positions : array like, number
        positions, where boxes should be drawn
    box_color : string
        color of the boxes and medians      
    whis : integer
        setw how far should be whiskers drawn
    Returns
    -------
    out:
        None 
    """
    arrays, positions = remove_nonvalid_data(arrays, positions)
    t = 0
    for ar in arrays:
        if len(ar):
            t=1
        else:
            pass
    if t == False:
        return    
    
    
    zorder = 10
    aa = plt.boxplot(arrays, positions = positions, zorder = zorder, showmeans = False, whis = whis )
 
    bb = aa["means"]
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2)
        line.set_zorder(zorder)
    bb = aa["medians"]
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2) 
        line.set_zorder(zorder)              
    bb = aa["boxes"]      
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2) 
        line.set_zorder(zorder)         
    bb = aa["whiskers"]    
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2)
        line.set_zorder(zorder)
    bb = aa["fliers"]    
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2)
        line.set_zorder(zorder)
    bb = aa["caps"]    
    for line in bb:
        line.set_color(box_color)
        line.set_linewidth(2)
        line.set_zorder(zorder)
    return
# =============================================================================
# TEST    
#data1  = [1,2,3,4,5]
#data2 = [9,8,7,6,5,4,30]
#plot_box([data1, data2], [88,99], box_color="k")
# =============================================================================

""" 
===============================================================================
 MODIFY_TICKS
===============================================================================
"""
def modify_ticks(new_labels, new_locations, action = "clear", axes_type = 'x'):
    """Adds ticks to current x_axes. Ticks are added in addition to curent ticks,
    when collision between old and new tick happens, it can be decided which ones should be kept
    
    Parameters
    ----------       
    tick_labels : list, string
        text shown on X axes for each box
    tick_positions : list, number
        positions, where labels on x axes should be drawn
    action : string
        clear - remove all old labels\n
        update - rewrite all old labels with the same axes position\n
        keep - keps all old labels with the same axes position
    axes_type : string 
        x or y axes
    Returns
    -------
    out:
        None 
    """
    old_locations, old_labels = plt.xticks()
    old_labels       = [a.get_text() for a in old_labels]  
    old_locations    = list(old_locations)
    result_labels    = []
    result_locations = []
  
    if action == "clear":
        result_labels    = new_labels
        result_locations = new_locations       

    elif action == "keep":
        result_labels.extend(old_labels)
        result_labels.extend(new_labels)
        result_locations.extend(old_locations)
        result_locations.extend(new_locations)

    elif action == "update":         
        result_labels.extend(new_labels)
        result_labels.extend(old_labels)
        result_locations.extend(new_locations)
        result_locations.extend(old_locations)
        
    else :pass

    for i, value in enumerate(result_locations):
        for j, value2 in enumerate(result_locations[i+1:]):
            if value == value2:
                result_locations[j+i+1] = None
                result_labels[j+i+1]    = None            
            else: pass
    
    result_locations = list(filter(lambda x : x != None, result_locations))         
    result_labels    = list(filter(lambda x : x != None, result_labels)) 

    if axes_type == "x":
        plt.xticks(result_locations, result_labels)
    if axes_type == "y":
        plt.yticks(result_locations, result_labels)
    return
# =============================================================================
# TEST
#plt.xlim = (0,10)
#plt.plot([1,20],[1,1])    
#plt.xticks([1,5,10,15, 12, 15], ['one', 'five', 'ten', 'fifteen', 'twelve', '\n fifteren'])
#modify_ticks(["\n01", "\n02", "\n03", "\n04", "\n08"],  [1,2,3,4,8],"keep" )
#modify_ticks(["1", "2", "3", "8", '12'],  [1,2,3,8, 12],"keep" )
# =============================================================================

""" 
===============================================================================
 STARS
===============================================================================
"""
class Stars(object):
    """Patch object used to add special tri-color label to curent plot
    """
    def __init__(self, multi):
        self.multi = multi
        return
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

        horizontal_shift = -5
        vertical_shift   = 0
        multiplicator    = 0.6
        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([10  + horizontal_shift,15  + vertical_shift])  * multiplicator
        n3 = np.array([20  + horizontal_shift,0   + vertical_shift])  * multiplicator

        n4 = np.array([0 + horizontal_shift,10  + vertical_shift])   * multiplicator
        n5 = np.array([20 + horizontal_shift,10 + vertical_shift])   * multiplicator
        n6 = np.array([10 + horizontal_shift,-5 + vertical_shift])   * multiplicator

        patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='r')
        patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='r')

        handlebox.add_artist(patch1)
        handlebox.add_artist(patch2)

        horizontal_shift = 16
        vertical_shift   = 0
      
        n1 = np.array([0  + horizontal_shift,0 + vertical_shift]) * multiplicator
        n2 = np.array([10 + horizontal_shift,15 + vertical_shift])  * multiplicator
        n3 = np.array([20 + horizontal_shift,0 + vertical_shift])  * multiplicator

        n4 = np.array([0+ horizontal_shift,10+ vertical_shift])  * multiplicator
        n5 = np.array([20 + horizontal_shift,10 + vertical_shift])  * multiplicator
        n6 = np.array([10+ horizontal_shift,-5+ vertical_shift])  * multiplicator
       
        patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='g')
        patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='g')
        
        handlebox.add_artist(patch1)
        handlebox.add_artist(patch2)
        
        horizontal_shift = 37
        vertical_shift   = 0
        
        n1 = np.array([0 + horizontal_shift,0  + vertical_shift]) * multiplicator
        n2 = np.array([10+ horizontal_shift,15 + vertical_shift]) * multiplicator
        n3 = np.array([20+ horizontal_shift,0 + vertical_shift])  * multiplicator

        n4 = np.array([0 + horizontal_shift,10 + vertical_shift])  * multiplicator
        n5 = np.array([20+ horizontal_shift,10 + vertical_shift])  * multiplicator
        n6 = np.array([10+ horizontal_shift,-5 + vertical_shift])  * multiplicator
       
        patch1 = mpatches.Polygon([n1,n2,n3 ], closed=True, color='b')
        patch2 = mpatches.Polygon([n4,n5,n6] , closed=True, color='b')
        
        handlebox.add_artist(patch1)
        handlebox.add_artist(patch2)
        return 
""" 
===============================================================================
 CIRCLES
===============================================================================
"""
class Circles(object):
    """Patch object used to add special tri-color label to curent plot
    """
    def __init__(self, multi):
        self.multi = multi
        return
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

        horizontal_shift = 3
        vertical_shift   = 5
        multiplicator    = 0.7
        
        patch1 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="r")        
        handlebox.add_artist(patch1)
        
        horizontal_shift = 15
        patch2 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="g")                
        handlebox.add_artist(patch2)
        
        horizontal_shift = 27
        patch3 = mpatches.Circle((0 + horizontal_shift,0 + vertical_shift),radius=7 * multiplicator, color="b")                
        handlebox.add_artist(patch3)
        return 
""" 
===============================================================================
 CROSSES
===============================================================================
"""
class Crosses(object):
    """Patch object used to add special tri-color label to curent plot
    """
    def __init__(self, multi):
        self.multi = multi
        return
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

        horizontal_shift = -3
        vertical_shift   = 0
        multiplicator    = 0.9

        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
        n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
        n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
        
        patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='r')      
        handlebox.add_artist(patch1)
        patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='r')      
        handlebox.add_artist(patch1)
        
        horizontal_shift   = 10        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
        n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
        n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
        
        patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='g')      
        handlebox.add_artist(patch1)
        patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='g')      
        handlebox.add_artist(patch1)
        
        horizontal_shift   = 23         
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([10  + horizontal_shift,10  + vertical_shift])  * multiplicator
        n3 = np.array([0   + horizontal_shift,10  + vertical_shift])   * multiplicator
        n4 = np.array([10  + horizontal_shift,0  + vertical_shift])  * multiplicator
        
        patch1 = mpatches.Polygon([n1,n2 ], closed=False,lw= 2,  color='b')      
        handlebox.add_artist(patch1)
        patch1 = mpatches.Polygon([n3,n4 ], closed=False, lw= 2, color='b')      
        handlebox.add_artist(patch1)
        return
""" 
===============================================================================
 LINES
===============================================================================
"""
class Lines(object):
    """Patch object used to add special tri-color label to curent plot
    """
    def __init__(self, multi):
        self.multi = multi
        return
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

        horizontal_shift = 0
        vertical_shift   = 0
        multiplicator    = 1

        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 5        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 10         
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
        n2 = np.array([30  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
        handlebox.add_artist(patch1)        
        return
""" 
===============================================================================
 DASH_LINES
===============================================================================
"""
class Dash_lines(object):
    """Patch object used to add special tri-color label to curent plot
    """
    def __init__(self, multi):
        self.multi = multi
        return
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

        horizontal_shift = 0
        vertical_shift   = 0
        multiplicator    = 1

        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
        handlebox.add_artist(patch1)
       
        vertical_shift   = 5        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
        handlebox.add_artist(patch1)

       
        vertical_shift   = 10 
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
        handlebox.add_artist(patch1)  
   
        vertical_shift   = 0 
        horizontal_shift = 10
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 5
        horizontal_shift = 10        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 10   
        horizontal_shift = 10
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 0   
        horizontal_shift = 20        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1, n2], closed=False,lw= 2,  color='r')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 5   
        horizontal_shift = 20        
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])   * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='g')      
        handlebox.add_artist(patch1)
        
        vertical_shift   = 10   
        horizontal_shift = 20       
        n1 = np.array([0   + horizontal_shift,0  + vertical_shift])  * multiplicator
        n2 = np.array([8  + horizontal_shift,0  + vertical_shift])  * multiplicator        
        patch1 = mpatches.Polygon([n1,n2], closed=False,lw= 2,  color='b')      
        handlebox.add_artist(patch1)        
        return

""" 
===============================================================================
 ADD_LABEL
===============================================================================
"""
def add_label (label, line_color,  line_width = 2, line_style = '-', marker = '', marker_size = 6):
    """Adds special tri-color legend label to curent plot
    
    Parameters
    ---------- 
    label : string
        legend label string    
    line_color : string
        color of label object        
    line_width : int
        line width if there is a line
    line_style : string
        possible options - -, --, -., :      
    marker : string
        possible options - *,o,x,x and more.. 
    marker_size : int
        size of the marker
    Returns
    -------
    out:
        None 
    """
    plt.plot([], [], c = line_color, linewidth = line_width, ls = line_style, marker= marker, ms =marker_size, label = label)
    plt.legend(handler_map=handler_map)
    return 
# =============================================================================
# TEST
#plt.plot([1,2,3], [1,2,3])  
#add_label ('label', 'r', line_width = 0, marker = '*')     
#add_label ('label 2', 'b')  
#plt.legend()
# =============================================================================

""" 
===============================================================================
 ADD_SPECIAL_LABEL
===============================================================================
"""
def add_special_label (label, symbol):
    """Adds special tri-color legend label to curent plot
    
    Parameters
    ----------           
    symbol : string
        possible options - *, o, x, -, -.
    label : string
        legend label text       
    Returns
    -------
    out:
        None 
    """    
    if symbol == "*":        
        handler_map.update({plt.plot([],[] , label = label)[0]:Stars(10)})  
    if symbol == "o":        
        handler_map.update({plt.plot([],[] , label = label)[0]:Circles(10)}) 
    if symbol == "x":        
        handler_map.update({plt.plot([],[] , label = label)[0]:Crosses(10)}) 
    if symbol == "-":        
        handler_map.update({plt.plot([],[] , label = label)[0]:Lines(10)}) 
    if symbol == "-.":        
        handler_map.update({plt.plot([],[] , label = label)[0]:Dash_lines(10)})
    plt.legend(handler_map=handler_map)
    return
# =============================================================================
# TEST
#set_rc_params(font_size_offset = 0, figsize = (1400,600), linewidth = 2, markersize = 6)
#plt.plot([1,2,3], [1,2,3])  
#add_special_label ('special label 1', '*') 
#add_label ('label', 'r', line_width = 10)     
#plt.plot([1],[1],'r-',lw =2, label = 'asdf')  
#add_special_label ('special label 2', 'o')  
# =============================================================================

""" 
===============================================================================
 C_map
===============================================================================
"""
class C_map():
    """ Class should be used for setting plot colors rotations   
 
    """
    def __init__(self, arg = None):         
        """Assings new custom color map
        
        Parameters
        ----------    
        arg : list or none
            custom list of colors - ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']  
        Notes
        -----
        base map - ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon', 'gold', 'darkred', 'darkblue']
        """  
        if arg:
            self.colors = arg
            self.pointer = 0
            self.number_of_colors = len(self.colors)            
                            
        else:
            self.pointer = 0
            self.colors           = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'pink', 'brown', 'orange', 'teal', 'coral', 'lightblue', 'lime', 'lavender', 'turquoise', 'darkgreen', 'tan', 'salmon', 'gold', 'darkred', 'darkblue']
            self.number_of_colors = len(self.colors)
        return
    
    def reset(self):
        """Set color pointer to first color in colors sequence
        
        Parameters
        ----------    
        param :  
            none      
        Returns
        -------
        out:
            None 
        """
        self.pointer = 0
        return
    
    def new_map(self, c_map):
        """Assings new custom color map
        
        Parameters
        ----------    
        c_map : list 
            custom list of colors, for example ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']      
        Returns
        -------
        out:
            None 
        """
        self.pointer = 0 
        self.colors = c_map
        self.number_of_colors = len(self.colors)        
        return

    def get_color(self, set_next = True):
        """Returns current color and set pointer to next color in colors sequence
        
        Parameters
        ----------    
        set_next : boolean 
            set next color in colors sequence or keep current color     
        Returns
        -------
        color: string
            current color in sequence 
      
        """        
        if self.pointer == self.number_of_colors-1: 
            if set_next:
                self.current_color = self.colors[self.pointer]            
                self.pointer = 0
            else:
                self.current_color = self.colors[self.pointer]                       
        else:
            if set_next:
                self.current_color = self.colors[self.pointer] 
                self.pointer += 1                
            else:
                self.current_color = self.colors[self.pointer]                 
                
        return self.current_color                
                
# =============================================================================
# TEST
#cmap = C_map(['grey', 'green', 'yellow'])
#cmap.new_map(['black', 'yellow', 'red'])  
#print(cmap.get_color(True))
#print(cmap.get_color(False))
#print(cmap.get_color(True))
#cmap.reset()
#print(cmap.get_color(True))              
# =============================================================================
 


























