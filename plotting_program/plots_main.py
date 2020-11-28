import pandas as pd

from configurations.path_version_settings import params_path, values_version_folder
from plotting_program.plots.generic_time_relation_plot import generic_time_relation_plot
from plotting_program.plots.generic_radius_relation import generic_radius_relation_plot

params_output_name = params_path + values_version_folder
outflow_props = []

galaxy_props_map = pd.read_csv(params_output_name+'properties_map.csv')
# failed_outflows = pd.read_csv(params_output_name+'failed_outflows.csv')
unique_galaxies = pd.unique(galaxy_props_map['galaxy_mass'])
failed_unique_galaxies = pd.unique(failed_outflows['galaxy_mass'])
unique_quasar_durations = pd.unique(galaxy_props_map['quasar_duration'])
failed_unique_quasar_durations = pd.unique(failed_outflows['quasar_duration'])
unique_duty_cycles = pd.unique(galaxy_props_map['duty_cycle'])
unique_bulge_masses = pd.unique(galaxy_props_map['bulge_mass'])
# unique_bulge_masses =galaxy_props_map.groupby(['bulge_mass'])
# print(unique_bulge_masses)
unique_bulge_gas_fractions = pd.unique(galaxy_props_map.bulge_gas_frac)
# same_bulge_gas_fractions_df = galaxy_props_map[galaxy_props_map.bulge_gas_frac == unique_bulge_gas_fractions]
# print(same_bulge_gas_fractions_df)
# print(unique_bulge_gas_fractions)

# for indication_index, unique_bulge_mass in enumerate(unique_bulge_masses):
#     same_bulge_mass = galaxy_props_map[galaxy_props_map.bulge_mass == unique_bulge_mass]
#     # a = same_quasar_durations_df[(same_quasar_durations_df.galaxy_mass.values > 15732978816292.) & (same_quasar_durations_df.galaxy_mass.values < 15732978816292.9)]
#     # print(same_bulge_gas_fraction_df)
#     labels = []
#
#     # print(len(filtered_df))
#     outflow_props = []
#
#     for index in same_bulge_mass.index:
#         file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
#         outflow_props.append(pd.read_csv(file_name))
#         labels.append('fade_type ' + str(format(same_bulge_mass.fade_type[index])))
#     generic_time_relation_plot(outflow_props, str(indication_index) + '-unique-quasar-dt-cy-gal1.6E13-gas0.1')
#     generic_radius_relation_plot(outflow_props, labels, str(indication_index) + '-unique-quasar-dt-cy-gal1.6E13-gas0.1')

for indication_index, quasar_duration in enumerate(unique_quasar_durations):
    same_quasar_durations_df = galaxy_props_map[galaxy_props_map.quasar_duration == quasar_duration]
    a = same_quasar_durations_df[(same_quasar_durations_df.galaxy_mass.values > 15732978816000.) & (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9)]
    # print(same_bulge_gas_fraction_df)
    labels = []

    # print(len(filtered_df))

    for galax_i, galaxy in enumerate(unique_galaxies):
        same_galaxies_df = galaxy_props_map[galaxy_props_map.galaxy_mass == galaxy]
        filtered_df = same_galaxies_df[
            # (same_quasar_durations_df.galaxy_mass.values > 15732978816000.) &
            #                                    (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9) &
            #                                    (same_quasar_durations_df.smbh_mass > 746903400.00) &
            #                                    (same_quasar_durations_df.smbh_mass < 746903499.9) &
            #                                    (same_quasar_durations_df.bulge_mass > 203033496000.0) &
            #                                    (same_quasar_durations_df.bulge_mass < 203033496999.9) &
            (same_galaxies_df.fade_type == 'exponential') &
            (same_galaxies_df.bulge_gas_frac > 0.01) &
            (same_galaxies_df.bulge_gas_frac < 0.1)]
        # (same_quasar_durations_df.bulge_gas_frac == 0.1)]
        # (same_quasar_durations_df.bulge_gas_frac == 0.2125)]

        outflow_props = []
        # for galaxy_ind in same_galaxies_df.index:

        for index in filtered_df.index:
            try:
                file_name = params_output_name + '_' + str(galaxy_props_map.params_index.values[index]) + '_' + \
                            str(galaxy_props_map.galaxy_index.values[galax_i]) +'.csv'
                # print(file_name)
                outflow_props.append(pd.read_csv(file_name))
                labels.append('duty_cycle ' + str(format(filtered_df.duty_cycle[index], '.2f')))
            except FileNotFoundError:
                print('pass')
        generic_time_relation_plot(outflow_props, str(indication_index)+str(galax_i) + '-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')
        generic_radius_relation_plot(outflow_props, labels, str(indication_index)+str(galax_i) + '-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')


