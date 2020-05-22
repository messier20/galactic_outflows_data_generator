from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_radius_relation_plot(outflow_props_table, labels, legend_title, indication):
    Plot = PlotSetup()
    #
    fig1, ax1 = Plot.setup_common_properties()
    colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        ax1.set_ylim(3.e0, 1.e4)
        ax1.set_xlim((2.e-2, 2.e1))
        ax1.set_ylabel('velocity [$km/s$]', fontsize=14)
        ax1.set_xlabel('radius [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.plot(outflow_props.radius_arr.values, outflow_props.dot_radius_arr.values, c=colors[i])
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'vel-radius-' + str(indication) + '.png', bbox_inches='tight')

    plt.close(fig1)

    fig1, ax1 = Plot.setup_common_properties()
    colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        ax1.set_ylim(1e0, 1.e4)
        ax1.set_xlim((2.e-2, 2.e1))
        ax1.set_ylabel('Mass outflow rate [$M_{\odot}yr^{-1}$]', fontsize=14)
        ax1.set_xlabel('radius [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.plot(outflow_props.radius_arr.values, outflow_props.dot_mass_arr.values, c=colors[i])
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'dot_mass-radius-' + str(indication) + '.png', bbox_inches='tight')
    plt.close(fig1)