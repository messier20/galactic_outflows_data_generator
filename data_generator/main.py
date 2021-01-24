import itertools
import math
import os
import time

import matplotlib.pyplot as plt
import pandas as pd

import data_generator.configurations.initial_galaxy_params as init
import data_generator.configurations.switches as swch
import data_generator.configurations.units as unt
from data_generator.configurations.path_version_settings import params_path, values_version_folder, version, \
    predictions_file
from data_generator.data_models.arrays_modifier import *
from data_generator.mathematical_calculations.DrivingForceIntegrator import DrivingForceIntegrator
from data_generator.mathematical_calculations.FadeTypeSwitcher import FadeTypeSwitcher
from data_generator.mathematical_calculations.mass_calculation import mass_calculation


def run_outflow_simulation(init_params, dtmax=const.DT_MAX_VERY_SMALL_OUTFLOWS):
    fade_type_switcher = FadeTypeSwitcher()
    integrator = DrivingForceIntegrator()

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
        luminosity_coef = fade_type_switcher.calc_luminosity_coef(
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
            integrator.driving_force_calc(swch.driving_force, mass_gas, radius_arr[index], const.ETA_DRIVE,
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

    outflow_properties = pd.DataFrame(
        {
            "radius_arr": radius_arr,
            "dot_radius_arr": dot_radius_arr,
            "time_arr": time_arr,
            "dot_mass_arr": derived_dot_mass,
            "mass_out_arr": mass_out_arr,
            "total_mass_arr": total_mass_arr,
            "luminosity_AGN_arr": luminosity_AGN_arr,
            "failed_calc": failed_calc,
        }
    )

    return outflow_properties[outflow_properties["radius_arr"] > 0.02].reset_index(drop=True)


if __name__ == '__main__':

    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()
    
    initial_galaxy_parameters = init.InitialGalaxyParameters()

    rng = np.random.RandomState(0)
    initial_galaxy_parameters.generate_stochastic_parameters(rng)

    initial_galaxy_parameters.to_dataframe().to_csv(
        os.path.join(params_path, values_version_folder, "initial_galaxy_parameters.csv"),
        index=False,
        encoding="utf-8"
    )

    # If Quasars are active longers - increase upper bound of time step, because we won't be missing much
    if initial_galaxy_parameters.duty_cycle < 0.07:
        dtmax = const.DT_MAX_VERY_SMALL_OUTFLOWS
    elif initial_galaxy_parameters.duty_cycle < 0.15:
        dtmax = const.DT_MAX_SMALL_OUTFLOWS
    elif initial_galaxy_parameters.duty_cycle < 0.26:
        dtmax = const.DT_MAX_INTERMEDIATE_OUTFLOWS
    else:
        dtmax = const.DT_MAX_BIG_OUTFLOWS
    outflow_properties = run_outflow_simulation(initial_galaxy_parameters, dtmax=dtmax)

    outflow_properties.to_csv(
        os.path.join(params_path, values_version_folder, "outflow_properties.csv"),
        index=False,
        encoding="utf-8"
    )

    print('passed time', time.time() - start_time)
