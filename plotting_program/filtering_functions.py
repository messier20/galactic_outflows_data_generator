import pandas as pd
import matplotlib.ticker as mticker

from data_generator.configurations.path_version_settings import params_path, values_version_folder
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot

params_output_name = params_path + values_version_folder

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.1e' % x))
fmt = mticker.FuncFormatter(g)

def filter_dataframe(filtered_df, fileting_criteria):
    legend_title = ''
    for param in fileting_criteria:
        # print(param)
        if "max" in param:
            filtered_df = filtered_df[(filtered_df[(param.replace('max', ''))] <= fileting_criteria[param])]
            print('max pass')
        elif "min" in param:
            filtered_df = filtered_df[(filtered_df[param.replace('min', '')] >= fileting_criteria[param])]
            print('min pass')
            print(fileting_criteria[param])
            legend_title += param + str(format(fileting_criteria[param], '.2f')) + '_'
            print(legend_title)

        else:
            try:
                print(fileting_criteria[param])
                filtered_df = filtered_df[(filtered_df[param] == fileting_criteria[param])]
                legend_title += param + str(fileting_criteria[param]) + '_'
            except:
                print('%s is not defined in filtering creteria' % param)

    # print(legend_title)
    return filtered_df, legend_title


def read_outflows(filtered_df, map_df, variable_parameter, galaxy_parameter=False):
    outflow_props = []
    labels = []
    legend_titles=[]
    print(outflow_props)
    # check if unique parameters to add labels and according to variable parameter
    nunique = filtered_df.nunique()
    print(nunique.galaxy_mass)
    non_unique_parameters =''
    for index in filtered_df.index:
        file_name = params_output_name + '_' + str(map_df.params_index.values[index]) + '_' + str(
                    map_df.galaxy_index.values[index]) + '_' + str(map_df.angle_index.values[index])+'.csv'
        outflow_props.append(pd.read_csv(file_name))
        variable_parameter_df = filtered_df[variable_parameter]
        param_value = str(format(variable_parameter_df[index], '.1e'))
        if galaxy_parameter or galaxy_parameter == 0:
            gal_indication = ', gal mass: ' + str(format(filtered_df.galaxy_mass[index], '.1e'))
        else:
            gal_indication = ''
        labels.append(variable_parameter + param_value + non_unique_parameters)
        # legend_titles.append(variable_parameter + param_value)
    return outflow_props, labels


def display_three_params_dependence(unique_galaxy_masses, map_df, filtering_criteria,
                                    unique_parameters_1=[False], unique_parameter_column_in_map_name=[False]):

    arr3 = []
    arr4 = []
    for galaxy_ident_index, galaxy_mass in enumerate(unique_galaxy_masses):
        filtered_df = map_df[map_df['galaxy_mass'] == galaxy_mass]
        filtered_df, file_title = filter_dataframe(filtered_df, filtering_criteria)
        arr1 = []
        arr2 = []
        if unique_parameters_1[0]:
            # for indication_index, unique_parameter in enumerate(unique_parameters_1):
                # filtered_df = filtered_df[filtered_df[unique_parameter_column_in_map_name] == unique_parameter]

            outflow_properties, labels = read_outflows(filtered_df, map_df, unique_parameter_column_in_map_name)

            generic_time_relation_plot(outflow_properties, labels,
                                       str(galaxy_ident_index) + unique_parameter_column_in_map_name +'-unique-' + file_title)
            generic_radius_relation_plot(outflow_properties, labels,
                                       str(galaxy_ident_index) + unique_parameter_column_in_map_name + '-unique-' + file_title)
        else:
            arr1, arr2 = read_outflows(filtered_df, map_df, arr1, unique_parameter_column_in_map_name, arr2, galaxy_ident_index)
            arr3.extend(arr1)
            arr4.extend(arr2)
    if not unique_parameters_1[0]:
    #     print('s')
        print(arr3)
        print(arr4)
        generic_time_relation_plot(arr3, arr4,
                                   '00' + variable_parameter + '-unique-' + file_title)
        generic_radius_relation_plot(arr3, arr4,
                                     '00' + variable_parameter + '-unique-' + file_title)


# Better to use this function for now
def display_three_params_dependence_for_specific_galaxy(map_df, filtering_criteria, unique_parameters_1,
                                                        unique_parameter_column_in_map_name):

    for galaxy_ident_index, unique_parameter in enumerate(unique_parameters_1):
        filtered_df = map_df[map_df[unique_parameter_column_in_map_name] == unique_parameter]
        param_value = " {key}".format(key=(fmt(unique_parameter)))
        # param_value = str(format(.index[0]]], '.1e'))
        legend_title = unique_parameter_column_in_map_name + param_value

        filtered_df, file_title = filter_dataframe(filtered_df, filtering_criteria)

        outflow_properties, labels = read_outflows(filtered_df, map_df, unique_parameter_column_in_map_name)

        generic_time_relation_plot(outflow_properties, labels, legend_title,
                                   str(galaxy_ident_index) + unique_parameter_column_in_map_name +'-unique-' + file_title)
        generic_radius_relation_plot(outflow_properties, labels, legend_title,
                                   str(galaxy_ident_index) + unique_parameter_column_in_map_name + '-unique-' + file_title)
        print(1)
