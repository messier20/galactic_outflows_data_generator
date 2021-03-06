import numpy as np
from model_program.input_parameters.galaxy_parameters import bulge_disc_totalmass_fractions, bulge_disc_gas_fractions

time_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
radius_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_radius_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_bulge_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
out_mass_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_derived_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
tot_mass_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
# dot_mass_one_point_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
avg_dot_mass_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_calc_dot_mass_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_dot_radius_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
dot_radius_one_point_arr_test = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
velocity_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
velocity_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_dot_mass_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_dot_radius_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_dot_mass_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_dot_radius_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
avg_calc_dot_mass_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]

max_dot_mass_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
max_dot_radius_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
# dot_radius_one_point_arr_test = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
# velocity_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
max_dot_mass_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
max_dot_radius_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
max_dot_mass_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
max_dot_radius_one_point_arr_ln = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]