from plotting_program.plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt
import numpy as np

from plotting_program.plots.plots_settings import plots_version_folder, graphs_path


def subfigure_plt(outflow_props_table, labels, legend_title, indication, real_data, color_len, outf_colors, display_lum,
                         labels_flag=False):

    fig = plt.figure(figsize=(8, 6.85))
    ax = fig.add_subplot(111)
    ax1 = fig.add_subplot(221)
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.3, hspace= 0.3)
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

    colors = plt.cm.tab20(np.linspace(0, 1, color_len))
    if display_lum:
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
            # ax1.set_ylabel('Masės pernašos sparta [$M_{\odot}yr^{-1}$]', fontsize=14)
            ax1.set_xlabel('Šviesis [$erg~s^{-1}$]', fontsize=14)
            ax1.set_yscale('log')
            ax1.set_xscale('log')
            ax1.scatter(outflow_props.luminosity_AGN_arr.values, outflow_props.dot_mass_arr.values, color=colors[i],
                        s=0.1)
        if real_data:
            print(real_data)
            for ind, x in enumerate(real_data):
                ax1.scatter(10 ** x.luminosity_AGN_log.values, x.derived_dot_mass.values, marker='*',
                            color=colors[len(outflow_props_table) + ind], s=95)
                labels.append(str(x.name.values[0]))

        a = np.linspace(1e40, 1e48, 1000)
        fior = (-29.8) + (0.76) * np.log10(a)
        cic = (-29.8) + (0.72) * np.log10(a)
        f1 = ax1.plot(a, 10 ** cic, '--', color='red', markersize=1, label='Cicone et al. 2013')
        # pplot.append(ax1.plot(a, 10**cic, '--', color='red', markersize=5))
        # f2 = ax1.plot(a, 10 ** fior, '--', color='black', markersize=1, label='Fiore et al. 2017')
    else:

        for i, outflow_props in enumerate(outflow_props_table):

            if isinstance(outf_colors, bool):
                # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
                colors = plt.cm.tab20(np.linspace(0, 1, color_len))
            else:
                # for outf in outflow_props_table:
                colors = outflow_props.color
                print(colors)

            ax1.set_xlim(1e3, 1e8)
            ax1.set_yscale('log')
            ax1.set_xscale('log')
            ax1.set_xlabel('Laikas [$yr$]', fontsize=14)

            ax1.set_ylim(1.e-2, 1.e2)
            ax1.set_ylabel('Spindulys [$kpc$]', fontsize=14)
            ax1.plot(outflow_props.time_arr.values, outflow_props.radius_arr.values, c=colors[i])
        # plt.show()
        # plt.legend(labels, title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))

    ax2 = fig.add_subplot(222)
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
        ax2.set_ylim(3.e0, 1.e4)
        ax2.set_xlim((2.e-2, 2.e1))
        ax2.set_ylabel('Greitis [$km/s$]', fontsize=14)
        ax2.set_xlabel('Spindulys [$kpc$]', fontsize=14)
        ax2.set_yscale('log')
        ax2.set_xscale('log')
        ax2.plot(outflow_props.radius_arr.values, outflow_props.dot_radius_arr.values, c=colors[i])

    if not isinstance(real_data, bool):
        print(real_data)
        for ind, x in enumerate(real_data):
            print(x)
            print(x.radius.values)

            ax2.plot(x.radius.values, x.dot_radius.values, marker='*', c=colors[len(outflow_props_table)+ind], markersize=15)
            labels.append(str(x.name.values[0]))

    ax3 = fig.add_subplot(223)
    for i, outflow_props in enumerate(outflow_props_table):
        if isinstance(outf_colors, bool):
            # colors = plt.cm.tab20(np.linspace(0, 1, len(outflow_props_table)))
            colors = plt.cm.tab20(np.linspace(0, 1, color_len))
        else:
            # for outf in outflow_props_table:
            colors = outflow_props.color
            print(colors)
        ax3.set_ylim(1e0, 4.e4)
        ax3.set_xlim((2.e-2, 2.e1))
        if display_lum:
            ax.set_ylabel('Masės pernašos sparta [$M_{sun}yr^{-1}$]', fontsize=14)
        else:
            ax3.set_ylabel('Masės pernašos sparta [$M_{sun}yr^{-1}$]', fontsize=14)
        ax3.set_xlabel('Spindulys [$kpc$]', fontsize=14)
        ax3.set_yscale('log')
        ax3.set_xscale('log')
        ax3.plot(outflow_props.radius_arr.values, outflow_props.dot_mass_arr.values, c=colors[i])
    if not isinstance(real_data, bool):
        for ind, x in enumerate(real_data):
            ax3.plot(x.radius.values, x.derived_dot_mass.values, marker='*', c=colors[len(outflow_props_table)+ind], markersize=15)
    # plt.show()
    print(labels)
    plt.legend(labels, title=legend_title, bbox_to_anchor=(1.28, 1), loc='upper left', borderaxespad=0.)

    # fig.subplots_adjust(left=0.2, wspace=0.6)

    ax1.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    ax1.tick_params(length=7, width=1.5)
    ax1.tick_params(which='minor', length=4.5, width=1.2)

    ax2.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    ax2.tick_params(length=7, width=1.5)
    ax2.tick_params(which='minor', length=4.5, width=1.2)

    ax3.tick_params(axis='both', which='both', direction='in', top=True, right=True, width=1.2, labelsize='large')
    ax3.tick_params(length=7, width=1.5)
    ax3.tick_params(which='minor', length=4.5, width=1.2)

    fig.align_ylabels([ax1, ax2, ax3])
    fig.align_xlabels([ax1, ax2, ax3])

    fig.savefig(graphs_path + plots_version_folder + 'test-' + str(indication) + '.png', bbox_inches='tight')

    plt.close(fig)
    # plt.show()