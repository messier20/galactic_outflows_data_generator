import os
import time

import numpy as np

import data_generator.configurations.constants as const
import data_generator.configurations.initial_galaxy_params as init
from data_generator.configurations.path_version_settings import params_path, values_version_folder
from data_generator.simulation import run_outflow_simulation

if __name__ == '__main__':
    start_time = time.time()
    
    initial_galaxy_parameters = init.InitialGalaxyParameters()

    rng = np.random.RandomState(0)
    initial_galaxy_parameters.generate_stochastic_parameters(rng)

    initial_galaxy_parameters.to_dataframe().to_csv(
        os.path.join(params_path, values_version_folder, "initial_galaxy_parameters.csv"),
        index=False,
        encoding="utf-8"
    )

    # If Quasars are active longers - increase upper bound of time step, because we won't be missing much
    if initial_galaxy_parameters.duty_cycle < 0.07:
        dtmax = const.DT_MAX_VERY_SMALL_OUTFLOWS
    elif initial_galaxy_parameters.duty_cycle < 0.15:
        dtmax = const.DT_MAX_SMALL_OUTFLOWS
    elif initial_galaxy_parameters.duty_cycle < 0.26:
        dtmax = const.DT_MAX_INTERMEDIATE_OUTFLOWS
    else:
        dtmax = const.DT_MAX_BIG_OUTFLOWS
    outflow_properties = run_outflow_simulation(initial_galaxy_parameters, dtmax=dtmax)

    outflow_properties.to_csv(
        os.path.join(params_path, values_version_folder, "outflow_properties.csv"),
        index=False,
        encoding="utf-8"
    )

    print('passed time', time.time() - start_time)
