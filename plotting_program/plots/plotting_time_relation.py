import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# from model_program.input_parameters.galaxy_parameters import bulge_scales, bulge_masses
from plotting_program.plots.PlotSetup import PlotSetup
from plotting_program.plots.plots_settings import *
from plotting_program.turning_plots_on_off import mass_out_t_on, r_t_on, dm_t_on, obs_time_on


def plotting_time_relation(outflow_props):
    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'orange']

    time_arr = time_arr.values
    radius = radius.values
    # arr = np.zeros(100000000)
    # print(arr)
    # bulge_line = np.array([bulge_scales[index] for i in range(len(arr))])

    Plot = PlotSetup()

    if r_t_on:
        fig1, ax1 = Plot.setup_time_rel()
        ax1.set_ylim(1.e-2, 1.e2)
        ax1.set_ylabel('radius [$kpc$]', fontsize=14)
        Plot.plotting(ax1, time_arr, radius, colors, labels)
        ax1.plot([100, 1e8], [bulge_scales[index], bulge_scales[index]], '--', color='purple', label="$R_{bulge}=$"+ str(format(bulge_scales[index], '.2')) + " kpc")
        ax1.legend(title="$M_{bulge} = $ "+ str(format(bulge_masses[index],'.1e')) +"$M_\odot$")

        # for tick in ax1.xaxis.get_major_ticks():
        #     tick.label.set_fontsize('large')
            # tick.set_fontsize('large')
            # ax1.set_title(str(model_index) + '$x10^{9}$')
        fig1.savefig(graphs_path +plots_version_folder  + 'radius-time-' +str(model_index)+'-fix.png', bbox_inches='tight')
        plt.close(fig1)

    # if mass_out_t_on:
    #     mass_out = mass_out.values
    #     mass_out = np.where(mass_out > 0.1, mass_out, np.nan)
    #
    #     fig2, ax2 = Plot.setup_time_rel()
    #     ax2.set_ylim(8.e2, 1.e12)
    #     ax2.set_ylabel('Total mass in outflow [$M_{sun}$]')
    #     # shape example
    #     # p6 = ax2.scatter(time_arr[0, ], mass_out[0, ], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    #     Plot.plotting(ax2, time_arr, mass_out, colors, labels)
    #
    #     # ax2.legend((p6, p7, p8, p9, p10), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
    #     #            markerscale=10)
    #     ax2.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.1e')) + "$M_\odot$")
    #     fig2.savefig(graphs_path +plots_version_folder  + 'out-mass-' + str(model_index)+'.png', bbox_inches='tight')
    #     plt.close(fig2)
    #
    # if dm_t_on:
    #     dot_mass = dot_mass.values
    #     dot_mass = np.where(dot_mass > 0.1, dot_mass, np.nan)
    #     fig3, ax3 = Plot.setup_time_rel()
    #     ax3.set_ylim(0.1, 2.e4)
    #     ax3.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    #     Plot.plotting(ax3, time_arr, dot_mass, colors, labels)
    #     ax3.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.1e')) + "$M_\odot$")
    #     fig3.savefig(graphs_path +plots_version_folder  + 'threepart3' + str(model_index)+'.png', bbox_inches='tight')
    #     plt.close(fig3)

    # if obs_time_on:
    #     dot_radius = dot_radius.values
    #     # dot_radius = np.where(dot_radius > 0.1, dot_radius, np.nan)
    #     dot_radius = dot_radius * 1.02269032e-9
    #     obs_time = np.divide(radius, dot_radius)
    #
    #     fig4, ax4 = Plot.setup_common_properties()
    #     # ax3.set_ylim(1.e-2, 1.e8)
    #     ax4.set_xlim(0, 7000)
    #     ax4.set_xlim(5e1, 1e8)
    #     ax4.set_xscale('log')
    #     ax4.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    #     ax4.set_xlabel('observed time [yr]')
    #     Plot.plotting(ax4, np.array(obs_time), np.array(dot_mass), colors, labels)
    #
    #     # ax3.legend((p16, p17, p18, p19, p20), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
    #     #            markerscale=10)
    #     ax4.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.1e')) + "$M_\odot$")
    #     fig4.savefig(graphs_path +plots_version_folder  + 'obstime' + str(model_index)+'.png', bbox_inches='tight')
    #     plt.close(fig4)