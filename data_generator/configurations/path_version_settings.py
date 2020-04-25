import os

version = 3
params_path = "C:/Users/Monika/PycharmProjects/galactic-outflows-nn/data_generator/results/"
values_version_folder = 'v' + str(version) + '/'
try:
    os.mkdir(params_path + values_version_folder)
except:
    pass