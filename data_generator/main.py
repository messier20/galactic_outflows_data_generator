import itertools
import decimal
import matplotlib.pyplot as plt

from data_generator.configurations.initial_galaxy_params import smbh_masses_initial, bulge_disc_gas_fractions
from data_generator.data_models.arrays_modifier import *

if __name__ == '__main__':
    bulge_masses = np.zeros((len(smbh_masses_initial), 1))
    theoretical_bulge_mass = np.zeros((len(smbh_masses_initial), 1))

    for index, bh_mass in enumerate(smbh_masses_initial):


        alpha = 8.46
        theoretical_bulge_mass_log = (np.log10(bh_mass) - alpha) / 1.05
        alpha = 7.86 #8.06
        theoretical_bulge_mass_log_less = (np.log10(bh_mass) - alpha) / 1.05
        alpha = 9.06
        # alpha = 9.12
        theoretical_bulge_mass_log_more = (np.log10(bh_mass) - alpha) / 1.05
        theoretical_bulge_mass[index] = (10 ** theoretical_bulge_mass_log) * 1e11
        theoretical_bulge_mass_less = (10 ** theoretical_bulge_mass_log_less) * 1e11
        theoretical_bulge_mass_more = (10 ** theoretical_bulge_mass_log_more) * 1e11
        print(format(theoretical_bulge_mass_less, '.2e'), ' less')
        print(format(theoretical_bulge_mass_more, '.2e'), 'more')
        # bulge_masses[index] = np.logspace(theoretical_bulge_mass_log_more, theoretical_bulge_mass_log_less, 10, dtype='int64')*1e11
        # bulge_masses[index] = np.random.RandomState(0).uniform(theoretical_bulge_mass_more, theoretical_bulge_mass_less, size=10)
        np.random.seed(index+3)
        bulge_masses_log = np.random.uniform(theoretical_bulge_mass_log_more, theoretical_bulge_mass_log_less, size=1)
        bulge_masses[index] = (10**bulge_masses_log)*1e11
        # print(bulge_masses)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e8, 1e13)
    plt.ylim(1e6, 4e10)
    plt.xlabel('$M_{bulge}$')
    plt.ylabel('$M_{BH}$')
    all_bhm = [[j for i in range(len(bulge_masses[0]))] for j in smbh_masses_initial]



    # plt.scatter(bulge_masses[0,], [smbh_masses_initial[0], smbh_masses_initial[0], smbh_masses_initial[0], smbh_masses_initial[0], smbh_masses_initial[0]] )
    # print(np.array(all_bhm))
    print(bulge_masses.shape)
    print(np.array(all_bhm).shape)
    plt.scatter(bulge_masses, all_bhm)
    plt.plot(theoretical_bulge_mass, smbh_masses_initial, 'r')
    # plt.show()
    plt.savefig('seed+3_seedn7_nonlog_alpha9-06_280_1full_wide.png')

    # for smbh_mass_init, bulge_disc_gas_fraction in itertools.product(smbh_masses_initial, bulge_disc_gas_fractions):
    #
    #     is_main_loop = True
    #     radius_arr, dot_radius_arr, dotdot_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, time_arr, \
    #         dot_time_arr, luminosity_AGN_arr, smbh_mass_arr = init_zero_arrays(arrays_count=10)
    #
    #     # alpha = 8.46
    #     # theoretical_bulge_mass_log = (np.log10(1e8) - alpha)/ 1.05
    #     # alpha = 7.46
    #     # theoretical_bulge_mass_log_less = (np.log10(1e8) - alpha)/ 1.05
    #     # alpha = 9.46
    #     # theoretical_bulge_mass_log_more = (np.log10(1e8) - alpha)/ 1.05
    #     # theoretical_bulge_mass = (10**theoretical_bulge_mass_log)*1e11
    #     # bulge_masses = np.logspace((10**theoretical_bulge_mass_log_less)*1e11, (10**theoretical_bulge_mass_log_more)*1e11, 5)
    #
    #     index = 0
    #     while is_main_loop:
    #         index = + 1
    #         print(index)
    #         is_main_loop = False
