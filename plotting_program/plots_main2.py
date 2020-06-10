import pandas as pd
import matplotlib.pyplot as plt

from data_generator.configurations.physical_values import intercept_alpha, slope_beta, bulge_normalization_mass
from plotting_program.plots.PlotSetup import PlotSetup
import numpy as np
import data_generator.configurations.constants as const
from data_generator.configurations.path_version_settings import params_path, values_version_folder, predictions_file, \
    version
from plotting_program.plots import smbh_relations
from plotting_program.filtering_functions import \
    display_three_params_dependence_for_specific_galaxy, display_chi_squared, display_all_predictions, \
    display_special_outflows, display_predictions_hists
from plotting_program.plots.generic_lum_relation import generic_lum_relation
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot
from plotting_program.turning_plots_on_off import *

params_output_name = params_path + values_version_folder
outflow_props = []
real_data = pd.read_csv(params_path + 'real_outflows_3.csv')

props_map = pd.read_csv(params_output_name+'properties_map.csv')
# failed_outflows = pd.read_csv(params_output_name+'failed_outflows.csv')

reduced_predictions = pd.read_csv(params_path+'/predictions/ep75_predictions_droped.csv')

unique_galaxies = pd.unique(props_map['galaxy_mass'])
min_max_galaxies1 = props_map[props_map.galaxy_mass == props_map.galaxy_mass.max()]
min_max_galaxies2 = props_map[props_map.galaxy_mass == props_map.galaxy_mass.min()]
min_max_galaxies = min_max_galaxies1.append(min_max_galaxies2)
min_max_gal_unique = pd.unique(min_max_galaxies['galaxy_mass'])

mtot13_df =props_map[(props_map.galaxy_mass < 1.18e13) & (props_map.galaxy_mass > 1.0000e13)]
print(mtot13_df)
mtot13_df_unique = pd.unique(mtot13_df['galaxy_mass'])


unique_duty_cycle = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value])
unique_gas_frac = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value])
unique_angle = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.OUTFLOW_SPHERE_ANGLE.value])
unique_fade_type = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.FADE_TYPE.value])
try :
    unique_name = pd.unique(props_map[const.PROPERTIES_MAP_COLUMNS.NAME.value])
except:
    pass
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

filtering_criteria_chi_squared = {'fade_type': const.FADE.NONE.value,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'max': 0.1,
                                    const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value + 'min': 0.03,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'max': 1.e4,
                                    const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value + 'min': 5.e3,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'max': 1.54e13,
                                    const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value + 'min': 1.0e13,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'max': 0.2,
                                    const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value + 'min': 0.04
                                    }
filtering_criteria_real_outf = {}


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
if display_fade_type_dependence_for_real_outf:
    display_all_predictions(props_map, unique_fade_type, const.PROPERTIES_MAP_COLUMNS.FADE_TYPE.value, real_data,
            const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value, const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value)

if display_predictions:
    display_all_predictions(props_map, unique_name, const.PROPERTIES_MAP_COLUMNS.NAME.value, real_data,
            const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value, const.PROPERTIES_MAP_COLUMNS.FADE_TYPE.value)

if display_smbh_relations:
    # smbh_relations(props_map)
    smbh_mass = []
    bulge_mass = []
    mtot_mass = []
    plot = PlotSetup()

    fig1, ax1 = plot.setup_common_properties()
    # for par_index in range(props_map.params_index.max() + 1):
    #     for gal_ind in range(props_map.galaxy_index.max() + 1):
    #         file_name = params_output_name + '_' + str(props_map.params_index.values[par_index - 1]) + '_' + str(
    #             props_map.galaxy_index.values[gal_ind - 1]) + '.csv'
    #         outflow = pd.read_csv(file_name)
    #         smbh_mass.append(outflow.smbh_mass)
    #         bulge_mass.append(outflow.bulge_mass)
    #         mtot_mass.append(outflow.galaxy_mass)
    bul = np.logspace(8, 15, 1000)
    mtot = np.logspace(11, 15, 1000)
    smbh = np.logspace(5, 12, 1000)
    # intercept_alpha, slope_beta, bulge_normalization_mass
    theor_bulge_mass_log = (np.log10(smbh) - intercept_alpha) / slope_beta
    theor_bulge_mass = (10 ** theor_bulge_mass_log) * bulge_normalization_mass

    theor_smbh_mass_log = 8.18 + (1.57 * (np.log10(mtot) - 13.0))
    theor_smbh_mass = 10 ** theor_smbh_mass_log

    ax1.set_xlabel('Baldžo masė [$M_{\odot}$]', fontsize=14)
    ax1.set_ylabel('SMBH masė [$M_{\odot}$]', fontsize=14)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim(1e8, 1e14)
    ax1.set_ylim(3e6, 3e10)
    ax1.plot(theor_bulge_mass, smbh, '--', color='black')
    ax1.scatter(props_map.bulge_mass.values, props_map.smbh_mass.values, s=20)
    fig1.savefig('bulge-smbh2' + str(version) + '.png')
    plt.legend()
    # plt.show()
    plt.close(fig1)

    fig1, ax1 = plot.setup_common_properties()

    ax1.set_xlabel('Virialinė galaktikos masė [$M_{\odot}$]', fontsize=14)
    ax1.set_ylabel('SMBH masė [$M_{\odot}$]', fontsize=14)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim(3e11, 4e14)
    ax1.set_ylim(3e6, 3e10)
    ax1.plot(mtot, theor_smbh_mass, '--', color='black')
    ax1.scatter(props_map.galaxy_mass.values, props_map.smbh_mass.values, s=20)
    # plt.show()
    fig1.savefig('smbh-mtot2' + str(version) + '.png')
    plt.close()

if display_specific_outflows:
    # display_special_outflows(props_map, min_max_gal_unique)
    display_special_outflows(props_map, mtot13_df_unique)

# display_predictions_hists(props_map, unique_galaxies, reduced_predictions)


# display_chi_squared(props_map, filtering_criteria_chi_squared)

# file_name = params_output_name + '_' + str(props_map.params_index.values[0]) + '_' + str(
#                     props_map.galaxy_index.values[0]) +'.csv'

# file_name2= params_output_name + '_' + str(props_map.params_index.values[2]) + '_' + str(
#                     props_map.galaxy_index.values[0]) +'.csv'
#
# file_name3= params_output_name + '_' + str(props_map.params_index.values[20]) + '_' + str(
#                     props_map.galaxy_index.values[0]) +'.csv'
#
# outflow_props.append(pd.read_csv(file_name))
# outflow_props.append(pd.read_csv(file_name2))
# outflow_props.append(pd.read_csv(file_name3))
#
# generic_time_relation_plot(outflow_props, '0', 'legend_title', 'test')
# generic_lum_relation(outflow_props, '0', 'legend_title', 'test')
