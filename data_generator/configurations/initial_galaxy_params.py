import math

import numpy as np

import configurations.units as unt
from configurations.constants import RADIATIVE_EFFICIENCY_ETA

# TODO maybe these should be red from file?

# np.random.seed(7)
# smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=150)
# smbh_masses_initial1 = np.random.uniform(7.95, 8.1, size=5)
# smbh_masses_initial = 10**smbh_masses_initial1
# predictions
# smbh_masses_initial = np.array([6.5419731e8/unt.unit_sunmass])
# smbh_masses_initial = np.array([2.4641722e8/unt.unit_sunmass])
# smbh_masses_initial = np.array([5.2158003e8/unt.unit_sunmass])
# smbh_masses_initial = smbh_masses_initial/ unt.unit_sunmass
# smbh_masses_initial =[]
# tekme1

# Total SMBH mass (no dark matter) MOST LIKELY UNUSED, IT'S CALCULATED FROM VIRIAL MASS IN MAIN.PY
smbh_masses_initial = np.array([3.7469304e7/unt.unit_sunmass])

# bulge_masses_initial = np.array([2.3859397e10])
# bulge_masses_initial = np.array([1.9936952e11])
# tekme1

# Total bulge mass (including SMBH? no dark matter) MOST LIKELY UNUSED, IT'S CALCULATED FROM SMBH MASS IN MAIN.PY
bulge_masses_initial = np.array([1.1056635e10])
# bulge_masses_initial = []

# bulge_disc_gas_fractions = np.linspace(0.2, 0.4, 3)
# outflow_sphere_angle_ratio = np.linspace(1, 1, 1)
# tekme1

# Ratio of outflow as a fraction of a full "sphere"
outflow_sphere_angle_ratio = np.array([0.3369176])

# outflow_sphere_angle_ratio = np.linspace(0.3, 1, 4)

# bulge_disc_gas_fractions = np.linspace(0.2, 0.4, 2)
# tekme1

# Bulge/ALL gas fraction
bulge_disc_gas_fractions = np.array([0.06823811])
# bulge_disc_gas_fractions = np.array([0.01, 0.04, 0.12, 0.25, 0.4])
# bulge_disc_gas_fractions = np.linspace(0.2, 0.4, 2)
# predictions
# bulge_disc_gas_fractions = np.array([0.02091882])
# bulge_disc_gas_fractions = np.array([0.1639377])
# bulge_disc_gas_fractions = np.array([0.12597907])

# bulge_disc_gas_fractions = np.linspace(0.1, 0.55, 5)
# bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]

# TODO maybe sample with non logarithmic scale?
# virial_galaxies_masses1 = np.random.uniform(13, 13, size=1)
np.random.seed(1)
# virial_galaxies_masses1 = np.random.uniform(12.8, 14, size=30)
# tekme1

# Total galaxy mass (with dark matter)
virial_galaxies_masses = np.array([4.9432725e+12])
# virial_galaxies_masses1 = np.random.uniform(12.0, 14.0, size=40)

# virial_galaxies_masses1 = np.random.uniform(12.4, 14.05, size=30)
# virial_galaxies_masses = 10**virial_galaxies_masses1
#
# predictions
# virial_galaxies_masses = np.array([1.0805586e13 / 8.5979939e12])
# virial_galaxies_masses = np.array([8.5979939e12 / 8.5979939e12])
# virial_galaxies_masses = np.array([1.6345322e13])

virial_galaxies_masses = virial_galaxies_masses / unt.unit_sunmass
# virial_galaxies_masses = [1.e13 / unt.unit_sunmass]

# ¯\_(ツ)_/¯
halo_concentration_parameter = 10

# Gas fraction in the halo
halo_gas_fraction = 1.e-3
# TODO probably this one to change from elliptical to different type galaxy
# bulge_totalmasses = [1 for i in range(0, ITERATIONS_NUM)]  
# Bulge-to-total mass ratio
bulge_to_total_mass = 1

# Eddington ratio - google it
eddingtion_ratio = 1.
# Integration parameters (both of them):
drop_timescale = 3.e5 / unt.unit_year
alpha_drop = 0.5

# Parametras iš šviesio funkcijų
duration_coef_exp_law = math.log(0.01)*drop_timescale

# quasar_dt = 1.e6 / unt.unit_year #time between successive quasar phases
# quasar_dts = [quasar_dt for i in range(0, ITERATIONS_NUM)]  # 1.d6/unityear time between successive quasar phases
# quasar_duration = 5.e4 / unit_year
# quasar_duration = 5.e10 / unt.unit_year
np.random.seed(4)
# duty_cycles = np.linspace(0.12, 0.12, 1)
# duty_cycles = np.linspace(0.1, 0.5, 3)

# tekme1
# Decides length of pauses between Quasar activity periods (see quasar_durations),
# approximately - fraction of time that Quasars are active
duty_cycles = np.array([0.20755565])
# duty_cycles = np.linspace(0.04, 0.4, 5)
# duty_cycles = np.linspace(0.05, 0.5, 4)
# duty_cycles = np.linspace(0.05, 0.5, 7)

# predictions
# duty_cycles = np.array([0.5847862])
# duty_cycles = np.array([0.23893265])
# duty_cycles = np.array([0.09565598])

# quasar_durations = np.linspace(1e4, 1e5, 3)
# quasar_durations = np.linspace(1e4, 1e5, 3)
# quasar_durations = np.linspace(1e5, 1e5, 1)

# quasar_durations = np.linspace(9.7e3, 1.15e5, 10)

# tekme1
# Duration of one Quasar activity period (in years)
quasar_durations = np.array([38015.47])
# quasar_durations = np.linspace(9.7e3, 1.1e5, 4)

# predictions
# quasar_durations = np.array([50059.734/ unt.unit_year])
# quasar_durations = np.array([71007.82/ unt.unit_year])
# quasar_durations = np.array([120702.66 / unt.unit_year])
quasar_durations = quasar_durations / unt.unit_year
# print(quasar_durations)
# quasar_durations = [quasar_duration for i in range(0, ITERATIONS_NUM)]  # ;quasar duration
# SMBH growth timescale at Eddington rate - Salpeter timescale
salpeter_timescale = 4.5e8 * RADIATIVE_EFFICIENCY_ETA / unt.unit_year  

# duty_cycle = 0.1
# TODO add variation of quasar_dts
# quasar_dts = quasar_durations / duty_cycle

dot_radius = 0
radius = 0.001 / unt.unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0