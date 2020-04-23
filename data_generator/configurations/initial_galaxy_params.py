from MiraTitanHMFemulator import MiraTitanHMFemulator

import data_generator.configurations.units as unt
import numpy as np
import matplotlib.pyplot as plt

# from data_generator.data_models._initial_masses_calculations import calc_smbh_bulge_masses
from data_generator.configurations.constants import RADIATIVE_EFFICIENCY_ETA
from hmf.hmf import get_hmf

# np.random.seed(7)
smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=150)
# smbh_masses_initial1 = np.random.uniform(7.95, 8.1, size=5)
# smbh_masses_initial = 10**smbh_masses_initial1
# smbh_masses_initial = smbh_masses_initial/ unt.unit_sunmass

smbh_masses_initial = []

bulge_disc_gas_fractions = np.linspace(0.1, 0.6, 5)
# bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]

# TODO maybe sample with non logarithmic scale?
# virial_galaxies_masses1 = np.random.uniform(13, 13, size=1)
np.random.seed(1)
virial_galaxies_masses1 = np.random.uniform(12.1, 14.8, size=100)
virial_galaxies_masses = 10**virial_galaxies_masses1
#
virial_galaxies_masses = virial_galaxies_masses / unt.unit_sunmass
# virial_galaxies_masses = [1.e13 / unt.unit_sunmass]

# virial_galaxies_masses = virial_galaxies_masses*unt.unit_sunmass

# HMFemu = MiraTitanHMFemulator.Emulator()
# fiducial_cosmo = {'Ommh2': .3*.7**2,
#                   'Ombh2': .022,
#                   'Omnuh2': .0006,
#                   'n_s': .96,
#                   'h': .7,
#                   'w_0': -1,
#                   'w_a': 0,
#                   'sigma_8': .8,
#                  }
#
# raw_res = HMFemu.predict_raw_emu(fiducial_cosmo)
#
# print(len(raw_res[0.0]['log10_M']), 'masses')
# virial_galaxies_masses = raw_res[0.0]['log10_M']
# virial_galaxies_masses = (10**virial_galaxies_masses)*0.6777

halo_concentration_parameter = 10

halo_gas_fraction = 1.e-3  # gas fraction in the halo
# TODO probably this one to change from elliptical to different type galaxy
# bulge_totalmasses = [1 for i in range(0, ITERATIONS_NUM)]  # bulge-to-total mass ratio
bulge_to_total_mass = 1

# bulge_masses = calc_bulge_masses(smbh_mass_init, out_indx)
# smbh_masses_initial = calc_smbh_bulge_masses()

# print(mass_tuple)
# print(np.array(mass_tuple).shape)
eddingtion_ratio = 1.
drop_timescale = 3.e5 / unt.unit_year
alpha_drop = 0.5

# quasar_dt = 1.e6 / unt.unit_year #time between successive quasar phases
# quasar_dts = [quasar_dt for i in range(0, ITERATIONS_NUM)]  # 1.d6/unityear time between successive quasar phases
# quasar_duration = 5.e4 / unit_year
# quasar_duration = 5.e10 / unt.unit_year
np.random.seed(4)
# quasar_durations1 = np.random.uniform(3.8, 5.1, 7)
# quasar_durations = 10**quasar_durations1
# quasar_durations = np.logspace(3.8, 5.1, 7)
quasar_durations = np.linspace(8.e3, 2.e5, 7)
quasar_durations = quasar_durations / unt.unit_year
# print(quasar_durations)
# quasar_durations = [quasar_duration for i in range(0, ITERATIONS_NUM)]  # ;quasar duration
salpeter_timescale = 4.5e8 * RADIATIVE_EFFICIENCY_ETA / unt.unit_year  #;SMBH growth timescale at Eddington rate - Salpeter timescale

duty_cycle = 0.1
# TODO add variation of quasar_dts
quasar_dts = quasar_durations / 0.1
quasar_dts = quasar_dts / unt.unit_year

dot_radius = 0
radius = 0.001 / unt.unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0