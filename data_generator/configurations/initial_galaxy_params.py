from dataclasses import dataclass

import numpy as np

import configurations.units as unt
from configurations.constants import RADIATIVE_EFFICIENCY_ETA, FADE

@dataclass
class InitialGalaxyParameters:
    # Total galaxy mass (with dark matter)
    virial_mass: float = 4.9432725e+12 / unt.unit_sunmass

    # Bulge/all gas fraction
    bulge_disc_gas_fraction: float = 0.06823811

    # Amount of outflow as a fraction of a full "sphere"
    outflow_sphere_angle_ratio: float = 0.3369176

    # A property of NFW halos, = ratio of virial and scale radii
    halo_concentration: float = 10.0

    # Gas fraction in the halo
    halo_gas_fraction: float = 1.e-3

    # Eddington ratio - google it
    eddington_ratio: float = 1.0

    # Integration parameters (both of them):
    drop_timescale: float = 3.e5 / unt.unit_year
    alpha_drop: float = 0.5

    # Decides length of pauses between Quasar activity periods (see quasar_durations),
    # approximately - fraction of time that Quasars are active
    duty_cycle: float = 0.20755565

    # Duration of one Quasar activity period (in years)
    quasar_activity_duration: float = 38015.47 / unt.unit_year

    # SMBH growth timescale at Eddington rate - Salpeter timescale
    salpeter_timescale: float = 4.5e8 * RADIATIVE_EFFICIENCY_ETA / unt.unit_year

    fade: FADE = FADE.KING

    # Parametras iš šviesio funkcijų
    duration_coef_exp_law: float = np.log(0.01) * drop_timescale

    # Random number generator that contributes to smbh and bulge mass calculations
    rng: np.random.RandomState = None

    @property
    def virial_radius(self):
        return (626 * (((self.virial_mass / (10 ** 13)) * unt.unit_sunmass) ** (1 / 3))) / unt.unit_kpc

    @property
    def smbh_mass(self):
        # Calculate SMBH mass from total galaxy mass (including dark matter)
        # Bandara et al. 2009, doi: 10.1088/0004-637X/704/2/1135 (equation 8)
        free_coef = 8.18
        if self.rng:
            # We randomize the value of the first free coefficient to provide
            # a realistic spread of smbh masses. Note that the bounds here
            # are somewhat smaller than in the original equation and are
            # sampled uniformly.
            free_coef += self.rng.uniform(-0.4, 0.4)
        log_smbh_mass = free_coef + (1.55 * (np.log10(self.virial_mass * unt.unit_sunmass) - 13.0))
        smbh_mass = 10 ** log_smbh_mass
        return smbh_mass / unt.unit_sunmass

    @property
    def bulge_mass(self):
        # Calculate bulge mass from SMBH mass
        # McConnell & Ma 2013, doi: 10.1088/0004-637X/764/2/184 (see abstract)
        intercept_alpha = 8.46
        if self.rng:
            # We randomize the value of the first free coefficient to provide
            # a realistic spread of bulge masses. Note that the bounds here
            # were derived by visually inspecting the results.
            intercept_alpha += self.rng.uniform(0.6, -0.6)
        slope_beta = 1.05
        log_bulge_mass = (np.log10(self.smbh_mass * unt.unit_sunmass) - intercept_alpha) / slope_beta
        return (10 ** log_bulge_mass) * 1e11

    @property
    def bulge_to_total_mass_fraction(self):
        # Fraction of bulge vs whole galaxy mass
        return self.bulge_mass / (self.virial_mass * unt.unit_sunmass)

    @property
    def bulge_scale(self):
        # Mass normalization factor for integration (?)
        return ((self.bulge_mass / 1.e11) ** 0.88) * 2.4 * 2 / unt.unit_kpc

    @property
    def quasar_dt(self):
        if self.fade == FADE.KING:
            return 47.328 * self.quasar_activity_duration / self.duty_cycle
        elif self.fade == FADE.POWER_LAW:
            return 10000 * self.quasar_activity_duration / self.duty_cycle
        elif self.fade == FADE.EXPONENTIAL:
            return (self.quasar_activity_duration - self.duration_coef_exp_law) / self.duty_cycle
        elif self.fade == FADE.NONE:
            return self.quasar_activity_duration / self.duty_cycle

        raise AttributeError(
            "Unknown fade type %s, can't calculate quasar dt", self.fade
        )


dot_radius = 0
radius = 0.001 / unt.unit_kpc
var = 100000.0
dot_radius = var / unt.unit_velocity
dotdot_radius = 0
delta_radius = 0
