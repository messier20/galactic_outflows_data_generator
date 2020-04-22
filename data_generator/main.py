import itertools
import math
import os

import matplotlib.pyplot as plt
import pandas as pd

import data_generator.configurations.initial_galaxy_params as init
import data_generator.configurations.switches as swch
import data_generator.configurations.constants as const
import data_generator.configurations.units as unt
from data_generator.configurations.path_version_settings import params_path, values_version_folder
from data_generator.data_models.initial_masses_calculations import calc_bulge_masses
from data_generator.data_models.arrays_modifier import *

import time

from data_generator.mathematical_calculations.DrivingForceIntegrator import DrivingForceIntegrator
from data_generator.mathematical_calculations.FadeTypeSwitcher import FadeTypeSwitcher
from data_generator.mathematical_calculations.mass_calculation import mass_calculation

# version = 1.0

if __name__ == '__main__':
    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()

    # params_path = "C:/Users/Monika/PycharmProjects/SMBHs/model_program/results/output_values/"
    # params_path = "C:/Users/Monika/PycharmProjects/galactic-outflows-nn/data_generator/results/"
    # values_version_folder = 'v' + str(version) + '/'
    # try:
    #     os.mkdir(params_path + values_version_folder)
    # except:
    #     pass

    # bulge_disc_gas_fraction
    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()
    header = True
    df_index = 0
    virial_mass = []
    smbh_m = []
    alpha_left = 8.18 + 0.13
    alpha_right = 8.18 - 0.13
    # alpha_right = 8.18
    # alpha_left = 8.18
    beta_left = 1.57 + 0.39
    beta_right = 1.57 - 0.39
    # beta_left = 1.57
    # beta_right = 1.57

    alpha_parameters = np.random.uniform(alpha_left, alpha_right, len(init.virial_galaxies_masses))
    # alpha_parameters = np.random.normal(8.18, 0.13, len(init.virial_galaxies_masses))
    beta_parameters = np.random.uniform(beta_left, beta_right, len(init.virial_galaxies_masses))
    # beta_parameters = np.random.normal(1.57, 0.39, len(init.virial_galaxies_masses))
    print(alpha_parameters)
    print(beta_parameters)
    for gal_index, virial_galaxy_mass in enumerate(init.virial_galaxies_masses):

        virial_radius = (626 * (((virial_galaxy_mass / (10 ** 13)) * unt.unit_sunmass) ** (1 / 3))) / unt.unit_kpc

        # alpha_left = 8.18 + 0.13
        # alpha_right = 8.18 - 0.13
        # beta_left = 1.57 + 0.39
        # beta_right = 1.57 - 0.39
        #
        # alpha_parameters = np.random.normal(8.18, 0.13, len(virial_galaxy_mass))
        # beta_parameters = np.random.normal(1.57, 0.39, len(virial_galaxy_mass))
        # print(alpha_parameters)
        # print(beta_parameters)


        # theor_bulge_mass_log_right = (np.log10(smbh_mass) - alpha_right) / beta
        # theor_bulge_mass_log_left = (np.log10(smbh_mass) - alpha_left) / beta
        # theor_bulge_mass_right = (10 ** theor_bulge_mass_log_right) * norm_mass
        # theor_bulge_mass_left = (10 ** theor_bulge_mass_log_left) * norm_mass
        # np.random.seed(int(np.ceil(smbh_mass * 100)))
        # np.random.seed(index)
        # bulge_masses_log = np.random.uniform(theor_bulge_mass_log_left, theor_bulge_mass_log_right, size=2)

        log_smbh_mass = alpha_parameters[gal_index] + (beta_parameters[gal_index] * (np.log10(virial_galaxy_mass) - 13.0))
        # log_smbh_mass = 8.18 + (1.55 * (np.log10(virial_galaxy_mass) - 13.0))
        bh_m = 10**log_smbh_mass
        virial_mass.append(virial_galaxy_mass)
        smbh_m.append(bh_m)

        # for out_indx, (smbh_mass_init, bulge_disc_gas_fraction) in enumerate(itertools.product(init.smbh_masses_initial,
        #                                                                                        init.bulge_disc_gas_fractions)):
        #     bh_mass = calc_smbh_masses(virial_galaxy_mass)
        #
        #     # if
        #     # print(smbh_mass_init, 'smbh')
        #     bulge_masses = calc_bulge_masses(smbh_mass_init, out_indx)
        #     # print(smbh_mass_init)
        #     print(bulge_masses)
        #     # bulge_masses = [9.e10]
        #     # bulge_masses = [2.e10, 3.e10, 4.e10, 5.e10, 6.e10, 7.e10, 8.e10, 9.e10, 1.e11, 2.e11, 3.e11]
        #     # TODO check if this shouldn't be division from virial galaxy mass
        #     bulge_disc_totalmass_fractions = bulge_masses / 1.e13
        #     # bulge_disc_totalmass_fractions = [0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.02, 0.03]
        #     # bulge_disc_totalmass_fractions = [0.009]
        #     bulge_scales = [((bulge_mass / 1.e11) ** 0.88) * 2.4 * 2 / unt.unit_kpc for bulge_mass in bulge_masses]
        #
        #     for bulge_index, bulge_disc_totalmass_fraction in enumerate(bulge_disc_totalmass_fractions):
        #         radius_arr, dot_radius_arr, dotdot_radius_arr, dotdotdot_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, time_arr, \
        #         dot_time_arr, luminosity_AGN_arr, smbh_mass_arr, bulge_mass_arr = init_zero_arrays(arrays_count=12)
        #         radius_arr[0] = init.radius
        #         dot_radius_arr[0] = init.dot_radius
        #         dotdot_radius_arr[0] = init.dotdot_radius
        #         smbh_mass = smbh_mass_init
        #         # print(bulge_index)
        #
        #         is_main_loop = True
        #         index = 0
        #         while is_main_loop:
        #             (mass_potential, dot_mass_potential, mass_gas, dot_mass_gas, dotdot_mass_gas, rho_gas, sigma, phi,
        #              phigrad, rhog_as2, mass_bulge) = mass_calculation(radius_arr[index], dot_radius_arr[index],
        #                                                                dotdot_radius_arr[index], virial_galaxy_mass,
        #                                                                virial_radius, init.halo_concentration_parameter,
        #                                                                bulge_scales[bulge_index],
        #                                                                bulge_disc_totalmass_fraction,
        #                                                                init.halo_gas_fraction, bulge_disc_gas_fraction,
        #                                                                init.bulge_to_total_mass)
        #             mass_out_arr[index] = mass_gas
        #             total_mass_arr[index] = mass_gas + mass_potential
        #             # print(total_mass_arr[index]*unit_sunmass)
        #             dot_mass_arr[index] = dot_mass_gas
        #             bulge_mass_arr[index] = mass_bulge
        #
        #             dot_t1 = (radius_arr[index] + 1.e-8) / (dot_radius_arr[index] + 1.e-8)
        #             dot_t2 = (dot_radius_arr[index] + 1.e-8) / (dotdot_radius_arr[index] + 1.e-8)
        #             dot_t3 = (dotdot_radius_arr[index] + 1.e-8) / (dotdotdot_radius_arr[index] + 1.e-8)
        #
        #             dt = 0.1 * min(abs(dot_t1), abs(dot_t2), abs(dot_t3))
        #             if dt > const.DT_MAX / 100. * (10. * time_arr[index] + 1.):
        #                 dt = const.DT_MAX / 100. * (10. * time_arr[index] + 1.)
        #             if dt < const.DT_MIN:
        #                 dt = const.DT_MIN
        #             dot_time_arr[index + 1] = dt
        #             time_arr[index + 1] = time_arr[index] + dt
        #
        #             if swch.repeating_equation:
        #                 time_eff = time_arr[index] % init.quasar_dt
        #             else:
        #                 time_eff = time_arr[index]
        #
        #             luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(swch.fade, time_eff, init.quasar_duration,
        #                                                                     init.eddingtion_ratio)
        #             luminosity_edd = 1.3e38 * (
        #                     smbh_mass * unt.unit_mass / 1.989e33) * unt.unit_time / unt.unit_energy  # ;eddington luminosity for the current SMBH mass
        #             luminosity = luminosity_coef * luminosity_edd
        #             luminosity_AGN_arr[index + 1] = luminosity  # ;actual luminosity
        #
        #             if swch.smbh_grows:
        #                 smbh_mass = smbh_mass * math.exp(luminosity_coef * dt / init.salpeter_timescale)
        #
        #             (radius_arr, dot_radius_arr, dotdot_radius, dotdotdot_radius_arr) = \
        #                 Integrator.driving_force_calc(swch.driving_force, mass_gas, radius_arr[index], const.ETA_DRIVE,
        #                                               swch.integration_method, luminosity, dot_mass_gas,
        #                                               dot_radius_arr[index], dotdot_radius_arr[index], mass_potential,
        #                                               dot_mass_potential,
        #                                               dotdot_mass_gas,
        #                                               dotdotdot_radius_arr, radius_arr,
        #                                               dot_radius_arr, dotdot_radius_arr, index, dt)
        #
        #             index += 1
        #
        #             if index >= len(radius_arr) - 1:
        #                 print(' timesteps')
        #                 is_main_loop = False
        #                 print('Iteration number ', bulge_index, ' finished')
        #             # print(time_arr[index])
        #             # print(const.TIME_MAX)
        #             if time_arr[index] >= const.TIME_MAX:
        #                 print('time')
        #                 is_main_loop = False
        #                 print('Iteration number ', bulge_index, ' finished')
        #
        #             if radius_arr[index] >= const.RADIUS_MAX:
        #                 print('radiusmax')
        #                 # print(time_arr[index])
        #                 is_main_loop = False
        #                 print('Iteration number ', bulge_index, ' finished')
        #
        #
        #
        #         radius_arr = radius_arr * unt.unit_kpc
        #         dot_radius_arr = dot_radius_arr * unt.unit_velocity / 1.e5
        #         time_arr = time_arr * unt.unit_year
        #         # pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
        #         # pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
        #         dot_mass_arr = dot_mass_arr * unt.unit_sunmass / unt.unit_year
        #         mass_out_arr = mass_out_arr * unt.unit_sunmass
        #         total_mass_arr = total_mass_arr * unt.unit_sunmass
        #
        #         bulge_mass_arr = bulge_mass_arr * unt.unit_sunmass
        #         # observed_time_arr = radius_arr / dot_radius_arr
        #
        #         #
        #
        #         radius_reduced_arr = np.where(radius_arr > 0.02, radius_arr, np.nan)
        #         dot_radius_reduced_arr = np.where(radius_arr > 0.02, dot_radius_arr, np.nan)
        #         dot_radius_reduced_arr.shape = dot_radius_arr.shape
        #         time_reduced_arr = np.where(radius_arr > 0.02, time_arr, np.nan)
        #         dot_mass_reduced_arr = np.where(radius_arr > 0.02, dot_mass_arr, np.nan)
        #         mass_out_reduced_arr = np.where(radius_arr > 0.02, mass_out_arr, np.nan)
        #         total_mass_reduced_arr = np.where(radius_arr > 0.02, total_mass_arr, np.nan)
        #         luminosity_AGN_reduced_arr = np.where(radius_arr > 0.02, luminosity_AGN_arr, np.nan)
        #         # observed_time_reduced_arr = np.where(radius_arr > 0.02, observed_time_arr, np.nan)
        #
        #         outflow_properties_df = pd.DataFrame(
        #             np.array([radius_reduced_arr, dot_radius_reduced_arr, time_reduced_arr,
        #                       dot_mass_reduced_arr, mass_out_reduced_arr,
        #                       total_mass_reduced_arr, luminosity_AGN_reduced_arr]).transpose())
        #         columns = 'radius_arr', 'dot_radius_arr', 'time_arr', 'dot_mass_arr', 'mass_out_arr', 'total_mass_arr', 'luminosity_AGN_arr'
        #         outflow_properties_df.columns = columns
        #
        #         outflow_properties_df.to_csv(
        #             (str(params_path) + values_version_folder + '_' + str(bulge_index) + '_' + str(
        #                 out_indx) + '_' + str(gal_index) + '.csv'),
        #             header=True, index=False)
        #
        #         galaxy_properties_df = pd.DataFrame({'smbh_mass': smbh_mass_init, 'bulge_mass': bulge_masses[bulge_index],
        #                                              'bulge_gas_frac': bulge_disc_gas_fraction,
        #                                              'bulge_index': bulge_index, 'params_index': out_indx, 'galaxy_index':
        #                                                  gal_index}, index=[df_index])
        #         # print(galaxy_properties_df)
        #         # galaxy_df_columns = 'smbh_mass', 'bulge_mass', 'bulge_gas_frac', 'bulge_index', 'params_index', 'galaxy_index'
        #         # galaxy_properties_df.columns = galaxy_df_columns
        #         mode = 'w' if header else 'a'
        #         galaxy_properties_df.to_csv((str(params_path) + values_version_folder + 'properties_map.csv'), mode=mode, header=header, index=False)
        #         header = False
        #         df_index +=1

    print('passed time', time.time() - start_time)
    plt.xlabel('mtot')
    plt.ylabel('smbh_m')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(3e10, 1e15)
    plt.ylim(5e4, 1e11)
    plt.scatter(virial_mass, smbh_m)
    plt.show()



# TODO write in one file like in this example and probably use extended pandas frame as for plotting

# header = True
# for dataset in datasets:
#     df = pd.DataFrame(dataset)
#     df = df[columns]
#     mode = 'w' if header else 'a'
#     df.to_csv('./new.csv', encoding='utf-8', mode=mode, header=header, index=False)
#     header = False
# TODO choose between csv and npy
# category = ['none' for i in range(len(luminosity_AGN_reduced_arr[0]))]
                #
                # np.savez(str(params_path) + params_output_name + model_type[out_index] + 'lum_none',
                #          radius=radius_more_than_20_arr, velocity=dot_radius_reduced_arr, time=time_reduced_arr,
                #          dot_mass=dot_mass_reduced_arr, luminosity=luminosity_AGN_reduced_arr, category=category)