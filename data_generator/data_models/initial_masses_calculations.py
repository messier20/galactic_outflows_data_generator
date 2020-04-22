import numpy as np

from data_generator.configurations.physical_values import intercept_alpha, slope_beta, bulge_normalization_mass
from data_generator.configurations.units import unit_sunmass


def calc_bulge_masses(smbh_mass, index, alpha=intercept_alpha, beta=slope_beta, norm_mass=bulge_normalization_mass):
    alpha_left = alpha + 0.6
    alpha_right = alpha - 0.6

    theor_bulge_mass_log_right = (np.log10(smbh_mass) - alpha_right) / beta
    theor_bulge_mass_log_left = (np.log10(smbh_mass) - alpha_left) / beta
    theor_bulge_mass_right = (10 ** theor_bulge_mass_log_right) * norm_mass
    theor_bulge_mass_left = (10 ** theor_bulge_mass_log_left) * norm_mass
    np.random.seed(int(np.ceil(smbh_mass*100)))
    # np.random.seed(index)
    bulge_masses_log = np.random.uniform(theor_bulge_mass_log_left, theor_bulge_mass_log_right, size=2)
    return ((10 ** bulge_masses_log) * 1e11) * unit_sunmass

def calc_smbh_masses(virial_mass):
    log_smbh_mass = 8.18 + (1.55*(np.log10(virial_mass) - 13.0))


# def calc_smbh_bulge_masses():
#     smbh_bulge_mass_tuple = []
#     smbh_masses_initial1 = np.random.uniform(6.3, 9.85, size=150)
#     smbh_masses_initial = 10 ** smbh_masses_initial1
#
#     for index, smbh_mass in enumerate(smbh_masses_initial):
#         bulge_masses = calc_bulge_masses(smbh_mass, index)
#         print([(smbh_mass, bulge_mass) for bulge_mass in bulge_masses])
#         # smbh_bulge_mass_tuple[index] = [(smbh_mass, bulge_mass) for bulge_mass in bulge_masses]
#         # smbh_bulge_mass_tuple.append(tuple([smbh_mass, bulge_masses]))
#
#
#     print(smbh_bulge_mass_tuple)
#     return smbh_bulge_mass_tuple
