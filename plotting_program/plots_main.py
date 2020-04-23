import pandas as pd

from data_generator.configurations.path_version_settings import params_path, values_version_folder
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot

params_output_name = params_path + values_version_folder
outflow_props = []

galaxy_props_map = pd.read_csv(params_output_name+'properties_map.csv')
# print(galaxy_props_map)
unique_bulge_masses = pd.unique(galaxy_props_map['bulge_mass'])
# unique_bulge_masses =galaxy_props_map.groupby(['bulge_mass'])
# print(unique_bulge_masses)
unique_bulge_gas_fractions = pd.unique(galaxy_props_map.bulge_gas_frac)
# same_bulge_gas_fractions_df = galaxy_props_map[galaxy_props_map.bulge_gas_frac == unique_bulge_gas_fractions]
# print(same_bulge_gas_fractions_df)
for indication_index, gas_fraction in enumerate(unique_bulge_gas_fractions):
    same_bulge_gas_fraction_df = galaxy_props_map[galaxy_props_map.bulge_gas_frac == gas_fraction]
    # print(same_bulge_gas_fraction_df)
    outflow_props = []

    for index in same_bulge_gas_fraction_df.index:
        file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
        outflow_props.append(pd.read_csv(file_name))
    generic_time_relation_plot(outflow_props, str(indication_index) + '-same-gasf')
    generic_radius_relation_plot(outflow_props, str(indication_index) + '-same-gasf')

for indication_index, bulge_mass in enumerate(unique_bulge_masses):
    same_bulge_masses = galaxy_props_map[galaxy_props_map.bulge_mass == bulge_mass]
    # filtered_props = same_bulge_masses[same_bulge_masses.bulge_gas_frac >=0.5]
    outflow_props = []

    for index in same_bulge_masses.index:
        file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
        outflow_props.append(pd.read_csv(file_name))
    generic_time_relation_plot(outflow_props, indication=str(indication_index) + '-same-bulgemass')
    generic_radius_relation_plot(outflow_props, indication=str(indication_index) + '-same-bulgemass')

