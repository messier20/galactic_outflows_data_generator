import pandas as pd
import matplotlib.ticker as mticker
import warnings
import matplotlib.pyplot as plt

from plotting_program.plots.PlotSetup import PlotSetup
from plotting_program.plots.generic_lum_relation import generic_lum_relation
from plotting_program.plots.plots_settings import graphs_path, plots_version_folder
from plotting_program.plots.subfigure_plt import subfigure_plt
from plotting_program.turning_plots_on_off import *

warnings.filterwarnings('error')

import numpy as np
import data_generator.configurations.constants as const
from data_generator.configurations.path_version_settings import params_path, values_version_folder
from data_generator.configurations.units import unit_sunmass
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot

params_output_name = params_path + values_version_folder

f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.1e' % x))
fmt = mticker.FuncFormatter(g)

cols = {'galaxy_mass': '$M_{tot}=$', 'duty_cycle': '$\delta_{AGN}=$', 'bulge_gas_frac': '$f_g=$', 'quasar_duration': '$t_q=$',
        'fade_type':'', 'smbh_mass': '$M_{BH}=$', 'bulge_mass': '$M_{bulge}=$'}

def filter_dataframe(filtered_df, fileting_criteria):
    file_title = ''
    for param in fileting_criteria:
        # print(param)
        if "max" in param:
            filtered_df = filtered_df[(filtered_df[(param.replace('max', ''))] <= fileting_criteria[param])]
            print('max pass')
        elif "min" in param:
            filtered_df = filtered_df[(filtered_df[param.replace('min', '')] >= fileting_criteria[param])]
            print('min pass')
            file_title += param + str(format(fileting_criteria[param], '.2f')) + '_'

        else:
            try:
                filtered_df = filtered_df[(filtered_df[param] == fileting_criteria[param])]
                file_title += param + str(fileting_criteria[param]) + '_'
            except:
                print('%s is not defined in filtering creteria' % param)

    # print(legend_title)
    return filtered_df, file_title


def read_outflows(filtered_df, map_df, variable_parameter, outflow_props, labels, colors_flag=False, *column_labels):
    # outflow_props = []
    # labels = []
    legend_titles=[]
    for spe, index in enumerate(filtered_df.index):
        file_name = params_output_name + '_' + str(map_df.params_index.values[index]) + '_' + str(
                    map_df.variant_loop_index.values[index]) +'.csv'
        # file_name = params_output_name + '_' + str(map_df.params_index.values[index]) + '_' + str(
        #     map_df.galaxy_index.values[index]) + '.csv'
        outflow = pd.read_csv(file_name)
        if colors_flag:
            outflow['color'] = [filtered_df.color[index] for j in range(len(outflow))]
        outflow_props.append(outflow)
        # variable_parameter_df = filtered_df[variable_parameter]
        # fade_type_val = filtered_df.fade_type[index]
        # param_value = str(format(variable_parameter_df[index], '.1e'))
        # param_value = " {key}".format(key=(fmt(unique_parameter)))
        # if galaxy_parameter or galaxy_parameter == 0:
        #     gal_indication = ', gal mass: ' + str(format(filtered_df.galaxy_mass[index], '.1e'))
        # else:
        #     gal_indication = ''
        add_val=''

        if column_labels:
            ls = ''
            for ind, column_label in enumerate(column_labels):
                print(column_label)
                val = filtered_df[column_label]
                if not isinstance(val[index], str):
                    param_value = " {key}".format(key=(fmt(val[index])))
                    print(cols[column_label])
                    # print(cols[column_label].value)
                    if len(column_labels) > 3 and ind ==2:
                        add_val = '\n'
                    ls += ', '+add_val + str(cols[column_label]) + param_value
                else:
                    if len(column_labels) > 3 and ind ==2:
                        add_val ='\n'
                    ls += ', '+ add_val + filtered_df.fade_type[index]
                add_val = ''

            labels.append(ls[2:])
        # labels.append(variable_parameter + param_value + non_unique_parameters +', '+ fade_type_val)
        # legend_titles.append(variable_parameter + param_value)
    return outflow_props, labels


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


