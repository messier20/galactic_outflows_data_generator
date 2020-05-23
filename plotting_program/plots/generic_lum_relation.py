from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_lum_relation(outflow_props_table, labels, legend_title, indication):
    Plot = PlotSetup()
    #
    fig1, ax1 = Plot.setup_common_properties()
    colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        ax1.set_ylim(1e0, 1.e3)
        ax1.set_xlim((1.e32, 1.e47))
        ax1.set_ylabel('Mass outflow rate [$M_{\odot}yr^{-1}$]', fontsize=14)
        ax1.set_xlabel('luminosity [$erg s^{-1}$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.scatter(outflow_props.luminosity_AGN_arr.values, outflow_props.dot_mass_arr.values, color=colors[i])
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'dot-mass-luminosity-' + str(indication) + '.png', bbox_inches='tight')

    plt.close(fig1)