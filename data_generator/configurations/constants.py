from data_generator.configurations.units import unit_year, unit_kpc
from enum import Enum


TIMESTEPS_NUMB = 30000


DT_MIN = 1 / unit_year  # ;1 year
# DT_MAX = 15000. * DT_MIN  # ;15000 years
# DT_MAX = 150000. * DT_MIN  # ;15000 years
# DT_MAX = 80000. * DT_MIN  # ;15000 years
DT_MAX_SMALL_OUTFLOWS = 45000. * DT_MIN
DT_MAX_VERY_SMALL_OUTFLOWS = 15000. * DT_MIN
DT_MAX_INTERMEDIATE_OUTFLOWS = 85000. * DT_MIN
DT_MAX_BIG_OUTFLOWS = 120000. * DT_MIN

T_MAX = 1.5e8 / unit_year  # ;time until the end of simulation, in years
R_MAX = 200. / unit_kpc  # ;stop the simulation once the c.d. reaches this radius_

RADIATIVE_EFFICIENCY_ETA = 0.1  # ;radiative efficiency
GAMMA = 5./3. #;adiabatic index of the outflowing material

TIME_MAX = 1.5e8/unit_year            #;time until the end of simulation, in years
RADIUS_MAX = 12./unit_kpc             #;stop the simulation once the c.d. reaches this radius

ETA_DRIVE = 0.05                        #coupling efficiency between luminosity or momentum and driving power/force ///

class PROFILE_TYPES(Enum):
    ISOTHERMAL = 'Isothermal'
    HERNQUIST = 'Hernquist'
    JAFFE = 'Jaffe'
    NFW = 'NFW'


class DISC_PROFILE(Enum):
    EXPONENTIAL = 'Exponential'


class FADE(Enum):
    NONE = 'none'
    EXPONENTIAL = 'exponential'
    POWER_LAW = 'power_law'
    KING = 'king'

# FADE_dict = {0: FADE.NONE, 1:FADE.EXPONENTIAL, 2: FADE.POWER_LAW, 3: FADE.KING}


class DRIVING_FORCE(Enum):
    ENERGY_DRIVING = 'energy_driving'
    MOMENTUM_DRIVING = 'momentum_driving'


class INTEGRATION_METHOD(Enum):
    SIMPLE_INTEGRATION = 'simple_integration'
    LEAP_FROG_DKD = 'leap_frog_dkd'
    LEAP_FROG_KDK = 'leap_frog_dkd'

class PROPERTIES_MAP_COLUMNS(Enum):
    SMBH_MASS = 'smbh_mass'
    BULGE_MASS = 'bulge_mass'
    BULGE_GAS_FRAC = 'bulge_gas_frac'
    GALAXY_MASS = 'galaxy_mass'
    QUASAR_DURATION = 'quasar_duration'
    FADE_TYPE = 'fade_type'
    DUTY_CYCLE = 'duty_cycle'
    PARAMS_INDEX = 'params_index'
    GALAXY_INDEX = 'galaxy_index'
    OUTFLOW_SPHERE_ANGLE = 'outflow_sphare_angle'