def display_all_in_one_graph(map_df, filtering_criteria, unique_parameters_1, unique_parameter_column_in_map_name):
    for galaxy_ident_index, unique_parameter in enumerate(unique_parameters_1):
        filtered_df = map_df[map_df[unique_parameter_column_in_map_name] == unique_parameter]

        # param_value = " {key}".format(key=(fmt(unique_parameter)))

        # param_value = str(format(.index[0]]], '.1e'))
        legend_title = unique_parameter_column_in_map_name
        # legend_title = unique_parameter_column_in_map_name + param_value

        # filtered_df, file_title = filter_dataframe(filtered_df, filtering_criteria)

        outflow_properties, labels = read_outflows(filtered_df, map_df, unique_parameter_column_in_map_name)

    generic_time_relation_plot(outflow_properties, labels, legend_title,
                           str(galaxy_ident_index) + unique_parameter_column_in_map_name +'-all-' + 'tekme1')
    generic_radius_relation_plot(outflow_properties, labels, legend_title,
                               str(galaxy_ident_index) + unique_parameter_column_in_map_name + '-all-' + 'tekme1')
    print(1)


def display_all_predictions(map_df, unique_parameters_1, unique_parameter_column_in_map_name, real_data=False, *additionl_legend_labels):
    colors = plt.cm.hsv(np.linspace(0, 1, len(unique_parameters_1)*4))
    indices = np.arange(len(colors))
    rng = np.random.RandomState(1)
    rng.shuffle(indices)
    count_filtered_data = 0

    for galaxy_ident_index, unique_parameter in enumerate(unique_parameters_1):
        filtered_df = map_df[map_df[unique_parameter_column_in_map_name] == unique_parameter]
        outflow_real_data = []
        outflow_properties =[]
        labels=[]
        if not isinstance(unique_parameter, str):
            param_value = " {key}".format(key=(fmt(unique_parameter)))
            legend_title = unique_parameter_column_in_map_name + param_value
        else:
            legend_title = unique_parameter

        if not isinstance(real_data, bool):
            if unique_parameter_column_in_map_name != 'name':
                for out_name in filtered_df.name:
                    print(out_name)
                    outflow_real_data.append(real_data[real_data.name == out_name])
            else:
                outflow_real_data.append(real_data[real_data.name == unique_parameter])

        color_len = len(real_data)+len(outflow_properties)
        count_filtered_data1 = count_filtered_data
        count_filtered_data += len(filtered_df)

        temp_ind = indices[count_filtered_data1:count_filtered_data]
        arr = [colors[temp_ind[j]] for j in range(len(filtered_df))]
        a = np.array(arr)
        filtered_df.insert(2, "color", arr, True)

        outflow_properties, labels = read_outflows(filtered_df, map_df, unique_parameter_column_in_map_name, outflow_properties,
                                                   labels, False, *additionl_legend_labels)

        generic_time_relation_plot(outflow_properties, labels, legend_title,
                               str(galaxy_ident_index) + unique_parameter_column_in_map_name +'-all-' + 'tekme1', False, 5, False)
        generic_radius_relation_plot(outflow_properties, labels, legend_title,
                               str(galaxy_ident_index) + unique_parameter_column_in_map_name + '-all-' + 'tekme1', outflow_real_data, 5, False)

        generic_lum_relation(outflow_properties, labels, legend_title,
                             str(galaxy_ident_index) + unique_parameter_column_in_map_name + '-all-' + 'tekme1', outflow_real_data, 5, False)

        subfigure_plt(outflow_properties, labels, legend_title, str(galaxy_ident_index) +
                      unique_parameter_column_in_map_name + '-all-' + 'tekme2', outflow_real_data, 5, False, True)




