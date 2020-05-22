import os

# version = 'predictions_1.4'
# version = 5
# version = 9.0
version = 10.2
# version = 6.1
params_path = "C:/Users/Monika/PycharmProjects/galactic-outflows-nn/data_generator/results/"
values_version_folder = 'v' + str(version) + '/'
try:
    os.mkdir(params_path + values_version_folder)
except:
    pass