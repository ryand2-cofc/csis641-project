#####################################################################################################
#  Dan Ryan
#
#  College Of Charleston - CSIS-641 Advanced Cybersecurity
#
#  04/01/2021
#
#  ryand2@g.cofc.edu
#
#  Builds and tests a NN model based on a binary classification (normal = 0, intrusion = 1)
#
#####################################################################################################

import pandas as pd
from cav_nn_constants import *
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import os

# Create a model folder, if it doesn't exist
if not os.path.exists(MODEL_DIRECTORY):
    os.mkdir(MODEL_DIRECTORY)

model_path = MODEL_DIRECTORY + '/binary_reg_3(64_16_1)(100 epochs).h5'

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

train_x = pd.read_csv(TRAIN_DATA_X, header=None).fillna(0).values
train_y = pd.read_csv(TRAIN_DATA_Y_BINARY, header=None).values

test_x = pd.read_csv(TEST_DATA_X, header=None).fillna(0).values
test_y = pd.read_csv(TEST_DATA_Y_BINARY, header=None).values

model = Sequential()
model.add(Dense(64, input_shape=(109,), activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_x, train_y, epochs=10, batch_size=100000)

_, train_accuracy = model.evaluate(train_x, train_y, verbose=0)
_, test_accuracy = model.evaluate(test_x, test_y, verbose=0)

print('Training Accuracy: %.2f' % (train_accuracy * 100))
print('Testing Accuracy: %.2f' % (test_accuracy * 100))

model.save(model_path)