def display_special_outflows(map_df, unique_galaxies):
    outflows = []
    labels = []
    outflow_real_data = []
    count_filtered_data = 0
    fade_count = 15
    full_needed_df = []
    colors = plt.cm.tab20(np.linspace(0, 1, 16 + 12))
    indices = np.arange(len(colors))
    rng = np.random.RandomState(0)
    rng.shuffle(indices)
    for galaxy_ident_index, unique_parameter in enumerate(unique_galaxies):
        filtered_df = map_df[(map_df.galaxy_mass == unique_parameter) & (map_df.outflow_sphare_angle==1)]
        df_with_duty_cycle = filter_min_max(filtered_df, [const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value,
                                     const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value])
        filtered = filter_min_max(filtered_df, [const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value, const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value,
                                     const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value])
        df_only_king = filtered[filtered.fade_type == 'king']

        df_with_duty_cycle_king = df_with_duty_cycle[df_with_duty_cycle.fade_type == 'king']


        count_filtered_data1 = count_filtered_data
        count_filtered_data += len(df_only_king)


        prefered_labels = const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value, const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value, \
                          const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value, const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value
        temp_ind = indices[count_filtered_data1:count_filtered_data]
        arr = [colors[temp_ind[j]] for j in range(len(df_only_king))]
        a = np.array(arr)
        df_only_king.insert(2, "color", arr, True)

        leave_galaxy_fade_small = filtered[(filtered.bulge_gas_frac<0.05)&(filtered.quasar_duration<1e4) &(filtered.duty_cycle>0.1)&
                                           (filtered.galaxy_mass<5e12)
        ]
        leave_only_duty_cycle_range_small = df_with_duty_cycle_king[
            (df_with_duty_cycle_king.bulge_gas_frac < 0.05) & (df_with_duty_cycle_king.quasar_duration < 1e4)
            ]

        # leave_only_duty_cycle_range_small = df_with_duty_cycle_king[
        #     (df_with_duty_cycle_king.bulge_gas_frac < 0.05) & (df_with_duty_cycle_king.quasar_duration < 1e4) &
        #     (df_with_duty_cycle_king.galaxy_mass < 5e12)
        #     ]
        leave_only_duty_cycle_range_big_mass = df_with_duty_cycle_king[
            (df_with_duty_cycle_king.bulge_gas_frac < 0.05) & (df_with_duty_cycle_king.quasar_duration < 1e4) &
            (df_with_duty_cycle_king.galaxy_mass > 5e12)
            ]

        fade_count1 = fade_count
        fade_count += len(leave_galaxy_fade_small)
        temp_ind2 = indices[fade_count1:fade_count]
        # arr2 =[]
        # for j in range(16, 16+len(leave_galaxy_fade_small)):
        #     b = temp_ind2[j]
        #
        #     arr2.append(colors[b])
        arr2 = [colors[temp_ind2[j]] for j in range(len(leave_galaxy_fade_small))]
        leave_galaxy_fade_small.insert(2, 'color', arr2, True)

        leave_only_duty_df = df_only_king[
            # (df_only_king.quasar_duration < 1e4) &
                                          (df_only_king.bulge_gas_frac<0.05)
                                            &(df_only_king.galaxy_mass < 5e13)]

        leave_galax_quasar = df_only_king[
            (df_only_king.duty_cycle < 0.06) &
            (df_only_king.bulge_gas_frac < 0.05)
            # & (df_only_king.galaxy_mass < 5e13)
        ]
        leave_galax_duty = df_only_king[
            # (df_only_king.duty_cycle < 0.06) &
            (df_only_king.bulge_gas_frac < 0.05)&
            (df_only_king.quasar_duration < 1e4)
            # & (df_only_king.galaxy_mass < 5e13)
            ]
        leave_galax_gas = df_only_king[
            (df_only_king.duty_cycle < 0.06) &
            # (df_only_king.bulge_gas_frac < 0.05) &
            (df_only_king.quasar_duration < 1e4)
            # & (df_only_king.galaxy_mass < 5e13)
            ]

        leave_galax_gas_big = df_only_king[
            (df_only_king.duty_cycle > 0.06) &
            # (df_only_king.bulge_gas_frac < 0.05) &
            (df_only_king.quasar_duration > 1e4)
            # & (df_only_king.galaxy_mass < 5e13)
            ]
        leave_duty_gas = df_only_king[
            # (df_only_king.duty_cycle > 0.06) &
            # (df_only_king.bulge_gas_frac < 0.05) &
            (df_only_king.quasar_duration <1e4)
            & (df_only_king.galaxy_mass < 5e13)
            ]

        leave_duty_gas_big = df_only_king[
            # (df_only_king.duty_cycle > 0.06) &
            # (df_only_king.bulge_gas_frac < 0.05) &
            (df_only_king.quasar_duration > 1e4)
            & (df_only_king.galaxy_mass > 5e13)
            ]
        leave_duty_gas_semibig = df_only_king[
            # (df_only_king.duty_cycle > 0.06) &
            # (df_only_king.bulge_gas_frac < 0.05) &
            (df_only_king.quasar_duration < 1e4)
            & (df_only_king.galaxy_mass > 5e13)
            ]
        prefered_labels2 = const.PROPERTIES_MAP_COLUMNS.FADE_TYPE.value, const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value, const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value, \
                          const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value, const.PROPERTIES_MAP_COLUMNS.QUASAR_DURATION.value

        if display_fades_small:
            outflows, labels = read_outflows(leave_galaxy_fade_small, map_df, unique_galaxies, outflows, labels, True,
                                             const.PROPERTIES_MAP_COLUMNS.FADE_TYPE.value)

        if display_duty_gas_semi_big:
            outflows, labels = read_outflows(leave_duty_gas_semibig, map_df, unique_galaxies, outflows, labels, True,
                                             *prefered_labels)
        if display_duty_gas_big:
            outflows, labels = read_outflows(leave_duty_gas_big, map_df, unique_galaxies, outflows, labels, True,
                                             *prefered_labels)

        if display_duty_gas:
            outflows, labels = read_outflows(leave_duty_gas, map_df, unique_galaxies, outflows, labels, True,
                                         *prefered_labels)

        if display_galaxy_gas:
            outflows, labels = read_outflows(leave_galax_gas, map_df, unique_galaxies, outflows, labels, True,*prefered_labels)
        if display_gal_gas_big:
            outflows, labels = read_outflows(leave_galax_gas_big, map_df, unique_galaxies, outflows, labels, True,*prefered_labels)

        if display_galaxy_duty:
            outflows, labels = read_outflows(leave_galax_duty, map_df, unique_galaxies, outflows, labels, True, *prefered_labels)

        if display_galaxy_quasar:
            outflows, labels = read_outflows(leave_galax_quasar, map_df, unique_galaxies, outflows, labels, True,
                                         *prefered_labels)

        if display_duty_cycle_quasar:
            outflows, labels = read_outflows(leave_only_duty_df, map_df, unique_galaxies, outflows, labels, True, *prefered_labels)
        if display_characteristic:
            outflows, labels = read_outflows(df_only_king, map_df, unique_galaxies, outflows, labels, True, *prefered_labels)

        if display_special_duty_cycle_range_small:
            outflows, labels = read_outflows(leave_only_duty_cycle_range_small, map_df, unique_galaxies, outflows, labels, False,
                                             # const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value,
                                             # const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value,
                                             # const.PROPERTIES_MAP_COLUMNS.SMBH_MASS.value,
                                             const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value)

        if display_special_duty_cycle_range_big:
            outflows, labels = read_outflows(leave_only_duty_cycle_range_big_mass, map_df, unique_galaxies, outflows,
                                             labels, False,
                                             # const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value,
                                             # const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value,
                                             # const.PROPERTIES_MAP_COLUMNS.SMBH_MASS.value,
                                             const.PROPERTIES_MAP_COLUMNS.DUTY_CYCLE.value)

        if display_gal_gas_big_sub:
            outflows, labels = read_outflows(leave_galax_gas_big, map_df, unique_galaxies, outflows, labels, True,
                                             const.PROPERTIES_MAP_COLUMNS.GALAXY_MASS.value,
                                             const.PROPERTIES_MAP_COLUMNS.BULGE_GAS_FRAC.value, const.PROPERTIES_MAP_COLUMNS.SMBH_MASS.value,
                                             const.PROPERTIES_MAP_COLUMNS.BULGE_MASS.value)

    if display_characteristic:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'all', False, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'all', False, colors[indices], True)

    if display_duty_cycle_quasar:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty+quasar-d1', False, colors[indices], True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty+quasar-d1', False, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'duty+quasar-d1', False, colors[indices], True)

    if display_galaxy_quasar:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-quasar-dt', False, colors[indices], True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-quasar-dt', False, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'gal-mass-quasar-dt', False, colors[indices], True)

    if display_galaxy_duty:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-duty', False, colors[indices], True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-duty', False, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'gal-mass-duty', False, colors[indices], True)

    if display_galaxy_gas:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas', False, colors[indices], True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas', False, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas', False, colors[indices], True)

    if display_gal_gas_big:

        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas-big', False, 0, display_special_duty_cycle_range_big[indices],
                                     True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas-big', False, 0, colors[indices], True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas-big', False, 0, colors[indices], True)

    if display_duty_gas:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas', False, colors[indices],
                                     True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas', False, colors[indices],
                                   True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'duty-gas', False, colors[indices], True)

    if display_duty_gas_big:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas-big', False, 0, colors[indices],
                                     True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas-big', False, 0, colors[indices],
                                   True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'duty-gas-big', False, 0, colors[indices], True)
    if display_duty_gas_semi_big:
        generic_radius_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas-semi-big', False, colors[indices],
                                     True)
        generic_time_relation_plot(outflows, labels, 'king šviesio funkcija', 'duty-gas-semi-big', False, colors[indices],
                                   True)
        generic_lum_relation(outflows, labels, 'king šviesio funkcija', 'duty-gas-semi-big', False, colors[indices], True)
    if display_fades_small:
        generic_radius_relation_plot(outflows, labels, '', 'galaxy-fade-3', False, 12,
                                     colors[indices],
                                     True)
        generic_time_relation_plot(outflows, labels, '', 'galaxy-fade-3', False, 12,
                                   colors[indices],
                                   True)
        generic_lum_relation(outflows, labels, '', 'galaxy-fade-3', False, 12, colors[indices],
                             True)
    if display_special_duty_cycle_range_small:
        gal_mass = leave_only_duty_cycle_range_small.galaxy_mass.values
        title = '$M_{tot}=$' +" {key}".format(key=(fmt(gal_mass[0]))) + "$M_{\odot}$"
        generic_radius_relation_plot(outflows, labels, title, 'spec-duty-small', False, 4,False,True)
        generic_time_relation_plot(outflows, labels, title, 'spec-duty-small', False, 4,
                                   False,
                                   True)
        generic_lum_relation(outflows, labels, title, 'spec-duty-small', False, 4, False,
                             True)
    if display_special_duty_cycle_range_big:
        # gal_mass = leave_only_duty_cycle_range_big_mass.galaxy_mass.values
        # qd = leave_only_duty_cycle_range_big_mass.quasar_duration.values
        # title = '$M_{tot}=$' + " {key}".format(key=(fmt(unique_parameter))) + "$M_{\odot}$, $t_{d}=$"+\
        #         " {key}".format(key=(fmt(qd[0]))) + " yr"/
        generic_radius_relation_plot(outflows, labels, '', 'spec-duty-big4', False, 8, False, True)
        generic_time_relation_plot(outflows, labels, '', 'spec-duty-big4', False, 8,
                                   False,
                                   True)
        generic_lum_relation(outflows, labels, '', 'spec-duty-big4', False, 8, False,
                             True)

    if display_gal_gas_big_sub:
        subfigure_plt(outflows, labels, 'king šviesio funkcija', 'gal-mass-gas-big2', False, 0, colors[indices],
                                     True)
    # generic_lum_relation(outflows, labels, '', 'gal-mass-gas-big2', False, 0, colors[indices],
    #                      True)
    # generic_time_relation_plot(outflows, labels, '', 'galaxy-fade-2', False, 0,
    #                            colors[indices],
    #                            True)



    print(filtered)


