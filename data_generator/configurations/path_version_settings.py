import os

# version = 'predictions_1.4'
# version = 5
# version = 9.0
# version = 9.2
# version = 10.3
# temke 1, po 5 ep sukimas 1
version = '10.3_predictions_1.1'
# version = 6.1
params_path = "C:/Users/Monika/PycharmProjects/galactic-outflows-nn/data_generator/results/"
values_version_folder = 'v' + str(version) + '/'
try:
    os.mkdir(params_path + values_version_folder)
except:
    pass