import matplotlib.pyplot as plt

# from model_program.input_parameters.galaxy_parameters import bulge_scales, bulge_masses
from plotting_program.plots.PlotSetup import PlotSetup
from plotting_program.plots.plots_settings import *
from plotting_program.turning_plots_on_off import r_r_on, dr_r_on
import numpy as np


def plotting_r_relation(radius, dot_radius, dot_mass, out_mass, model_type, index):
    # graphs_path = '/home/monika/Documents/SMBHs/plots/'
    Plot = PlotSetup()

    radius = radius.values
    dot_radius = dot_radius.values
    dot_mass = dot_mass.values
    out_mass = out_mass.values

    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'orange']

# ?    p1, p2, p3, p4, p5, p6 = np.nan
#
    if r_r_on:
        fig1, ax1 = Plot.setup_common_properties()
        ax1.set_ylim(3.e0, 1.e4)
        ax1.set_xlim((3.e-2, 6.e1))
        ax1.set_ylabel('velocity [$km/s$]', fontsize=14)
        ax1.set_xlabel('radius [$kpc$]', fontsize=14)
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        Plot.plotting(ax1, radius, dot_radius, colors, labels)
        ax1.plot([bulge_scales[index], bulge_scales[index]], [1.e2, 1.e4], '--', color='purple', label="$R_{bulge}=$"+ str(format(bulge_scales[index], '.2')) + " kpc")
        # ax1.plot([100, 1e8], [bulge_scales[index], bulge_scales[index]], '--', color='purple', label="$R_{bulge}=$"+ str(format(bulge_scales[index], '.2')) + " kpc")
        ax1.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.2e')) + "$M_\odot$")

        # ax1.set_title(model_type + '$x10^{9}$')
        # Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
        fig1.savefig(graphs_path + plots_version_folder + 'vel-radius-' + str(model_type) + '.png', bbox_inches='tight')
        plt.close(fig1)

    if dr_r_on:
        fig2, ax2 = Plot.setup_common_properties()
        ax2.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]', fontsize=14)
        ax2.set_xlabel('radius [$kpc$]', fontsize=14)
        ax2.set_yscale('log')
        ax2.set_xscale('log')
        # ax1.set_xlim((1.e-3, 1.e2))
        ax2.set_ylim(5.e-2, 1e4)
        Plot.plotting(ax2, radius, dot_mass, colors, labels)
        ax2.plot([bulge_scales[index], bulge_scales[index]], [1.e-1, 1e4], '--', color='purple',
                 label="$R_{bulge}=$" + str(format(bulge_scales[index], '.2')) + " kpc")
        # ax2.set_title(model_type + '$x10^{9}$')
        ax2.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.2e')) + "$M_\odot$")
        # Plot.add_legend_gas_fractions(ax2, p1, p2, p3, p4, p5)
        fig2.savefig(graphs_path + plots_version_folder + 'dotmass-radius' + str(model_type) + '.png', bbox_inches='tight')
        plt.close(fig2)


    mv = out_mass*dot_radius* 1.02269032e-9
    calculated_dot_mass = np.divide(mv, radius)
    fig4, ax4 = Plot.setup_common_properties()
    ax4.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]', fontsize=14)
    ax4.set_xlabel('radius [$kpc$]', fontsize=14)
    ax4.set_yscale('log')
    ax4.set_xscale('log')
    # ax4.set_xlim(0, 100)
    ax4.set_ylim(5.e1, 1e4)
    Plot.plotting(ax4, radius, np.array(calculated_dot_mass), colors, labels)
    ax4.plot([bulge_scales[index], bulge_scales[index]], [1.e-1, 1e4], '--', color='purple',
             label="$R_{bulge}=$" + str(format(bulge_scales[index], '.2')) + " kpc")
    # ax2.set_title(model_type + '$x10^{9}$')
    ax4.legend(title="$M_{bulge} = $ " + str(format(bulge_masses[index], '.2e')) + "$M_\odot$")
    # Plot.add_legend_gas_fractions(ax2, p1, p2, p3, p4, p5)
    fig4.savefig(graphs_path + plots_version_folder + 'dotmass-calc--radius' + str(model_type) + '.png', bbox_inches='tight')
    plt.close(fig4)


    #
    # fig3, ax3 = Plot.setup_common_properties()
    # ax3.set_ylabel('Mass outflow [$M_{sun}}$]')
    # ax3.set_xlabel('radius [$kpc$]')
    #
    # ax3.set_yscale('log')
    # ax3.set_ylim(1.e8, 1.e13)
    # # ax3.set_xscale('log')
    # # ax1.set_xlim((1.e-3, 1.e2))
    # p1 = ax3.scatter(radius[0,], mass_out[0,], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    # p2 = ax3.scatter(radius[1,], mass_out[1,], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    # p3 = ax3.scatter(radius[2,], mass_out[2,], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    # p4 = ax3.scatter(radius[3,], mass_out[3,], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    # p5 = ax3.scatter(radius[4,], mass_out[4,], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    # ax3.set_title(model_type + '$x10^{9}$')
    #
    # Plot.add_legend_gas_fractions(ax3, p1, p2, p3, p4, p5)
    # fig3.savefig(graphs_path + plots_version_folder + 'massout_radius_' + type_name + str(model_type) + '.png',
    #              bbox_inches='tight')
    # plt.close(fig3)


