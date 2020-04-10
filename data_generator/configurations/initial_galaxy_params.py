import data_generator.configurations.units as unt
import numpy as np
import matplotlib.pyplot as plt

# from data_generator.data_models._initial_masses_calculations import calc_smbh_bulge_masses

np.random.seed(7)
smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=150)
smbh_masses_initial = 10**smbh_masses_initial1
bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]

virial_galaxies_masses1 = np.random.uniform(10, 14, size=50)
virial_galaxies_masses = 10**virial_galaxies_masses1

halo_concentration_parameter = 10

halo_gas_fraction = 1.e-3  # gas fraction in the halo
# TODO probably this one to change from elliptical to different type galaxy
# bulge_totalmasses = [1 for i in range(0, ITERATIONS_NUM)]  # bulge-to-total mass ratio
bulge_to_total_mass = 1

# bulge_masses = calc_bulge_masses(smbh_mass_init, out_indx)
# smbh_masses_initial = calc_smbh_bulge_masses()

# print(mass_tuple)
# print(np.array(mass_tuple).shape)


dot_radius = 0
radius = 0.001 / unt.unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0