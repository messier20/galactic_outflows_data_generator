import data_generator.configurations.constants as const

repeating_equation = True
smbh_grows = False

halo_profile = const.PROFILE_TYPES.NFW
bulge_profile = const.PROFILE_TYPES.ISOTHERMAL
disc_profile = const.DISC_PROFILE.EXPONENTIAL

fade = const.FADE.NONE
fade_arr = [const.FADE.NONE, const.FADE.EXPONENTIAL, const.FADE.POWER_LAW, const.FADE.KING]
driving_force = const.DRIVING_FORCE.ENERGY_DRIVING
integration_method = const.INTEGRATION_METHOD.SIMPLE_INTEGRATION

