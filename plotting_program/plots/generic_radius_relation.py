from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_radius_relation_plot(outflow_props_table, labels, legend_title, indication, real_data,color_len, outf_colors, labels_flag=False):
    Plot = PlotSetup()
    #
    fig1, ax1 = Plot.setup_common_properties()
    colors = plt.cm.tab20(np.linspace(0, 1, color_len))

    # if not isinstance(real_data, bool):
    #     colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)+len(real_data)))
    # elif isinstance(outf_colors, bool):
    #     colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    # else:
    #     # for outf in outflow_props_table:
    #     colors = outflow_props_table[0].colors

    for i, outflow_props in enumerate(outflow_props_table):

        # if not isinstance(real_data, bool):
        #     colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table) + len(real_data)))
        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))

            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        ax1.set_ylim(3.e0, 1.e4)
        ax1.set_xlim((2.e-2, 2.e1))
        ax1.set_ylabel('Greitis [$km/s$]', fontsize=14)
        ax1.set_xlabel('Spindulys [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.plot(outflow_props.radius_arr.values, outflow_props.dot_radius_arr.values, c=colors[i])

    if not isinstance(real_data, bool):
        print(real_data)
        for ind, x in enumerate(real_data):
            print(x)
            print(x.radius.values)

            ax1.plot(x.radius.values, x.dot_radius.values, marker='*', c=colors[len(outflow_props_table)+ind], markersize=15)
            labels.append(str(x.name.values[0]))
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'vel-radius-' + str(indication) + '.png', bbox_inches='tight')

    plt.close(fig1)

    fig1, ax1 = Plot.setup_common_properties()
    # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
    for i, outflow_props in enumerate(outflow_props_table):
        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        ax1.set_ylim(1e0, 4.e4)
        ax1.set_xlim((2.e-2, 2.e1))
        ax1.set_ylabel('Masės pernašos sparta [$M_{sun}yr^{-1}$]', fontsize=14)
        ax1.set_xlabel('Spindulys [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax1.plot(outflow_props.radius_arr.values, outflow_props.dot_mass_arr.values, c=colors[i])
    if not isinstance(real_data, bool):
        for ind, x in enumerate(real_data):
            ax1.plot(x.radius.values, x.derived_dot_mass.values, marker='*', c=colors[len(outflow_props_table)+ind], markersize=15)
    # plt.show()
    print(labels)
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'dot_mass-radius-' + str(indication) + '.png', bbox_inches='tight')
    plt.close(fig1)