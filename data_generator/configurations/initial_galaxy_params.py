import data_generator.configurations.units as unt
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)
smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=280)
smbh_masses_initial = 10**smbh_masses_initial1
# smbh_masses_initial = np.logspace(6.3, 9.85, num= 25, dtype='int64')
bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]



dot_radius = 0
radius = 0.001 / unt.unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0