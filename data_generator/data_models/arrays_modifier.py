import numpy as np
import configurations.constants as const
import configurations.initial_galaxy_params as params


def init_zero_arrays(arrays_count):
    return (np.zeros(const.TIMESTEPS_NUMB,) for i in range(arrays_count))
    # return (np.zeros(const.TIMESTEPS_NUMB),) * arrays_count


def get_galaxy_params_lists():
    # TODO think if dictionary is more logical approach
    # return {'bulge_masses': params.bulge_masses, 'bulge_disc_gas_fractions': params.bulge_disc_gas_fractions}
    return params.smbh_masses_initial, params.bulge_disc_gas_fractions
