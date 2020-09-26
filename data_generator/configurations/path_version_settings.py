import os
# TODO maybe these should be red from file as well or otherwise shouldn't versions be automatic?
# version = 'predictions_1.4'
# version = 5
# version = 9.0
# version = 9.2
version = 13.0
# version = 10.5
# temke 1, po 5 ep sukimas 1
# version = '3.2_predictions'
# ep = 25
ep=30
# version = '11.1'+str(ep)+'_predictions'
# version = '1.1_predictions'
# version = 6.1
params_path = "C:/Users/Monika/PycharmProjects/galactic-outflows-nn/data_generator/results/"
values_version_folder = 'v' + str(version) + '/'
# predictions_file = 'predictions/ep'+str(ep)+'_predictions'
predictions_file = 'predictions/ep'+str(ep)+'_predictions_more_data'
# predictions_file = 'predictions/ep'+str(ep)+'_2_try'
try:
    os.mkdir(params_path + values_version_folder)
except:
    print('didnt create folder or exists')