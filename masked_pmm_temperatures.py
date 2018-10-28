# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:51:33 2018

@author: zdenek
"""

def remap_values(all_possible_values, old_positions):
    old_map            = all_possible_values
    old_map_unique     = np.unique(old_map)           
    new_map_unique     = np.arange(len(old_map_unique))
        
    new_positions = []
    for p in old_positions:
        new_positions.append(new_map_unique[ np.where(old_map_unique == p )][0])
    return old_map_unique, new_map_unique,  new_positions            



plt.ioff()
print('\nGenerating p_diff graphs')
os.makedirs( '{}/{}/{}'.format(cwd, results_dir, p_diff_graphs), exist_ok=True)

samples      = sorted([ a for a in result_frame['sample'].unique()   ])
for sample in samples:
    next_frame = result_frame[result_frame['sample'] == sample]
    pressures     = sorted([ a for a in next_frame['pressure'].unique() ])
    for pressure in pressures:
        next_frame2 = next_frame[next_frame['pressure'] == pressure]       
        voltages     = sorted([ a for a in next_frame2['voltage'].unique()])
        for voltage in voltages: 
            last_frame = next_frame2[next_frame2['voltage'] == voltage]
           
            p_diff_color_map.reset()            
            plt.figure()
            last_frame = last_frame.sort_values(by='temperature')                                  

            xt = np.arange(len(last_frame.temperature.unique()))



            all_possible_x_values  = np.array(last_frame.temperature.tolist()+ [-8,-5,0,10,22,40])            
            
            old_map_unique, new_map_unique,  new_X_positions  = remap_values(all_possible_x_values, last_frame.temperature)

            


            plt.plot(new_X_positions, last_frame.pDiff, color= p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_diff', p_diff_color_map.get_color(True), marker = 'o' )  
           
            for msp, msp_cor, msp_cor_new, temp, pDiff in zip(last_frame.valid_MSP_rate,  last_frame.valid_msp_rate_cor,last_frame.valid_msp_rate_cor2, new_X_positions, last_frame.pDiff ):
                print(msp, msp_cor, msp_cor_new, temp, pDiff)
                plt.annotate("{} \n {} \n {}".format(msp, msp_cor, msp_cor_new), [temp, pDiff], fontsize = 16, fontweight='bold', color='red')

            plt.plot(new_X_positions, last_frame.pDiff_BMP, color = p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_BMP', p_diff_color_map.get_color(True), marker = 'o' ) 
                         
            plt.plot(new_X_positions, last_frame.pDiff_MSP, color = p_diff_color_map.get_color(False), lw = 1, marker = 'o', label = '')
            fplot.add_label('p_MSP', p_diff_color_map.get_color(True), marker = 'o' )                               

            old_positions = [-8,-5,0,10,22,40]
            old_map_unique, new_map_unique,  new_X_positions = remap_values(all_possible_x_values, [-8,-5,0,10,22,40])

            plt.plot(new_X_positions, [-700,-700,-700,-700,-500,-700], 'k', ls = '--')
            plt.plot(new_X_positions, [ 700, 700, 700, 700, 500, 700], 'k', ls = '--')
           
            fplot.set_plot_config('Temperature [°C]', 'Pressure [mbar]',' {}; {} bar; {} V'.format( sample, pressure/1000 ,voltage/1000), ylim = [-2000,None])    
            fplot.modify_ticks(list(map(str, old_map_unique)), new_map_unique, action = "clear", axes_type = 'x')         
            plt.xlim(-0.3,len(new_map_unique))   
            plt.legend(loc = 'lower right')                       
            plt.savefig( '{}/{}/{}/{}_{}_bar_{}_V.png'.format( cwd, results_dir, p_diff_graphs, sample, pressure/1000, voltage/1000))                      
            plt.close()
