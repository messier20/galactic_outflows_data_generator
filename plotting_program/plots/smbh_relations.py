import numpy as np
import matplotlib.pyplot as plt

from data_generator.configurations.path_version_settings import version
from data_generator.configurations.physical_values import intercept_alpha, slope_beta, bulge_normalization_mass
from plotting_program.plots.PlotSetup import PlotSetup


def plot_smbh_relations(props_map):
    smbh_mass = []
    bulge_mass = []
    mtot_mass = []
    plot = PlotSetup()

    fig1, ax1 = plot.setup_common_properties()
    # for par_index in range(props_map.params_index.max() + 1):
    #     for gal_ind in range(props_map.galaxy_index.max() + 1):
    #         file_name = params_output_name + '_' + str(props_map.params_index.values[par_index - 1]) + '_' + str(
    #             props_map.galaxy_index.values[gal_ind - 1]) + '.csv'
    #         outflow = pd.read_csv(file_name)
    #         smbh_mass.append(outflow.smbh_mass)
    #         bulge_mass.append(outflow.bulge_mass)
    #         mtot_mass.append(outflow.galaxy_mass)
    bul = np.logspace(8, 15, 1000)
    mtot = np.logspace(11, 15, 1000)
    smbh = np.logspace(5, 12, 1000)
    # intercept_alpha, slope_beta, bulge_normalization_mass
    theor_bulge_mass_log = (np.log10(smbh) - intercept_alpha) / slope_beta
    theor_bulge_mass = (10 ** theor_bulge_mass_log) * bulge_normalization_mass

    theor_smbh_mass_log = 8.18 + (1.57 * (np.log10(mtot) - 13.0))
    theor_smbh_mass = 10 ** theor_smbh_mass_log

    ax1.set_xlabel('Baldžo masė [$M_{\odot}$]', fontsize=14)
    ax1.set_ylabel('SMBH masė [$M_{\odot}$]', fontsize=14)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim(1e8, 1e14)
    ax1.set_ylim(3e6, 3e10)
    ax1.plot(theor_bulge_mass, smbh, '--', color='black')
    ax1.scatter(props_map.bulge_mass.values, props_map.smbh_mass.values, s=20)
    fig1.savefig('bulge-smbh2' + str(version) + '.png')
    plt.legend()
    # plt.show()
    plt.close(fig1)

    fig1, ax1 = plot.setup_common_properties()

    ax1.set_xlabel('Virialinė galaktikos masė [$M_{\odot}$]', fontsize=14)
    ax1.set_ylabel('SMBH masė [$M_{\odot}$]', fontsize=14)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim(3e11, 4e14)
    ax1.set_ylim(3e6, 3e10)
    ax1.plot(mtot, theor_smbh_mass, '--', color='black')
    ax1.scatter(props_map.galaxy_mass.values, props_map.smbh_mass.values, s=20)
    # plt.show()
    fig1.savefig('smbh-mtot2' + str(version) + '.png')
    plt.close()
