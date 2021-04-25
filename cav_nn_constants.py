#####################################################################################################
#  Dan Ryan
#
#  College Of Charleston - CSIS-641 Advanced Cybersecurity
#
#  04/01/2021
#
#  ryand2@g.cofc.edu
#
#  Constants used throughout the application
#
#####################################################################################################

DATA_DIRECTORY = 'data'
MODEL_DIRECTORY = 'models'
ANALYSIS_DIRECTORY = 'analysis'

TEST_DATA_URL = 'http://kdd.ics.uci.edu/databases/kddcup99/corrected.gz'
TEST_DATA_LOCAL = DATA_DIRECTORY + '/corrected.gz'
TEST_DATA_UNZIPPED = DATA_DIRECTORY + '/test'

TRAIN_DATA_URL = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz'
TRAIN_DATA_LOCAL = DATA_DIRECTORY + '/kddcup.data.gz'
TRAIN_DATA_UNZIPPED = DATA_DIRECTORY + '/train'

TRAIN_DATA_X = DATA_DIRECTORY + '/train_X'
TRAIN_DATA_Y = DATA_DIRECTORY + '/train_Y'
TRAIN_DATA_Y_BINARY = DATA_DIRECTORY + '/train_Y_binary'
TEST_DATA_X = DATA_DIRECTORY + '/test_X'
TEST_DATA_Y = DATA_DIRECTORY + '/test_Y'
TEST_DATA_Y_BINARY = DATA_DIRECTORY + '/test_Y_binary'

TEST_X_BUFFER_OVERFLOW = DATA_DIRECTORY + '/test_X_buffer_overflow'
TEST_X_FTP_WRITE = DATA_DIRECTORY + '/test_X_ftp_write'
TEST_X_GUESS_PSWD = DATA_DIRECTORY + '/test_X_guess_password'
TEST_X_IPSWEEP = DATA_DIRECTORY + '/test_X_ipsweep'
TEST_X_NEPTUNE = DATA_DIRECTORY + '/test_X_neptune'
TEST_X_NMAP = DATA_DIRECTORY + '/test_X_nmap'
TEST_X_NORMAL = DATA_DIRECTORY + '/test_X_normal'
TEST_X_POD = DATA_DIRECTORY + '/test_X_pod'
TEST_X_SMURF = DATA_DIRECTORY + '/test_X_smurf'
TEST_X_TEARDROP = DATA_DIRECTORY + '/test_X_teardrop'
TEST_X_CATEGORIES = [TEST_X_BUFFER_OVERFLOW, TEST_X_FTP_WRITE, TEST_X_GUESS_PSWD, TEST_X_IPSWEEP, TEST_X_NEPTUNE,
                     TEST_X_NMAP, TEST_X_NORMAL, TEST_X_POD, TEST_X_SMURF, TEST_X_TEARDROP]

TEST_Y_BUFFER_OVERFLOW = DATA_DIRECTORY + '/test_Y_buffer_overflow'
TEST_Y_FTP_WRITE = DATA_DIRECTORY + '/test_Y_ftp_write'
TEST_Y_GUESS_PSWD = DATA_DIRECTORY + '/test_Y_guess_password'
TEST_Y_IPSWEEP = DATA_DIRECTORY + '/test_Y_ipsweep'
TEST_Y_NEPTUNE = DATA_DIRECTORY + '/test_Y_neptune'
TEST_Y_NMAP = DATA_DIRECTORY + '/test_Y_nmap'
TEST_Y_NORMAL = DATA_DIRECTORY + '/test_Y_normal'
TEST_Y_POD = DATA_DIRECTORY + '/test_Y_pod'
TEST_Y_SMURF = DATA_DIRECTORY + '/test_Y_smurf'
TEST_Y_TEARDROP = DATA_DIRECTORY + '/test_Y_teardrop'
TEST_Y_CATEGORIES = [TEST_Y_BUFFER_OVERFLOW, TEST_Y_FTP_WRITE, TEST_Y_GUESS_PSWD, TEST_Y_IPSWEEP, TEST_Y_NEPTUNE,
                     TEST_Y_NMAP, TEST_Y_NORMAL, TEST_Y_POD, TEST_Y_SMURF, TEST_Y_TEARDROP]


MODEL_ANALYSIS_FILE = ANALYSIS_DIRECTORY + '/model_compare.txt'
