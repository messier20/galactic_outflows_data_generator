import pandas as pd

from data_generator.configurations.path_version_settings import params_path, values_version_folder
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot

params_output_name = params_path + values_version_folder
outflow_props = []

galaxy_props_map = pd.read_csv(params_output_name+'properties_map.csv')
# print(galaxy_props_map)
unique_bulge_masses = pd.unique(galaxy_props_map['bulge_mass'])
# unique_bulge_masses =galaxy_props_map.groupby(['bulge_mass'])
# print(unique_bulge_masses)
for bulge_mass in unique_bulge_masses:
    same_bulge_masses = galaxy_props_map[galaxy_props_map.bulge_mass == bulge_mass]
    # filtered_props = same_bulge_masses[same_bulge_masses.bulge_gas_frac >=0.5]
    outflow_props = []

    for index in same_bulge_masses.index:
        file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
        outflow_props.append(pd.read_csv(file_name))
    generic_time_relation_plot(outflow_props)