for indication_index, quasar_duration in enumerate(failed_unique_quasar_durations):
    same_quasar_durations_df = failed_outflows[failed_outflows.quasar_duration == quasar_duration]
    a = same_quasar_durations_df[(same_quasar_durations_df.galaxy_mass.values > 15732978816000.) & (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9)]
    # print(same_bulge_gas_fraction_df)
    labels = []
    filtered_df = same_quasar_durations_df[
        # (same_quasar_durations_df.galaxy_mass.values > 15732978816000.) &
        #                                    (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9) &
        #                                    (same_quasar_durations_df.smbh_mass > 746903400.00) &
        #                                    (same_quasar_durations_df.smbh_mass < 746903499.9) &
        #                                    (same_quasar_durations_df.bulge_mass > 203033496000.0) &
        #                                    (same_quasar_durations_df.bulge_mass < 203033496999.9) &
                                           (same_quasar_durations_df.fade_type == 'exponential') &
                                           (same_quasar_durations_df.bulge_gas_frac > 0.01) &
                                           (same_quasar_durations_df.bulge_gas_frac < 0.9)]
                                           # (same_quasar_durations_df.bulge_gas_frac == 0.1)]
                                           # (same_quasar_durations_df.bulge_gas_frac == 0.2125)]

    # print(len(filtered_df))
    for galaxy in failed_unique_galaxies:
        same_galaxies_df = failed_outflows[failed_outflows.galaxy_mass == galaxy]

        outflow_props = []
        for galaxy_ind in same_galaxies_df.index:

            for index in filtered_df.index:
                try:
                    file_name = params_output_name + '_failed' + str(failed_outflows.params_index.values[index]) + '_' + \
                                str(failed_outflows.galaxy_index.values[galaxy_ind]) +'.csv'
                    # print(file_name)
                    outflow_props.append(pd.read_csv(file_name))
                    labels.append('duty_cycle ' + str(format(filtered_df.duty_cycle[index], '.2f')))
                except FileNotFoundError:
                    print('pass')
        generic_time_relation_plot(outflow_props, str(indication_index)+str(galaxy_ind) + 'failed-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')
        generic_radius_relation_plot(outflow_props, labels, str(indication_index)+str(galaxy_ind) + 'failed-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')

# for indication_index, quasar_duration in enumerate(unique_quasar_durations):
#     same_quasar_durations_df = galaxy_props_map[galaxy_props_map.quasar_duration == quasar_duration]
#     a = same_quasar_durations_df[(same_quasar_durations_df.galaxy_mass.values > 15732978816000.) & (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9)]
#     # print(same_bulge_gas_fraction_df)
#     labels = []
#     filtered_df = same_quasar_durations_df[
#         # (same_quasar_durations_df.galaxy_mass.values > 15732978816000.) &
#         #                                    (same_quasar_durations_df.galaxy_mass.values < 15732978816999.9) &
#         #                                    (same_quasar_durations_df.smbh_mass > 746903400.00) &
#         #                                    (same_quasar_durations_df.smbh_mass < 746903499.9) &
#         #                                    (same_quasar_durations_df.bulge_mass > 203033496000.0) &
#         #                                    (same_quasar_durations_df.bulge_mass < 203033496999.9) &
#                                            (same_quasar_durations_df.fade_type == 'exponential') &
#                                            (same_quasar_durations_df.bulge_gas_frac > 0.01) &
#                                            (same_quasar_durations_df.bulge_gas_frac < 0.9)]
#                                            # (same_quasar_durations_df.bulge_gas_frac == 0.1)]
#                                            # (same_quasar_durations_df.bulge_gas_frac == 0.2125)]
#
#     # print(len(filtered_df))
#     outflow_props = []
#     for galaxy in unique_galaxies:
#         same_galaxies_df = galaxy_props_map[galaxy_props_map.galaxy_mass == galaxy]
#
#         for galaxy_ind in same_galaxies_df.index:
#
#             for index in filtered_df.index:
#                 try:
#                     file_name = params_output_name + '_failed' + str(galaxy_props_map.params_index.values[index]) + '_' + \
#                                 str(galaxy_props_map.galaxy_index.values[galaxy_ind]) +'.csv'
#                     print(file_name)
#                     outflow_props.append(pd.read_csv(file_name))
#                     labels.append('duty_cycle ' + str(format(filtered_df.duty_cycle[index], '.2f')))
#                 except FileNotFoundError:
#                     print('pass')
#     generic_time_relation_plot(outflow_props, str(indication_index) + 'failed-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')
#     generic_radius_relation_plot(outflow_props, labels, str(indication_index) + 'failed-exp-unique-quasar-dt-cy-gal1.6E13-gas0.1')

