import itertools
import math
import time

import matplotlib.pyplot as plt
import pandas as pd

import data_generator.configurations.initial_galaxy_params as init
import data_generator.configurations.switches as swch
import data_generator.configurations.units as unt
from data_generator.configurations.path_version_settings import params_path, values_version_folder
from data_generator.data_models.arrays_modifier import *
from data_generator.data_models.initial_masses_calculations import calc_bulge_masses, calc_smbh_masses
from data_generator.mathematical_calculations.DrivingForceIntegrator import DrivingForceIntegrator
from data_generator.mathematical_calculations.FadeTypeSwitcher import FadeTypeSwitcher
from data_generator.mathematical_calculations.mass_calculation import mass_calculation

if __name__ == '__main__':
    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()

    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()
    db_file_header = True
    df_index = 0
    virial_mass = []
    smbh_m = []
    bulge_mas = []
    spc_bm = []
    indices = []

    columns = 'radius_arr', 'dot_radius_arr', 'time_arr', 'dot_mass_arr', 'mass_out_arr', 'total_mass_arr', 'luminosity_AGN_arr'
    # all_params_columns = 'radius', 'dot_radius', 'dot_mass', 'mass_out', 'total_mass', \
    #                      'luminosity_AGN', 'smbh_mass', 'duty_cycle', 't_initial_smbh_mass', 'bulge_mass', 'bulge_gas', \
    #                      'galaxy_mass', 'quasar_duration', 'fade_type'

    for gal_index, virial_galaxy_mass in enumerate(init.virial_galaxies_masses):

        virial_radius = (626 * (((virial_galaxy_mass / (10 ** 13)) * unt.unit_sunmass) ** (1 / 3))) / unt.unit_kpc

        current_smbh_masses = calc_smbh_masses(virial_galaxy_mass) if len(init.smbh_masses_initial) == 0 else init.smbh_masses_initial
        bulge_masses = calc_bulge_masses(current_smbh_masses, gal_index)
        bulge_disc_totalmass_fractions = bulge_masses / (virial_galaxy_mass * unt.unit_sunmass)
        bulge_scales = [((bulge_mass / 1.e11) ** 0.88) * 2.4 * 2 / unt.unit_kpc for bulge_mass in bulge_masses]


        for out_indx, (bulge_disc_gas_fraction, initial_smbh_mass, quasar_duration, fade, duty_cycle) in enumerate(
                itertools.product(init.bulge_disc_gas_fractions, current_smbh_masses, init.quasar_durations, swch.fade_arr.values(), init.duty_cycles)):

            # loop_time = time.time()
            # if fade == const.FADE.KING:
            #     quasar_dt = (48*quasar_duration) / duty_cycle
            quasar_dt = quasar_duration / duty_cycle


            for bulge_index, bulge_disc_totalmass_fraction in enumerate(bulge_disc_totalmass_fractions):

                radius_arr, dot_radius_arr, dotdot_radius_arr, dotdotdot_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, time_arr, \
                dot_time_arr, luminosity_AGN_arr, smbh_mass_arr, bulge_mass_arr = init_zero_arrays(arrays_count=12)
                radius_arr[0] = init.radius
                dot_radius_arr[0] = init.dot_radius
                dotdot_radius_arr[0] = init.dotdot_radius
                smbh_mass_arr[0] = initial_smbh_mass

                is_main_loop = True
                index = 0
                while is_main_loop:
                    (mass_potential, dot_mass_potential, mass_gas, dot_mass_gas, dotdot_mass_gas, rho_gas, sigma, phi,
                     phigrad, rhog_as2, mass_bulge) = mass_calculation(radius_arr[index],
                                                                       dot_radius_arr[index],
                                                                       dotdot_radius_arr[index],
                                                                       virial_galaxy_mass,
                                                                       virial_radius, init.halo_concentration_parameter,
                                                                       bulge_scales[bulge_index],
                                                                       bulge_disc_totalmass_fraction,
                                                                       init.halo_gas_fraction, bulge_disc_gas_fraction,
                                                                       init.bulge_to_total_mass)
                    mass_out_arr[index] = mass_gas
                    total_mass_arr[index] = mass_gas + mass_potential
                    # print(total_mass_arr[index]*unit_sunmass)
                    dot_mass_arr[index] = dot_mass_gas
                    bulge_mass_arr[index] = mass_bulge

                    dot_t1 = (radius_arr[index] + 1.e-8) / (dot_radius_arr[index] + 1.e-8)
                    dot_t2 = (dot_radius_arr[index] + 1.e-8) / (dotdot_radius_arr[index] + 1.e-8)
                    dot_t3 = (dotdot_radius_arr[index] + 1.e-8) / (dotdotdot_radius_arr[index] + 1.e-8)

                    dt = 0.1 * min(abs(dot_t1), abs(dot_t2), abs(dot_t3))
                    if dt > const.DT_MAX / 100. * (10. * time_arr[index] + 1.):
                        dt = const.DT_MAX / 100. * (10. * time_arr[index] + 1.)
                    if dt < const.DT_MIN:
                        dt = const.DT_MIN
                    dot_time_arr[index + 1] = dt
                    time_arr[index + 1] = time_arr[index] + dt

                    if swch.repeating_equation:
                        time_eff = time_arr[index] % quasar_dt
                    else:
                        time_eff = time_arr[index]

                    luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(fade, time_eff, quasar_duration,
                                                                            init.eddingtion_ratio)
                    luminosity_edd = 1.3e38 * (
                            smbh_mass_arr[index] * unt.unit_mass / 1.989e33) * unt.unit_time / unt.unit_energy  # ;eddington luminosity for the current SMBH mass

                    luminosity = luminosity_coef * luminosity_edd
                    luminosity_AGN_arr[index + 1] = luminosity  # ;actual luminosity

                    if swch.smbh_grows:
                        smbh_mass_arr[index+1] = smbh_mass_arr[index] * math.exp(luminosity_coef * dt / init.salpeter_timescale)
                    # TODO change implementation without passing arrays
                    (radius_arr, dot_radius_arr, dotdot_radius_arr, dotdotdot_radius_arr) = \
                        Integrator.driving_force_calc(swch.driving_force, mass_gas, radius_arr[index], const.ETA_DRIVE,
                                                      swch.integration_method, luminosity, dot_mass_gas,
                                                      dot_radius_arr[index], dotdot_radius_arr[index], mass_potential,
                                                      dot_mass_potential,
                                                      dotdot_mass_gas,
                                                      dotdotdot_radius_arr, radius_arr,
                                                      dot_radius_arr, dotdot_radius_arr, index, dt)

                    index += 1

                    if index >= len(radius_arr) - 1:
                        # print(' timesteps')
                        is_main_loop = False

                    if time_arr[index] >= const.TIME_MAX:
                        # print('time')
                        is_main_loop = False

                    if radius_arr[index] >= const.RADIUS_MAX:
                        # print('radiusmax')
                        is_main_loop = False

                radius_arr = radius_arr * unt.unit_kpc
                dot_radius_arr = dot_radius_arr * unt.unit_velocity / 1.e5
                time_arr = time_arr * unt.unit_year
                # pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
                # pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
                dot_mass_arr = dot_mass_arr * unt.unit_sunmass / unt.unit_year
                mass_out_arr = mass_out_arr * unt.unit_sunmass
                total_mass_arr = total_mass_arr * unt.unit_sunmass
                smbh_mass_arr = smbh_mass_arr * unt.unit_sunmass

                # bulge_mass_arr = bulge_mass_arr * unt.unit_sunmass
                w_initial_smbh_mass = initial_smbh_mass * unt.unit_sunmass
                w_virial_galaxy_mass = virial_galaxy_mass * unt.unit_sunmass
                w_quasar_duration = quasar_duration * unt.unit_year
                # observed_time_arr = radius_arr / dot_radius_arr

                reducion_indices = np.where(radius_arr > 0.02)
                # observed_time_reduced_arr = np.where(radius_arr > 0.02, observed_time_arr, np.nan)

                outflow_properties_df = pd.DataFrame(
                    np.array([radius_arr[reducion_indices], dot_radius_arr[reducion_indices], time_arr[reducion_indices],
                              dot_mass_arr[reducion_indices], mass_out_arr[reducion_indices],
                              total_mass_arr[reducion_indices], luminosity_AGN_arr[reducion_indices]]).transpose())
                outflow_properties_df.columns = columns

                outflow_properties_df.to_csv(
                    (str(params_path) + values_version_folder + '_' + str(bulge_index) + '_' + str(
                        out_indx) + '_' + str(gal_index) + '.csv'),
                    header=True, index=False)

                del outflow_properties_df

                galaxy_properties_df = pd.DataFrame({'smbh_mass': w_initial_smbh_mass, 'bulge_mass': bulge_masses[bulge_index],
                                                     'bulge_gas_frac': bulge_disc_gas_fraction, 'galaxy_mass': w_virial_galaxy_mass,
                                                     'quasar_duration': w_quasar_duration, 'fade_type': fade.value,
                                                     'duty_cycle': duty_cycle,
                                                     'bulge_index': bulge_index, 'params_index': out_indx, 'galaxy_index':
                                                         gal_index}, index=[df_index])
                smbh_m.append(w_initial_smbh_mass)
                bulge_mas.append(bulge_masses[bulge_index])
                virial_mass.append((w_virial_galaxy_mass))

                mode = 'w' if db_file_header else 'a'
                galaxy_properties_df.to_csv((str(params_path) + values_version_folder + 'properties_map.csv'), mode=mode, header=db_file_header, index=False)
                # db_file_header = False
                # df_index +=1
                del galaxy_properties_df

                subtracted_indices = reducion_indices[0][::3]

                temp_initial_smbh_mass = [w_initial_smbh_mass for i in range(len(subtracted_indices))]
                temp_bulge_masses = [bulge_masses[bulge_index] for i in range(len(subtracted_indices))]
                temp_bulge_disc_gas_fraction = [bulge_disc_gas_fraction for i in range(len(subtracted_indices))]
                temp_virial_galaxy_mass = [w_virial_galaxy_mass for i in range(len(subtracted_indices))]
                temp_quasar_duration = [w_quasar_duration for i in range(len(subtracted_indices))]
                temp_duty_cycle = [duty_cycle for i in range(len(subtracted_indices))]

                temp_fade = np.array([fade.value for i in range(len(subtracted_indices))], dtype='U25')
                # d = dict([(y, x + 1) for x, y in enumerate(fade_arr)])
                # indices = indices[]

                all_parameters = np.column_stack([radius_arr[subtracted_indices], dot_radius_arr[subtracted_indices],
                                                  dot_mass_arr[subtracted_indices], mass_out_arr[subtracted_indices],
                                                  luminosity_AGN_arr[subtracted_indices],
                                                  smbh_mass_arr[subtracted_indices], temp_duty_cycle,
                                                  temp_initial_smbh_mass, temp_bulge_masses,
                                                  temp_bulge_disc_gas_fraction,
                                                  temp_virial_galaxy_mass, temp_quasar_duration, temp_fade])

                all_params_columns = ['radius', 'dot_radius', 'dot_mass', 'mass_out','luminosity_AGN', 'smbh_mass', \
                                     'duty_cycle', 't_initial_smbh_mass', 'bulge_mass', 'bulge_gas', 'galaxy_mass', \
                                     'quasar_duration', 'fade_type']
                df_all_parameters = pd.DataFrame(all_parameters, columns=all_params_columns)

                mode = 'w' if db_file_header else 'a'
                df_all_parameters.to_csv((str(params_path) + values_version_folder + 'train_data.csv'),
                                            mode=mode, header=db_file_header, index=False, encoding="utf-8")
                db_file_header = False
                df_index += 1

                del temp_initial_smbh_mass
                del temp_bulge_masses
                del temp_bulge_disc_gas_fraction
                del temp_virial_galaxy_mass
                del temp_quasar_duration
                del temp_fade
                del all_parameters

                # print("exec time --- %s seconds ---" % (time.time() - loop_time))
                # print()


    print('passed time', time.time() - start_time)
    # print(bulge_mas)
    # print(smbh_m)

    plt.xlabel('mbulge')
    plt.ylabel('smbh_m')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e8, 1e14)
    plt.ylim(3e5, 5e11)
    plt.scatter(bulge_mas, smbh_m)
    # plt.scatter(spc_bm, smbh_m, c='r')
    # plt.show()
    plt.savefig('bulge-smbh2.png')

    # print(smbh_m)
    # print(virial_mass)

    plt.xlabel('mtot')
    plt.ylabel('smbh_m')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(3e11, 1e15)
    plt.ylim(3e6, 5e11)
    plt.scatter(virial_mass, smbh_m, s=1)
    # plt.show()
    plt.savefig('smbh-mtot2.png')


# TODO choose between csv and npy
# category = ['none' for i in range(len(luminosity_AGN_reduced_arr[0]))]
#
# np.savez(str(params_path) + params_output_name + model_type[out_index] + 'lum_none',
#          radius=radius_more_than_20_arr, velocity=dot_radius_reduced_arr, time=time_reduced_arr,
#          dot_mass=dot_mass_reduced_arr, luminosity=luminosity_AGN_reduced_arr, category=category)
