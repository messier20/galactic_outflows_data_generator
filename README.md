# Galactic outflows data generator

1D outflow simulation of active galactic nuclei.

# Running sample outflow

1. Install poetry for dependency management (read more [here](https://python-poetry.org/docs/#installation))

2. Install dependencies with:

```bash
poetry install
```

3. Run generation with:

```bash
poetry run python data_generator/run.py
```

This should output raw data in `./galactic_outflows_data_generator/data_generator/results/v13.0` and several illustrations in `./galactic_outflows_data_generator/data_generator/results/graphs`.
