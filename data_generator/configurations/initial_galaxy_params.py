import numpy as np

import data_generator.configurations.units as unt
from data_generator.configurations.constants import RADIATIVE_EFFICIENCY_ETA

# np.random.seed(7)
# smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=150)
# smbh_masses_initial1 = np.random.uniform(7.95, 8.1, size=5)
# smbh_masses_initial = 10**smbh_masses_initial1
# smbh_masses_initial = smbh_masses_initial/ unt.unit_sunmass

smbh_masses_initial = []

bulge_disc_gas_fractions = np.linspace(0.1, 0.55, 3)
# bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]

# TODO maybe sample with non logarithmic scale?
# virial_galaxies_masses1 = np.random.uniform(13, 13, size=1)
np.random.seed(1)
virial_galaxies_masses1 = np.random.uniform(12.2, 14.05, size=50)
virial_galaxies_masses = 10**virial_galaxies_masses1
#
virial_galaxies_masses = virial_galaxies_masses / unt.unit_sunmass
# virial_galaxies_masses = [1.e13 / unt.unit_sunmass]


halo_concentration_parameter = 10

halo_gas_fraction = 1.e-3  # gas fraction in the halo
# TODO probably this one to change from elliptical to different type galaxy
# bulge_totalmasses = [1 for i in range(0, ITERATIONS_NUM)]  # bulge-to-total mass ratio
bulge_to_total_mass = 1


eddingtion_ratio = 1.
drop_timescale = 3.e5 / unt.unit_year
alpha_drop = 0.5

# quasar_dt = 1.e6 / unt.unit_year #time between successive quasar phases
# quasar_dts = [quasar_dt for i in range(0, ITERATIONS_NUM)]  # 1.d6/unityear time between successive quasar phases
# quasar_duration = 5.e4 / unit_year
# quasar_duration = 5.e10 / unt.unit_year
np.random.seed(4)
duty_cycles = np.linspace(0.05, 0.5, 3)

quasar_durations = np.linspace(9.7e3, 1.15e5, 4)
quasar_durations = quasar_durations / unt.unit_year
# print(quasar_durations)
# quasar_durations = [quasar_duration for i in range(0, ITERATIONS_NUM)]  # ;quasar duration
salpeter_timescale = 4.5e8 * RADIATIVE_EFFICIENCY_ETA / unt.unit_year  #;SMBH growth timescale at Eddington rate - Salpeter timescale

duty_cycle = 0.1
# TODO add variation of quasar_dts
quasar_dts = quasar_durations / duty_cycle

dot_radius = 0
radius = 0.001 / unt.unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0