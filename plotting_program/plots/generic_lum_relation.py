from data_generator.configurations.units import unit_sunmass
from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_lum_relation(outflow_props_table, labels, legend_title, indication, real_data, color_len, outf_colors, labels_flag=False):
    Plot = PlotSetup()
    fig1, ax1 = Plot.setup_common_properties()

    colors = plt.cm.tab20(np.linspace(0, 1, color_len))

    pplot = []
    for i, outflow_props in enumerate(outflow_props_table):

        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        ax1.set_ylim(1e0, 2.e4)
        ax1.set_xlim((1.e42, 1.e48))
        ax1.set_ylabel('Masės pernašos sparta [$M_{\odot}yr^{-1}$]', fontsize=14)
        ax1.set_xlabel('Šviesis [$erg~s^{-1}$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        pplot.append(ax1.scatter(outflow_props.luminosity_AGN_arr.values, outflow_props.dot_mass_arr.values, color=colors[i], s=0.1))
    if real_data:
        print(real_data)
        for ind, x in enumerate(real_data):
            ax1.scatter(10 ** x.luminosity_AGN_log.values, x.derived_dot_mass.values, marker='*', color=colors[len(outflow_props_table)+ind], s=95)
            labels.append(str(x.name.values[0]))
    # plt.show()
    print(labels)
    # lgnd = plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5), scatterpoints=1)
    # for handle in lgnd.legendHandles:
    #     handle.set_sizes([18.0])
    a = np.linspace(1e40, 1e48, 1000)
    fior=(-29.8)+(0.76)*np.log10(a)
    cic=(-29.8)+(0.72)*np.log10(a)
    # b = (a**0.76)/(unit_sunmass*1e7*((60*60*24*365)**2))*(1000)
    # arba
    # b = (a**0.76)/(unit_sunmass*1e7*((60*60*24*365)**2))*(1000)/1e6
    f1 = ax1.plot(a, 10**cic, '--', color='red', markersize=1, label='Cicone et al. 2013')
    # pplot.append(ax1.plot(a, 10**cic, '--', color='red', markersize=5))
    # f2 = ax1.plot(a, 10**fior, '--', color='black', markersize=1, label='Fiore et al. 2017')
    # pplot.append(ax1.plot(a, 10**fior, '--', color='black', markersize=5))
    # labels.append('Cicone et al. 2013')
    # labels.append('Fiore et al. 2017')
    # first_legend = plt.legend(handles=[f1, f2])
    # plt.gca().add_artist(first_legend)
    lgnd = plt.legend(pplot, labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5), scatterpoints=1)
    for handle in lgnd.legendHandles:
        try:
            handle.set_sizes([18.0])
        except:
            pass

    fig1.savefig(graphs_path + plots_version_folder + 'dot-mass-luminosity-2' + str(indication) + '.png', bbox_inches='tight')
    #
    plt.close(fig1)
    # plt.show()