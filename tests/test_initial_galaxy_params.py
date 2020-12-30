import pytest
import numpy as np

import data_generator.configurations.initial_galaxy_params as init


@pytest.mark.parametrize(
    "rng, expected_bulge_mass",
    [
        (None, 19126721261),
        (np.random.RandomState(0), 36708148026),
        (np.random.RandomState(42), 50252088092),
    ],
)
def test_bulge_mass(rng, expected_bulge_mass):
    initial_galaxy_parameters = init.InitialGalaxyParameters()
    if rng:
        initial_galaxy_parameters.generate_stochastic_parameters(rng)

    assert initial_galaxy_parameters.bulge_mass == pytest.approx(expected_bulge_mass)
