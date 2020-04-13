from plotting_program.plots import PlotSetup
import matplotlib.pyplot as plt
from plotting_program.plots.plots_settings import *


def plotting_histogram(dot_radius, dot_mass, time_arr, model_name, type_name):
    bins = [i + 10 for i in range(270, 1390)]
    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'yellow']

    Plot = PlotSetup()

    # a = np.where(np.array(dot_radius_arr)>0, dot_radius_arr, np.nan)
    a = dot_radius

    # dot_mass_nozero = np.where(np.array(dot_mass) > 6, dot_mass, np.nan)
    # dot_mass_nozero = np.where(np.array(dot_mass_nozero) < 3500, dot_mass_nozero, np.nan)

    fig1, ax1 = Plot.setup_histogram(model_name)
    # ax1.set_xlim(100, 1400)
    ax1.set_xlabel('velocity [$km/s$]')
    ax1.hist([a[0,], a[1,], a[2,], a[3,], a[4,]], bins=bins, histtype='stepfilled', color=colors, alpha=0.5, label=labels)
    ax1.legend(prop={'size': 10})

    fig1.savefig(graphs_path + plots_version_folder + 'vel_hist_' + type_name  + str(model_name) + '.png', bbox_inches='tight')
    plt.close(fig1)

    # b = np.where(np.array(a) < 360, a,  np.nan)
    # b = a
    # fig2, ax2 = Plot.setup_common_properties()
    # # ax2.set_xlim(0, 360)
    # ax2.set_ylabel('count')
    # ax2.set_xlabel('velocity [$km/s$]')
    # ax2.hist([b[0,], b[1,], b[2,], b[3,], b[4,]], bins=bins, histtype='stepfilled', color=colors, alpha=0.5,
    #          label=labels)
    # ax2.legend(prop={'size': 10})
    # fig2.savefig(graphs_path + name + 'hist_zoomed_v1' + str(model_name) + '.png', bbox_inches='tight')
    # plt.close(fig2)


    i = 0;
    for vel in dot_radius:
        fig, ax = Plot.setup_histogram(model_name)
        ax.set_xlabel('velocity [$km/s$]')
        ax.hist(vel, bins=bins, histtype='stepfilled', color=colors[i], alpha=0.5, label=labels[i])
        ax.legend(prop={'size': 10})
        fig.savefig(graphs_path + plots_version_folder + 'vel_hist' + str(i) + '_' + type_name  + str(model_name) + '.png', bbox_inches='tight')
        i = i + 1
        plt.close(fig)


    fig1, ax1 = Plot.setup_histogram(model_name)
    # ax1.set_xlim(1, 20)
    # ax1.set_ylabel('count')
    ax1.set_xlabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    # labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    # colors = ['black', 'b', 'g', 'r', 'yellow']
    ax1.hist([dot_mass[0,], dot_mass[1,], dot_mass[2,], dot_mass[3,], dot_mass[4,]], bins=800, histtype='stepfilled', color=colors, alpha=0.5,
             label=labels)

    ax1.legend(prop={'size': 10})

    fig1.savefig(graphs_path + plots_version_folder + 'mass_out_hist' + str(i) + '_' + type_name  + str(model_name) + '.png', bbox_inches='tight')
    plt.close(fig1)