# for indication_index, unique_duty_cycle in enumerate(unique_duty_cycles):
#     same_duty_cycles_df = galaxy_props_map[galaxy_props_map.duty_cycle == unique_duty_cycle]
#     a = same_duty_cycles_df[(same_duty_cycles_df.galaxy_mass.values > 15732978816292.) & (same_duty_cycles_df.galaxy_mass.values < 15732978816292.9)]
#     # print(same_bulge_gas_fraction_df)
#     filtered_df = same_duty_cycles_df[(same_duty_cycles_df.galaxy_mass.values > 15732978816292.) &
#                                            (same_duty_cycles_df.galaxy_mass.values < 15732978816292.9) &
#                                            (same_duty_cycles_df.smbh_mass > 746903489.42) &
#                                            (same_duty_cycles_df.smbh_mass < 746903489.5) &
#                                            (same_duty_cycles_df.bulge_mass > 203033496728.9) &
#                                            (same_duty_cycles_df.bulge_mass < 203033496728.99) &
#                                            (same_duty_cycles_df.fade_type == 'none') &
#                                            # (same_duty_cycles_df.bulge_gas_frac == 0.1)]
#                                            (same_duty_cycles_df.bulge_gas_frac == 0.2125)]
#
#     # print(len(filtered_df))
#     outflow_props = []
#     labels = []
#
#     for index in filtered_df.index:
#         file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
#         outflow_props.append(pd.read_csv(file_name))
#         labels.append('quasar dur ' + str(format(filtered_df.quasar_duration[index], '.0f')))
#     generic_time_relation_plot(outflow_props, str(indication_index) + '-unique-duty-cycle-quasar-gal1.6E13-gas0.2')
#     generic_radius_relation_plot(outflow_props, labels, str(indication_index) + '-unique-duty-cycle-quasar-gal1.6E13-gas0.2')



# for indication_index, gas_fraction in enumerate(unique_bulge_gas_fractions):
#     same_bulge_gas_fraction_df = galaxy_props_map[galaxy_props_map.bulge_gas_frac == gas_fraction]
#     # print(same_bulge_gas_fraction_df)
#     outflow_props = []
#
#     for index in same_bulge_gas_fraction_df.index:
#         file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
#         outflow_props.append(pd.read_csv(file_name))
#     generic_time_relation_plot(outflow_props, str(indication_index) + '-same-gasf')
#     generic_radius_relation_plot(outflow_props, str(indication_index) + '-same-gasf')


# for indication_index, bulge_mass in enumerate(unique_bulge_masses):
#     same_bulge_masses = galaxy_props_map[galaxy_props_map.bulge_mass == bulge_mass]
#     # filtered_props = same_bulge_masses[same_bulge_masses.bulge_gas_frac >=0.5]
#     outflow_props = []
#
#     for index in same_bulge_masses.index:
#         file_name = params_output_name + '_' + str(galaxy_props_map.bulge_index.values[index]) + '_' + str(galaxy_props_map.params_index.values[index]) + '_0.csv'
#         outflow_props.append(pd.read_csv(file_name))
#     generic_time_relation_plot(outflow_props, indication=str(indication_index) + '-same-bulgemass')
#     generic_radius_relation_plot(outflow_props, indication=str(indication_index) + '-same-bulgemass')
#
