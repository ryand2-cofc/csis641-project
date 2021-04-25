#####################################################################################################
#  Dan Ryan
#
#  College Of Charleston - CSIS-641 Advanced Cybersecurity
#
#  04/01/2021
#
#  ryand2@g.cofc.edu
#
#  Downloads the KDD-99 dataset and unzips the data
#
#####################################################################################################

import urllib.request
import gzip
import shutil
import os
from cav_nn_constants import *

# Remove existing data if it exists
if os.path.exists(DATA_DIRECTORY):
    shutil.rmtree(DATA_DIRECTORY)

# Create a folder to hold the data
os.mkdir(DATA_DIRECTORY)

# Download the compressed files from the web
urllib.request.urlretrieve(TRAIN_DATA_URL, TRAIN_DATA_LOCAL)
urllib.request.urlretrieve(TEST_DATA_URL, TEST_DATA_LOCAL)

# Unzip the TRAIN file
with gzip.open(TRAIN_DATA_LOCAL, 'rb') as f_in:
    with open(TRAIN_DATA_UNZIPPED, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Unzip the TEST file
with gzip.open(TEST_DATA_LOCAL, 'rb') as f_in:
    with open(TEST_DATA_UNZIPPED, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Remove the zipped files
os.remove(TRAIN_DATA_LOCAL)
os.remove(TEST_DATA_LOCAL)
