import pandas as pd

import data_generator.configurations.constants as const
from data_generator.configurations.path_version_settings import params_path, values_version_folder
from plotting_program.filtering_functions import display_three_params_dependence, \
    display_three_params_dependence_for_specific_galaxy
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot
from plotting_program.turning_plots_on_off import display_galaxy_and_gas_dependence, display_gas_and_galaxy_dependence, \
    display_angle_dependence

params_output_name = params_path + values_version_folder
outflow_props = []

props_map = pd.read_csv(params_output_name+'properties_map.csv')
# failed_outflows = pd.read_csv(params_output_name+'failed_outflows.csv')

unique_galaxies = pd.unique(props_map['galaxy_mass'])
unique_duty_cycle = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value])
unique_gas_frac = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value])
unique_angle = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.OUTFLOW_SPHERE_ANGLE.value])

filtering_criteria_unique_galaxy = {'fade_type': const.FADE.NONE.value,
                                    # const.PROPERTIES_MAP_COLUMNS.OUTFLOW_SPHERE_ANGLE.value: 1,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'max': 0.1,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'min': 0.03,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'max': 1.e4,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'min': 5.e3,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'max': 0.2,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'min': 0.04
                                    }

filtering_criteria_unique_gas = {'fade_type': const.FADE.NONE.value, const.PROPERTIES_MAP_COLUMNS.OUTFLOW_SPHERE_ANGLE.value: 1,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'max': 0.6,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'min': 0.03,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'max': 9e4,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'min': 5.e3,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'max': 1.6e13,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'min': 1.0e13
                                    }
filtering_criteria_unique_angle = {'fade_type': const.FADE.NONE.value,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'max': 0.1,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'min': 0.03,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'max': 1.e4,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'min': 5.e3,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'max': 1.54e13,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'min': 1.0e13,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'max': 0.2,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'min': 0.04
                                    }

filtering_criteria_unique_duty_cycle = {'fade_type': const.FADE.NONE}
variable_gas_unique_galaxy = const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value
# print(filtering_criteria_unique_galaxy[0])
# display_three_params_dependence(unique_galaxies, variable_gas_unique_galaxy, props_map, filtering_criteria_unique_galaxy)

# display_three_params_dependence(unique_galaxies, props_map,
#                                 filtering_criteria_unique_gas, unique_gas_frac, const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value)

if display_gas_and_galaxy_dependence:
    display_three_params_dependence_for_specific_galaxy(props_map, filtering_criteria_unique_gas, unique_gas_frac,
                                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value)

if display_galaxy_and_gas_dependence:
    display_three_params_dependence_for_specific_galaxy(props_map, filtering_criteria_unique_galaxy, unique_galaxies,
                                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value)

if display_angle_dependence:
    display_three_params_dependence_for_specific_galaxy(props_map, filtering_criteria_unique_angle, unique_angle,
                                                        const.PROPERTIES_MAP_COLUMNS.OUTFLOW_SPHERE_ANGLE.value)

file_name = params_output_name + '_' + str(props_map.params_index.values[0]) + '_' + str(
                    props_map.galaxy_index.values[0]) +'.csv'
# file_name = params_output_name + '_' + str(props_map.params_index.values[0]) + '_' + str(
                    # props_map.galaxy_index.values[0]) + '_' + str(props_map.angle_index.values[2])+'.csv'
outflow_props.append(pd.read_csv(file_name))

generic_time_relation_plot(outflow_props, '0', 'legend_title', 'test')
