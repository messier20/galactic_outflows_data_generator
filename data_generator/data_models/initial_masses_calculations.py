import numpy as np

from data_generator.configurations.physical_values import intercept_alpha, slope_beta, bulge_normalization_mass
from data_generator.configurations.units import unit_sunmass


def calc_bulge_masses(smbh_mass, index, size, alpha=intercept_alpha, beta=slope_beta, norm_mass=bulge_normalization_mass):
    alpha_left = alpha + 0.6
    alpha_right = alpha - 0.6

    # theor_bulge_mass_log_right = (np.log10(smbh_mass) - alpha_right) / beta
    theor_bulge_mass_log_right = (np.log10(smbh_mass * unit_sunmass) - alpha_right) / beta
    # theor_bulge_mass_log_left = (np.log10(smbh_mass) - alpha_left) / beta
    theor_bulge_mass_log_left = (np.log10(smbh_mass * unit_sunmass) - alpha_left) / beta
    spetial_bm = (np.log10(smbh_mass * unit_sunmass) - alpha) / beta
    theor_bulge_mass_right = (10 ** theor_bulge_mass_log_right) * norm_mass
    theor_bulge_mass_left = (10 ** theor_bulge_mass_log_left) * norm_mass
    # print(smbh_mass, 'bh')
    s = int(np.ceil(smbh_mass*10000))
    np.random.seed(s)
    # np.random.seed(index)
    bulge_masses_log = np.random.uniform(theor_bulge_mass_log_left, theor_bulge_mass_log_right, size=size)
    return ((10 ** bulge_masses_log) * 1e11)
    # a = ((10 ** bulge_masses_log) * 1e11) * unit_sunmass
    # print(a, 'bm')
    # return a

def calc_smbh_masses(virial_mass):

    np.random.seed(int(np.ceil(virial_mass)))
    # log_smbh_mass = 8.18 + (1.55*(np.log10(virial_mass) - 13.0))
    # alpha = 8.18 + 0.13
    alpha_left = 8.18 + 0.4
    alpha_right = 8.18 - 0.4
    # alpha_right = 8.18
    # alpha_left = 8.18
    # beta_left = 1.57 + 0.39
    # beta_right = 1.57 - 0.39
    beta_left = 1.57
    beta_right = 1.57

    alpha_parameters = np.random.uniform(alpha_left, alpha_right, 1)
    # alpha_parameters = np.random.normal(8.18, 0.13, 1)
    beta_parameters = np.random.uniform(beta_left, beta_right, 1)
    # beta_parameters = np.random.normal(1.57, 0.39, 1)

    log_smbh_mass = alpha_parameters + (beta_parameters * (np.log10(virial_mass * unit_sunmass) - 13.0))
    # log_smbh_mass = 8.18 + (1.55 * (np.log10(virial_galaxy_mass) - 13.0))
    smbh_mass = 10 ** log_smbh_mass
    return smbh_mass / unit_sunmass
