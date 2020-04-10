import itertools
import matplotlib.pyplot as plt
import data_generator.configurations.initial_galaxy_params as init
from data_generator.configurations.units import unit_sunmass, unit_kpc
from data_generator.data_models.initial_masses_calculations import calc_bulge_masses
from data_generator.data_models.arrays_modifier import *
import time

from data_generator.mathematical_calculations.mass_calculation import mass_calculation

mas = []
if __name__ == '__main__':
    # bulge_disc_gas_fraction
    for virial_galaxy_mass in init.virial_galaxies_masses:

        virial_radius = (626 * (((virial_galaxy_mass / (10 ** 13)) * unit_sunmass) ** (1 / 3))) / unit_kpc

        for out_indx, (smbh_mass_init, bulge_disc_gas_fraction) in enumerate(itertools.product(init.smbh_masses_initial,
                                                                    init.bulge_disc_gas_fractions)):

            is_main_loop = True
            radius_arr, dot_radius_arr, dotdot_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, time_arr, \
                dot_time_arr, luminosity_AGN_arr, smbh_mass_arr = init_zero_arrays(arrays_count=10)

            bulge_masses = calc_bulge_masses(smbh_mass_init, out_indx)
            # check if this shouldn't be division from virial galaxy mass
            bulge_disc_totalmass_fractions = bulge_masses/1.e13
            bulge_scales = [((bulge_mass / 1.e11) ** 0.88) * 2.4 * 2 / unit_kpc for bulge_mass in bulge_masses]
            print(bulge_scales)

            for bulge_index, bulge_disc_totalmass_fraction in enumerate(bulge_disc_totalmass_fractions):
                radius_arr[0] = init.radius
                dot_radius_arr[0] = init.dot_radius
                dotdot_radius_arr[0] = init.dotdot_radius


                index = 0
                while is_main_loop:
                    (mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2, mb) = \
                        mass_calculation(radius_arr[0], dot_radius_arr[0], dotdot_radius_arr[0], virial_galaxy_mass,
                                         virial_radius, init.halo_concentration_parameter, bulge_scales[bulge_index],
                                         bulge_disc_totalmass_fraction, init.halo_gas_fraction, bulge_disc_gas_fraction,
                                         init.bulge_to_total_mass)

                        # mass_calculation(radius_arr[k, index], dot_radius_arr[k, index], dotdot_radius_arr[k, index],
                        #                  delta_radius_arr[k, index], total_masses[k], virial_radiuses[k],
                        #                  halo_concentration_parameters[k],
                        #                  bulge_scale, disc_scale, bulge_disc_totalmass_fraction,
                        #                  halo_gas_fraction, bulge_disc_gas_fractions[k], bulge_totalmasses[k])

                    index = + 1
                    # print(index)
                    is_main_loop = False
