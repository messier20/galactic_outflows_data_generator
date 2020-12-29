import itertools
import math
import time

import matplotlib.pyplot as plt
import pandas as pd

import configurations.initial_galaxy_params as init
import configurations.switches as swch
import configurations.units as unt
from configurations.path_version_settings import params_path, values_version_folder, version, \
    predictions_file
from data_models.arrays_modifier import *
from mathematical_calculations.DrivingForceIntegrator import DrivingForceIntegrator
from mathematical_calculations.FadeTypeSwitcher import FadeTypeSwitcher
from mathematical_calculations.mass_calculation import mass_calculation

all_params_columns = ['radius', 'dot_radius', 'derived_dot_mass', 'mass_out', 'luminosity_AGN', 'smbh_mass', \
                              'duty_cycle', 't_initial_smbh_mass', 'bulge_mass', 'bulge_gas', 'galaxy_mass', \
                              'quasar_duration', 'fade_type', 'outflow_sphare_angle']
columns = 'radius_arr', 'dot_radius_arr', 'time_arr', 'dot_mass_arr', 'mass_out_arr', 'total_mass_arr', 'luminosity_AGN_arr'


def run_outflow_simulation(
    init_params,
    outf_name,
    db_file_header,
    failed_outflows_mode_header,
    df_index,
    virial_mass=[],
    smbh_m=[],
    bulge_mas=[]):
    '''
        outf_name: name used for mapping outflows later (NN code?)
        db_file_header: On first iteration forces 'w' mode on files, later turns on 'a'
        failed_outflows_mode_header: When outflow calculations fail this gets set to True, afterwards outputs are written to a separate file
        df_index: pandas table index, increments by 1 each iteration, makes tables behave >:(
        out_indx: current galaxy (parameter set) index, used for file naming when outputting - first number in file name
        variant_index: outer loop index (so either mass or fade type) - second number in file name
    '''
    out_indx = 0
    variant_index = 0
    
    if swch.testing_phase:
        subtracted_indices_count = 42
        dtmax = const.DT_MAX_VERY_SMALL_OUTFLOWS
    else:
        # TODO change to switch
        # TODO maybe I can write a function for subtracted_indices_count depending on duty cycle
        # If Quasars are active longers - increas upper bound of time step, because we won't be missing much
        if init_params.duty_cycle < 0.07:
            subtracted_indices_count = 42
            dtmax = const.DT_MAX_VERY_SMALL_OUTFLOWS
        elif init_params.duty_cycle < 0.15:
            subtracted_indices_count = 32
            dtmax = const.DT_MAX_SMALL_OUTFLOWS
        elif init_params.duty_cycle < 0.26:
            subtracted_indices_count = 22
            dtmax = const.DT_MAX_INTERMEDIATE_OUTFLOWS
        else:
            subtracted_indices_count = 12
            dtmax = const.DT_MAX_BIG_OUTFLOWS

    # for bulge_index, bulge_disc_totalmass_fraction in enumerate(bulge_disc_totalmass_fractions):

    radius_arr, dot_radius_arr, dotdot_radius_arr, dotdotdot_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, time_arr, \
    dot_time_arr, luminosity_AGN_arr, smbh_mass_arr, bulge_mass_arr = init_zero_arrays(arrays_count=12)
    radius_arr[0] = init.radius
    dot_radius_arr[0] = init.dot_radius
    dotdot_radius_arr[0] = init.dotdot_radius
    smbh_mass_arr[0] = init_params.smbh_mass

    is_main_loop = True
    index = 0
    while is_main_loop:
        failed_calc = False
        # mass_potential is ALL mass (dark matter, stars, SMBH) without gas (WITHIN CURRENT RADIUS)
        # mass_gas is ONLY gas mass (WITHIN CURRENT RADIUS)
        # rho_gas is gas density
        # phi potential
        # mass_bulge is bulge mass (WITHIN CURRENT RADIUS)
        (mass_potential, dot_mass_potential, mass_gas, dot_mass_gas, dotdot_mass_gas, rho_gas, phi,
         phigrad, rhog_as2, mass_bulge) = mass_calculation(
            radius_arr[index],
            dot_radius_arr[index],
            dotdot_radius_arr[index],
            init_params.virial_mass,
            init_params.virial_radius,
            init_params.halo_concentration,
            init_params.bulge_scale,
            init_params.bulge_to_total_mass_fraction,
            init_params.halo_gas_fraction,
            init_params.bulge_disc_gas_fraction,
            init_params.bulge_to_total_mass_fraction
        )

        '''
        1. Calculate mass within radius
        2. Out of that calculate time step
        3. Calculate radius (?)
        '''
        # mass_out - the mass of the outflow (it's only gas, duh)
        mass_out_arr[index] = mass_gas
        # reminder: mass_potential is mass of everything except gas
        total_mass_arr[index] = mass_gas + mass_potential
        # Amount of mass per unit of time
        dot_mass_arr[index] = dot_mass_gas
        bulge_mass_arr[index] = mass_bulge

        # TODO change to one function
        # radius / speed -> time
        dot_t1 = (radius_arr[index] + 1.e-8) / (dot_radius_arr[index] + 1.e-8)
        # greitis / pagreitis -> time what is time?
        dot_t2 = (dot_radius_arr[index] + 1.e-8) / (dotdot_radius_arr[index] + 1.e-8)
        dot_t3 = (dotdot_radius_arr[index] + 1.e-8) / (dotdotdot_radius_arr[index] + 1.e-8)

        if index > 0:
            # Most conservative time step size
            dt = 0.1 * min(abs(dot_t1), abs(dot_t2), abs(dot_t3))

            # If we're jumping over a quasar inactivity period, make time step lower to start at some inactivity period or something idunno
            if ((time_arr[index] + dt) // init_params.quasar_dt) > (time_arr[index] // init_params.quasar_dt):
                dt = init_params.quasar_dt * ((time_arr[index] + dt) // init_params.quasar_dt) - time_arr[index]

            if dt > dtmax / 100. * (10. * time_arr[index] + 1.):
                dt = dtmax / 100. * (10. * time_arr[index] + 1.)
            if dt < const.DT_MIN:
                dt = const.DT_MIN
        else:
            dt = const.DT_MIN
        # Note: dt is just a time step
        dot_time_arr[index + 1] = dt
        time_arr[index + 1] = time_arr[index] + dt

        if swch.repeating_equation:
            time_eff = time_arr[index] % init_params.quasar_dt
        else:
            time_eff = time_arr[index]

        # How much luminosity gets reduced, mainly decided by time
        luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(
            init_params.fade, time_eff,
            init_params.quasar_activity_duration,
            init_params.eddington_ratio
        )

        # How much luminosity does the SMBH produce in total                                                        
        luminosity_edd = 1.3e38 * (
                smbh_mass_arr[
                    index] * unt.unit_mass / 1.989e33) * unt.unit_time / unt.unit_energy  # ;eddington luminosity for the current SMBH mass

        luminosity = luminosity_coef * luminosity_edd
        luminosity_AGN_arr[index + 1] = luminosity  # ;actual luminosity

        # SMBH increases in mass
        if swch.smbh_grows:
            smbh_mass_arr[index + 1] = smbh_mass_arr[index] * math.exp(luminosity_coef * dt / init_params.salpeter_timescale)
        # TODO change implementation without passing arrays or without passing separate array elements
        # Calculates next radius and its derivatives from various current parameters
        (radius_arr, dot_radius_arr, dotdot_radius_arr, dotdotdot_radius_arr) = \
            Integrator.driving_force_calc(swch.driving_force, mass_gas, radius_arr[index], const.ETA_DRIVE,
                                          swch.integration_method, luminosity, dot_mass_gas,
                                          dot_radius_arr[index], dotdot_radius_arr[index], mass_potential,
                                          dot_mass_potential,
                                          dotdot_mass_gas,
                                          dotdotdot_radius_arr, radius_arr,
                                          dot_radius_arr, dotdot_radius_arr, index, dt)

        if radius_arr[index + 1] < 0.00000000000000:
            print('ups, calc failed')
            failed_calc = True
            is_main_loop = False

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
    # TODO pressure might be calculated incorrectly, needs to be checked
    # pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
    # pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
    mv = (mass_out_arr * unt.unit_sunmass) * init_params.outflow_sphere_angle_ratio * dot_radius_arr * 1.02269032e-9
    derived_dot_mass = np.divide(mv, radius_arr)
    # dot_mass_arr = dot_mass_arr * unt.unit_sunmass / unt.unit_year
    mass_out_arr = mass_out_arr * init_params.outflow_sphere_angle_ratio * unt.unit_sunmass
    total_mass_arr = total_mass_arr * unt.unit_sunmass
    smbh_mass_arr = smbh_mass_arr * unt.unit_sunmass
    luminosity_AGN_arr = luminosity_AGN_arr * unt.unit_energy / unt.unit_time

    # w_bulge_mass_arr = bulge_mass_arr * unt.unit_sunmass
    w_initial_smbh_mass = init_params.smbh_mass * unt.unit_sunmass
    w_virial_galaxy_mass = init_params.virial_mass * unt.unit_sunmass
    w_quasar_duration = init_params.quasar_activity_duration * unt.unit_year

    # observed_time_arr = radius_arr / dot_radius_arr

    # reducion_indices = np.where(time_arr > 1e4)
    reducion_indices = np.where(radius_arr > 0.02)
    # observed_time_reduced_arr = np.where(radius_arr > 0.02, observed_time_arr, np.nan)

    outflow_properties_df = pd.DataFrame(
        np.array([radius_arr[reducion_indices], dot_radius_arr[reducion_indices], time_arr[reducion_indices],
                  derived_dot_mass[reducion_indices], mass_out_arr[reducion_indices],
                  total_mass_arr[reducion_indices], luminosity_AGN_arr[reducion_indices]]).transpose())
    outflow_properties_df.columns = columns

    if failed_calc:
        outflow_properties_df.to_csv(
            (str(params_path) + values_version_folder + '_failed' + str(
                out_indx) + '_' + str(variant_index) + '.csv'),
            header=True, index=False)
    else:
        out_temp_name = str(params_path) + values_version_folder + '_' + str(
            out_indx) + '_' + str(variant_index)
        outflow_properties_df.to_csv(
            (out_temp_name + '.csv'),
            header=True, index=False)
        smbh_m.append(w_initial_smbh_mass)
        # bulge_mas.append(bulge_masses[0])
        bulge_mas.append(init_params.bulge_mass)
        virial_mass.append((w_virial_galaxy_mass))

    del outflow_properties_df

    galaxy_properties_df = pd.DataFrame({'smbh_mass': w_initial_smbh_mass, 'bulge_mass': init_params.bulge_mass,
                                         'bulge_gas_frac': init_params.bulge_disc_gas_fraction, 'galaxy_mass': w_virial_galaxy_mass,
                                         'quasar_duration': w_quasar_duration, 'fade_type': init_params.fade.value,
                                         'duty_cycle': init_params.duty_cycle,
                                         'params_index': out_indx, 'variant_loop_index': variant_index,
                                         'outflow_sphare_angle': init_params.outflow_sphere_angle_ratio, 'name': outf_name}, index=[df_index])

    mode = 'w' if db_file_header else 'a'
    failed_outflows_mode = 'w' if failed_outflows_mode_header else 'a'

    if failed_calc:
        galaxy_properties_df.to_csv((str(params_path) + values_version_folder + 'failed_outflows.csv'),
                                    mode=failed_outflows_mode, header=failed_outflows_mode_header, index=False)
        failed_outflows_mode_header = False

    else:
        galaxy_properties_df.to_csv((str(params_path) + values_version_folder + 'properties_map.csv'), mode=mode,
                                    header=db_file_header, index=False)
    # db_file_header = False
    # df_index +=1
    del galaxy_properties_df

    if not failed_calc:
        rng = np.random.RandomState(variant_index + out_indx)
        subtracted_indices = reducion_indices[0]
        rng.shuffle(subtracted_indices)
        # subtracted_indices = subtracted_indices[::10]
        subtracted_indices = subtracted_indices[::subtracted_indices_count]
        # subtracted_indices = subtracted_indices[::13]
        # subtracted_indices = subtracted_indices[::8]

        # TODO move to function?
        temp_initial_smbh_mass = [w_initial_smbh_mass for i in range(len(subtracted_indices))]
        temp_bulge_masses = [init_params.bulge_mass for i in range(len(subtracted_indices))]
        temp_bulge_disc_gas_fraction = [init_params.bulge_disc_gas_fraction for i in range(len(subtracted_indices))]
        temp_virial_galaxy_mass = [w_virial_galaxy_mass for i in range(len(subtracted_indices))]
        temp_quasar_duration = [w_quasar_duration for i in range(len(subtracted_indices))]
        temp_duty_cycle = [init_params.duty_cycle for i in range(len(subtracted_indices))]
        temp_outf_angle = [init_params.outflow_sphere_angle_ratio for i in range(len(subtracted_indices))]

        temp_fade = [init_params.fade.value for i in range(len(subtracted_indices))]

        all_parameters = np.column_stack([radius_arr[subtracted_indices], dot_radius_arr[subtracted_indices],
                                          derived_dot_mass[subtracted_indices], mass_out_arr[subtracted_indices],
                                          luminosity_AGN_arr[subtracted_indices],
                                          smbh_mass_arr[subtracted_indices], temp_duty_cycle,
                                          temp_initial_smbh_mass, temp_bulge_masses,
                                          temp_bulge_disc_gas_fraction, temp_virial_galaxy_mass,
                                          temp_quasar_duration, temp_fade, temp_outf_angle])

        df_all_parameters = pd.DataFrame(all_parameters, columns=all_params_columns)

        mode = 'w' if db_file_header else 'a'
        df_all_parameters.to_csv((str(params_path) + values_version_folder + 'train_data' + str(version) + '.csv'),
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
        del temp_outf_angle

    return db_file_header, df_index, virial_mass, smbh_m, bulge_mas, failed_outflows_mode_header


if __name__ == '__main__':

    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()

    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()
    db_file_header = True
    failed_outflows_mode_header = True
    df_index = 0
    virial_mass = []
    smbh_m = []
    bulge_mas = []
    
    rng = np.random.RandomState(0)
    initial_galaxy_parameters = init.InitialGalaxyParameters(rng=rng)

    (db_file_header, df_index, virial_mass, smbh_m, bulge_mas, failed_outflows_mode_header) = run_outflow_simulation(
        initial_galaxy_parameters,
        False,
        db_file_header,
        failed_outflows_mode_header,
        df_index,
        virial_mass,
        smbh_m,
        bulge_mas)

    print('passed time', time.time() - start_time)

    plt.xlabel('mbulge')
    plt.ylabel('smbh_m')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e8, 1e14)
    plt.ylim(3e5, 5e11)
    plt.scatter(bulge_mas, smbh_m)
    plt.savefig(params_path + 'graphs/bulge-smbh' + str(version) + '.png')
    plt.close()

    plt.xlabel('mtot')
    plt.ylabel('smbh_m')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(3e11, 1e15)
    plt.ylim(3e6, 5e11)
    plt.scatter(virial_mass, smbh_m, s=1)
    plt.savefig(params_path + 'graphs/smbh-mtot' + str(version) + '.png')