def display_predictions_hists(props_map, unique_galaxies, reduced_predictions):

    if display_duty_cycle_hist:
        Plot = PlotSetup()
        #
        fig1, ax1 = Plot.setup_common_properties()
        ax1.set_xlabel('Laiko dalis aktyvioje fazėje, $\delta_{AGN}$', fontsize=14)
        ax1.set_ylabel('Kiekis', fontsize=14)
        bins = np.linspace(0, 0.42, 10, endpoint=False)
        plt.hist(reduced_predictions.duty_cycle, bins=bins, histtype='bar', alpha=0.7, rwidth=0.85)
        ax1.grid(axis='y', alpha=0.75)
        # plt.xticks(range(0.4))
        ax1.set_xticks(np.arange(0, 0.42, step=0.05))
        ax1.set_xlim(0, 0.41)
        plt.savefig(graphs_path + plots_version_folder +'duty-cycle-hist2.png')
        plt.show()

    if display_quasar_duration_hist:
        Plot = PlotSetup()
        #
        fig1, ax1 = Plot.setup_common_properties()
        bins = np.logspace(3., 5, 20)
        plt.hist(reduced_predictions.quasar_duration, bins=bins, histtype='bar', alpha=0.7, rwidth=0.85)
        ax1.grid(axis='y', alpha=0.75)
        ax1.set_xlabel('Aktyvumo epizodo trukmė, $t_{q}$', fontsize=14)
        ax1.set_ylabel('Kiekis', fontsize=14)

        ax1.set_xscale('log')
        # plt.xticks(labels=np.arange(0, 2e5, step=0.5e4))
        ax1.set_xlim(2e3, 1.1e5)
        plt.savefig(graphs_path + plots_version_folder +'quasar-duration-hist.png')
        # plt.show()

    if display_outf_angle_hist:
        Plot = PlotSetup()
        #
        fig1, ax1 = Plot.setup_common_properties()
        ax1.set_xlabel('Tėkmės erdvinio kampo dalis, $f_{\\alpha}$', fontsize=14)
        ax1.set_ylabel('Kiekis', fontsize=14)
        bins = np.linspace(0, 1, 20, endpoint=False)
        # plt.hist(reduced_predictions.outflow_angle)
        plt.hist(reduced_predictions.outflow_angle, bins=bins, histtype='bar', alpha=0.7, rwidth=0.85)
        ax1.grid(axis='y', alpha=0.75)
        # plt.xticks(range(0.4))
        # plt.xticks(np.arange(0, 0.42, step=0.04))
        # plt.xlim(0, 0.41)
        plt.savefig(graphs_path + plots_version_folder + 'outflow-angle-hist.png')
        # plt.show()

    if display_gas_frac_hist:
        Plot = PlotSetup()
        #
        fig1, ax1 = Plot.setup_common_properties()

        ax1.set_xlabel('Dujų dalis baldže, $f_{g}$', fontsize=14)
        ax1.set_ylabel('Kiekis', fontsize=14)
        ax1.set_xscale('log')
        bins = np.logspace(-3, 0.5, 20, endpoint=False)

        # plt.hist(reduced_predictions.outflow_angle)
        ax1.hist(reduced_predictions.bulge_gas_frac, bins=bins, histtype='bar', alpha=0.7, rwidth=0.85)
        ax1.grid(axis='y', alpha=0.75)
        # plt.xticks(range(0.4))
        # ax1.set_xticks(np.arange(0, 0.8, step=0.08))
        plt.xlim(3.e-3, 1.e0)
        plt.savefig(graphs_path + plots_version_folder + 'bulge-gas-hist2.png')
        # plt.show()



