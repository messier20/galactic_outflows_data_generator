import numpy as np
import pandas as pd

import data_generator.configurations.initial_galaxy_params as init
from data_generator.simulation import run_outflow_simulation


def test_simulation_default_params():
    initial_galaxy_parameters = init.InitialGalaxyParameters()
    rng = np.random.RandomState(0)
    initial_galaxy_parameters.generate_stochastic_parameters(rng)

    outflow_properties = run_outflow_simulation(initial_galaxy_parameters)
    expected_outflow_properties = pd.read_csv(
        "tests/data/outflow_properties_default_params.csv"
    )

    pd.testing.assert_frame_equal(
        outflow_properties, expected_outflow_properties
    )
