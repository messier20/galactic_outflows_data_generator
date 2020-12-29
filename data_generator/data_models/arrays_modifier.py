import numpy as np
import configurations.constants as const
import configurations.initial_galaxy_params as params


def init_zero_arrays(arrays_count):
    return (np.zeros(const.TIMESTEPS_NUMB,) for i in range(arrays_count))
    # return (np.zeros(const.TIMESTEPS_NUMB),) * arrays_count