def filter_min_max(df, filer_props):
    for prop in filer_props:
        dt_max = df[prop].max()
        dt_min = df[prop].min()
        filtered_df1 = df[(df[prop] == dt_max)]
        filtered_df2 = df[(df[prop] == dt_min)]
        df = filtered_df1.append(filtered_df2)
    return df

def display_chi_squared(map_df, filtering_criteria):
    print(map_df.params_index.max())
    print(map_df.galaxy_index.max())
    columns = ['galaxy_index', 'params_index', 'chi2_calc', 'chi2_king', 'chi2_76']
    # chi_df = pd.DataFrame(columns=columns)
    outflow_props = []
    flag = False
    for par_index in range(map_df.params_index.max()+1):
        for gal_ind in range(map_df.galaxy_index.max()+1):
            file_name = params_output_name + '_' + str(map_df.params_index.values[par_index-1]) + '_' + str(
                map_df.galaxy_index.values[gal_ind-1])+ '.csv'
            outflow = pd.read_csv(file_name)
            # outflow_props.append(outflow)
            print(outflow)
            chi_square_calc = 0
            chi_square_king = 0
            chi_square_76 = 0
            for index in outflow.dot_mass_arr.index[:-1]:
                # lagn_calc = np.multiply(np.abs(outflow.dot_mass_arr[index])*unit_sunmass, (np.abs(outflow.dot_radius_arr[index]*1000.)**2.)*1.e7)
                lagn_calc = (np.abs(outflow.dot_mass_arr[index])*unit_sunmass) * (np.abs(outflow.dot_radius_arr[index]*1000.)**2.)*1.e7
                # lagn_th_king = np.power((np.abs(outflow.dot_mass_arr[index]*unit_sunmass*1000.*1.e7)), 3.)
                lagn_th_king = np.abs(outflow.dot_mass_arr[index]*unit_sunmass*1000.*1.e7)** 3.
                # lagn_th_76 = np.power((np.abs(outflow.dot_mass_arr[index]*unit_sunmass*1000.*1.e7)),1.31578947)
                lagn_th_76 = (np.abs(outflow.dot_mass_arr[index]*unit_sunmass*1000.*1.e7)*1.31578947)

                chi_square_calc = chi_square_calc + np.divide(((lagn_calc - outflow.luminosity_AGN_arr[index])**2.), lagn_calc)
                chi_square_king = chi_square_king + np.divide(((lagn_th_king - outflow.luminosity_AGN_arr[index])**2.),lagn_th_king)
                chi_square_76 = chi_square_76 + np.divide(((lagn_th_76 - outflow.luminosity_AGN_arr[index])**2.),lagn_th_76)

            print(chi_square_calc, 'calc')
            print(chi_square_king, 'king')
            print(chi_square_76, '76')
            if flag:
                chi_df.append(
                    pd.DataFrame([gal_ind - 1, par_index - 1, chi_square_calc, chi_square_king, chi_square_76],
                                 columns=columns))
            else:
                chi_df = pd.DataFrame([gal_ind - 1, par_index - 1, chi_square_calc, chi_square_king, chi_square_76],
                                      columns=columns)
                flag = True

            # chi_df.append(pd.DataFrame([gal_ind-1, par_index-1, chi_square_calc, chi_square_king, chi_square_76], columns=columns))
    print(chi_df)
            #     0.76

            # outflow_props.append(outflow)
    # print(len(outflow_props))


