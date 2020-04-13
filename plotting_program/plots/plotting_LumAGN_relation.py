from plotting_program.plots import PlotSetup
import matplotlib.pyplot as plt
from plotting_program.plots.plots_settings import *

def plotting_LumAGN_relation(luminosity_AGN_arr, dot_radius_arr, dot_mass_arr, index, type_name):
    # graphs_path = '/home/monika/Documents/SMBHs/plots/'
    name = plots_version_folder +'nongrow_quasar_alltime_fbtVar_'  + type_name
    Plot = PlotSetup()
    fig1, ax1 = Plot.setup_LAGN_rel()
    ax1.set_ylim(0.e0, 3.e3)
    ax1.set_xlim(3840, 4560)
    ax1.set_ylabel('velocity [$km/s$]')
    ax1.set_xlabel('$Luminosity_{AGN}$ ')
    p1 = ax1.scatter(luminosity_AGN_arr[0,], dot_radius_arr[0,], color='black', marker='.', linewidth=0.7, s=0.3)
    p2 = ax1.scatter(luminosity_AGN_arr[1,], dot_radius_arr[1,], color='b', marker='.', linewidth=0.7, s=0.3)
    p3 = ax1.scatter(luminosity_AGN_arr[2,], dot_radius_arr[2,], color='g', marker='.', linewidth=0.7, s=0.3)
    p4 = ax1.scatter(luminosity_AGN_arr[3,], dot_radius_arr[3,], color='r', marker='.', linewidth=0.7, s=0.3)
    p5 = ax1.scatter(luminosity_AGN_arr[4,], dot_radius_arr[4,], color='yellow', marker='.', linewidth=0.7, s=0.3)

    Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
    fig1.savefig(graphs_path + name + 'lumANG_vel_v2'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig1)

    # Test if luminosity grows
    # fig2, ax2 = Plot.setup_LAGN_rel()
    # ax2.set_xlim(3540, 3900)
    # ax2.set_ylabel('velocity [$kpc/yr$]')
    # ax2.set_xlabel('$Luminosity_{AGN}$ ')
    # p1 = ax2.scatter(luminosity_AGN_arr[0,], dot_mass_arr[0, ], color='black', marker='.', linewidth=0.7, s=0.3)
    # p2 = ax2.scatter(luminosity_AGN_arr[1,], dot_mass_arr[1,], color='b', marker='.', linewidth=0.7, s=0.3)
    # p3 = ax2.scatter(luminosity_AGN_arr[2,], dot_mass_arr[2,], color='g', marker='.', linewidth=0.7, s=0.3)
    # p4 = ax2.scatter(luminosity_AGN_arr[3,], dot_mass_arr[3,], color='r', marker='.', linewidth=0.7, s=0.3)
    # p5 = ax2.scatter(luminosity_AGN_arr[4,], dot_mass_arr[4,], color='yellow', marker='.', linewidth=0.7, s=0.3)
    #
    # Plot.add_legend_gas_fractions(ax2, p1, p2, p3, p4, p5)
    #
    # plt.show()


