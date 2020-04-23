from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_radius_relation_plot(outflow_props_table, indication):
    Plot = PlotSetup()
    #
    fig1, ax1 = Plot.setup_common_properties()
    colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        ax1.set_ylim(3.e0, 1.e4)
        ax1.set_xlim((3.e-2, 6.e1))
        ax1.set_ylabel('velocity [$km/s$]', fontsize=14)
        ax1.set_xlabel('radius [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.plot(outflow_props.radius_arr.values, outflow_props.dot_radius_arr.values, c=colors[i])
    # plt.show()
    fig1.savefig(graphs_path + plots_version_folder + 'vel-radius-' + str(indication) + '.png', bbox_inches='tight')