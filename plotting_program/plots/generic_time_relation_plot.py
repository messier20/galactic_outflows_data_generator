from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def generic_time_relation_plot(outflow_props_table, labels, legend_title, indication, real_data, color_len, outf_colors, labels_flag=False):
    Plot = PlotSetup()
    #
    colors = plt.cm.tab20(np.linspace(0, 1, color_len))

    fig1, ax1 = Plot.setup_time_rel()
    for i, outflow_props in enumerate(outflow_props_table):

        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        ax1.set_ylim(1.e-2, 1.e2)
        ax1.set_ylabel('Spindulys [$kpc$]', fontsize=14)
        ax1.plot(outflow_props.time_arr.values, outflow_props.radius_arr.values, c=colors[i])
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'time-radius-' + str(indication) + '.png', bbox_inches='tight')
    plt.close(fig1)

    fig1, ax1 = Plot.setup_time_rel()


    # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))

    for i, outflow_props in enumerate(outflow_props_table):

        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        dot_radius_in_scale = outflow_props.dot_radius_arr.values * 1.02269032e-9
        obs_time = np.divide(outflow_props.radius_arr.values, dot_radius_in_scale)
        time_arr = outflow_props.time_arr.values
        ax1.set_ylim(1e4, 1.e8)
        ax1.set_xlim(1e4, 1.e8)
        ax1.set_ylabel('Stebimas laikas [$yr$]', fontsize=14)
        # a =np.logspace(1, 8.1, 1000)
        ax1.plot(time_arr, obs_time, c=colors[i])
    a = np.logspace(1, 8.1, 1000)
    ax1.plot(a, a, '--', color='grey', markersize=5)
    # plt.show()
    plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    fig1.savefig(graphs_path + plots_version_folder + 'time-obs_time-' + str(indication) + '.png', bbox_inches='tight')
    plt.close(fig1)