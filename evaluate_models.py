#####################################################################################################
#  Dan Ryan
#
#  College Of Charleston - CSIS-641 Advanced Cybersecurity
#
#  04/01/2021
#
#  ryand2@g.cofc.edu
#
#  Evaluates all models saved in the /models folder against the training/testing datasets
#
#####################################################################################################

import pandas as pd
import os
from cav_nn_constants import *
import keras

# Create an analysis folder, if it doesn't exist
if not os.path.exists(ANALYSIS_DIRECTORY):
    os.mkdir(ANALYSIS_DIRECTORY)

# If an analysis file already exists, remove it
if os.path.exists(MODEL_ANALYSIS_FILE):
    os.remove(MODEL_ANALYSIS_FILE)

train_x = pd.read_csv(TRAIN_DATA_X, header=None).fillna(0).values
train_y_binary = pd.read_csv(TRAIN_DATA_Y_BINARY, header=None).values
train_y_softmax = pd.read_csv(TRAIN_DATA_Y, header=None).values

test_x = pd.read_csv(TEST_DATA_X, header=None).fillna(0).values
test_y_binary = pd.read_csv(TEST_DATA_Y_BINARY, header=None).values
test_y_softmax = pd.read_csv(TEST_DATA_Y, header=None).values

analysis_file = open(MODEL_ANALYSIS_FILE, 'w')

for file in os.listdir(MODEL_DIRECTORY):
    filepath = MODEL_DIRECTORY + '/' + file

    train_y = train_y_binary
    test_y = test_y_binary

    if 'softmax' in file:
        train_y = train_y_softmax
        test_y = test_y_softmax

    model = keras.models.load_model(filepath)

    _, train_accuracy = model.evaluate(train_x, train_y, verbose=0)
    _, test_accuracy = model.evaluate(test_x, test_y, verbose=0)

    analysis_file.write('************************************************\n')
    analysis_file.write('Model = ' + file + '\n')
    analysis_file.write('Training Accuracy: %.2f\n' % (train_accuracy * 100))
    analysis_file.write('Testing Accuracy: %.2f\n' % (test_accuracy * 100))
    analysis_file.write('************************************************\n\n')

for x_file, y_file in zip(TEST_X_CATEGORIES, TEST_Y_CATEGORIES):
    test_x = pd.read_csv(x_file, header=None).fillna(0).values
    test_y = pd.read_csv(y_file, header=None).values

    filepath = MODEL_DIRECTORY + '/' + 'softmax_3(64_16_10).h5'

    model = keras.models.load_model(filepath)

    _, test_accuracy = model.evaluate(test_x, test_y, verbose=0)

    analysis_file.write('************************************************\n')
    analysis_file.write('Model = ' + file + '\n')
    analysis_file.write('Subset = ' + x_file + '\n')
    analysis_file.write('Testing Accuracy: %.2f\n' % (test_accuracy * 100))
    analysis_file.write('************************************************\n\n')

analysis_file.close()

