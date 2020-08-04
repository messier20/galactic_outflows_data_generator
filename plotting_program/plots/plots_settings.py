import os
# from model_program.input_parameters.initial_values import version
from data_generator.configurations.path_version_settings import values_version_folder, version

graphs_path = "./graphs/"
plots_version_folder = 'v' + str(version) + '.10_11/'
# plots_version_folder = ''
# plots_version_folder = values_version_folder + '1/'
try:
    os.mkdir(graphs_path + plots_version_folder)
except:
    print('ex')
    pass

plot_velocities = 0
plot_massrate = 0
plot_momentum = 0                   #plots both momentum and energy of the outflow
plot_momentumvsl = 0
plot_pressures = 0
plot_sf = 0
plot_sixpart = 0
plot_threepart = 1
plot_enloadingandr = 0
plot_vandr = 0
plot_enloadingandv = 0
plot_ratios = 0