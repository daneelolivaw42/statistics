#%%
from xmlrpc.client import boolean
import matplotlib.pyplot as plt
import numpy as np

def scatter_plot(plot_data, style_plot:dict):
    plt.figure(figsize = style_plot['plot_template']['plot_size'])
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
    plt.rcParams['xtick.major.size'] = 6
    plt.rcParams['xtick.major.width'] = 4
    plt.rcParams['ytick.major.size'] = 6
    plt.rcParams['ytick.major.width'] = 4
    plt.rcParams['xtick.bottom'] = True
    plt.rcParams['ytick.left'] = True
    ax = plt.gca()
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(style_plot['plot_template']['plot_line_width'])
        ax.spines[axis].set_color(style_plot['plot_template']['main_text_color'])
    ax.tick_params(axis='x', colors = style_plot['plot_template']['main_text_color'], labelsize=18)
    ax.tick_params(axis='y', colors = style_plot['plot_template']['main_text_color'], labelsize=18)
    ax.grid(color = style_plot['plot_template']['grid_color'], linestyle='-', linewidth=1.5)
    ax.set_ylabel(plot_data['y_label'], fontsize = style_plot['plot_template']['label_font_size'], color = style_plot['plot_template']['main_text_color'], fontweight='bold')
    ax.set_xlabel(plot_data['x_label'], fontsize = style_plot['plot_template']['label_font_size'], color = style_plot['plot_template']['main_text_color'], fontweight='bold')
    #plt.xticks(rotation=45)
    legend_list = []
    if style_plot['data_colors']['use_colormap']:       
        cm = plt.get_cmap(style_plot['data_colors']['colormap'])(np.linspace(0, 1, len(plot_data['y_data_column_name'])))
        ax.set_prop_cycle('color', list(cm))
        for index, y_data in enumerate(plot_data['y_data_column_name']):  
            ax.scatter(    
                    plot_data['x_data_column_name'], 
                    y_data, data=plot_data['data'], 
                    #linestyle='-', marker='o',
                    #linewidth=style_plot['plot_template']['plot_line_width'], 
                    s = style_plot['plot_template']['plot_marker_size']
                    )
            legend_list.append(plt.Rectangle((0,0),1,1,fc=tuple(list(cm)[index]),  edgecolor = 'none'))       
    else:
        for index, y_data in enumerate(plot_data['y_data_column_name']):
            ax.scatter( 
                    plot_data['x_data_column_name'], 
                    y_data, data=plot_data['data'], 
                    #linestyle='-', 
                    #marker='o',
                    #linewidth=style_plot['plot_template']['plot_line_width'], 
                    s = style_plot['plot_template']['plot_marker_size'], 
                    color = style_plot['data_colors']['specific_colors'][index]
                    )
            legend_list.append(plt.Rectangle((0,0),1,1,fc=style_plot['data_colors']['specific_colors'][index],  edgecolor = 'none'))

    l = plt.legend(legend_list, plot_data['y_data_column_name'], loc='best', prop={'size':16})
    #l.draw_frame(False)

    plt.show()
    #plt.savefig(plot_data['filename'] + ".png", bbox_inches='tight')
    plt.clf()




def line_plot(plot_data, style_plot:dict):

    plt.figure(figsize = style_plot['plot_template']['plot_size'])
    plt.rcParams['lines.markersize'] = 6
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14
    plt.rcParams['xtick.major.size'] = 6
    plt.rcParams['xtick.major.width'] = 4
    plt.rcParams['ytick.major.size'] = 6
    plt.rcParams['ytick.major.width'] = 4
    plt.rcParams['xtick.bottom'] = True
    plt.rcParams['ytick.left'] = True
    ax = plt.gca()
    #plt.xlim(2000, 2025)
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(style_plot['plot_template']['plot_line_width'])
        ax.spines[axis].set_color(style_plot['plot_template']['main_text_color'])
    ax.tick_params(axis='x', colors = style_plot['plot_template']['main_text_color'], labelsize=18)
    ax.tick_params(axis='y', colors = style_plot['plot_template']['main_text_color'], labelsize=18)
    ax.grid(color = style_plot['plot_template']['grid_color'], linestyle='-', linewidth=1.5)
    ax.set_ylabel(plot_data['y_label'], fontsize = style_plot['plot_template']['label_font_size'], color = style_plot['plot_template']['main_text_color'], fontweight='bold')
    ax.set_xlabel(plot_data['x_label'], fontsize = style_plot['plot_template']['label_font_size'], color = style_plot['plot_template']['main_text_color'], fontweight='bold')
    plt.xticks(rotation=45)
    legend_list = []
    if style_plot['data_colors']['use_colormap']:       
        cm = plt.get_cmap(style_plot['data_colors']['colormap'])(np.linspace(0, 1, len(plot_data['y_data_column_name'])))
        ax.set_prop_cycle('color', list(cm))
        for index, y_data in enumerate(plot_data['y_data_column_name']):  
            ax.plot(    
                    plot_data['x_data_column_name'], 
                    y_data, data=plot_data['data'], 
                    linestyle='-', marker='o',
                    linewidth=style_plot['plot_template']['plot_line_width'], 
                    markersize = style_plot['plot_template']['plot_marker_size'])
            legend_list.append(plt.Rectangle((0,0),1,1,fc=tuple(list(cm)[index]),  edgecolor = 'none'))       
    else:
        for index, y_data in enumerate(plot_data['y_data_column_name']):
            ax.plot( 
                    plot_data['x_data_column_name'], 
                    y_data, data=plot_data['data'], 
                    linestyle='-', 
                    marker='o',
                    linewidth=style_plot['plot_template']['plot_line_width'], 
                    markersize = style_plot['plot_template']['plot_marker_size'], 
                    color = style_plot['data_colors']['specific_colors'][index]
                    )
            legend_list.append(plt.Rectangle((0,0),1,1,fc=style_plot['data_colors']['specific_colors'][index],  edgecolor = 'none'))

    #l = plt.legend(legend_list, plot_data['elements'], ncol = 2, bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':16})
    #l.draw_frame(False)

    plt.show()
    #plt.savefig(plot_data['filename'] + ".png", bbox_inches='tight')
    plt.clf()



# %%
