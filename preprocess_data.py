#####################################################################################################
#  Dan Ryan
#
#  College Of Charleston - CSIS-641 Advanced Cybersecurity
#
#  04/01/2021
#
#  ryand2@g.cofc.edu
#
#  Preprocess the KDD-99 dataset for CAV usage
#
#####################################################################################################

from cav_nn_constants import *
import pandas as pd
import os


def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].astype(float).max()
        min_value = df[feature_name].astype(float).min()
        result[feature_name] = (df[feature_name].astype(float) - min_value) / (max_value - min_value)
    return result


for file in [TRAIN_DATA_X, TRAIN_DATA_Y, TEST_DATA_X, TEST_DATA_Y, TRAIN_DATA_Y_BINARY, TEST_DATA_Y_BINARY]:
    if os.path.exists(file):
        os.remove(file)

for file in TEST_X_CATEGORIES:
    if os.path.exists(file):
        os.remove(file)

for file in TEST_Y_CATEGORIES:
    if os.path.exists(file):
        os.remove(file)

labels = ['duration', 'protocol', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_frag', 'urgent', 'hot',
          'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempt', 'num_root',
          'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
          'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
          'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
          'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
          'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
          'dst_host_srv_rerror_rate', 'label']

categorical_columns = ['protocol', 'service', 'flag']  # Plus label

one_hot_labels = ['buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'ipsweep.', 'neptune.', 'nmap.', 'normal.',
                  'pod.', 'smurf.', 'teardrop.']

services = ['auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i',
            'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'hostnames', 'http', 'http_443', 'imap4',
            'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns',
            'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pop_2', 'pop_3', 'printer', 'private',
            'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'time',
            'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'Z39_50']

flags = ['SF', 'S0', 'REJ', 'RSTO', 'SH', 'S1', 'RSTR', 'S2', 'S3']

# Create dataframes from input data
train_df = pd.read_csv(TRAIN_DATA_UNZIPPED, header=None, names=labels)
test_df = pd.read_csv(TEST_DATA_UNZIPPED, header=None, names=labels)

# Only include the labels of interest
train_df = train_df[train_df['label'].isin(one_hot_labels)]
test_df = test_df[test_df['label'].isin(one_hot_labels)]

# Only include the flags of interest
train_df = train_df[train_df['flag'].isin(flags)]
test_df = test_df[test_df['flag'].isin(flags)]

# Only include the services of interest
train_df = train_df[train_df['service'].isin(services)]
test_df = test_df[test_df['service'].isin(services)]

# One hot encode the categorical attributes
for col in categorical_columns:
    train_dummies = pd.get_dummies(train_df[col])
    test_dummies = pd.get_dummies(test_df[col])

    for dummy in train_dummies:
        train_df.insert(0, col + '_' + dummy, train_dummies[dummy])

    for dummy in test_dummies:
        test_df.insert(0, col + '_' + dummy, test_dummies[dummy])

    train_df = train_df.drop(col, axis=1)
    test_df = test_df.drop(col, axis=1)

# One hot encode the label attribute
train_y = pd.get_dummies(train_df['label'])
test_y = pd.get_dummies(test_df['label'])

# Create a binary classification
train_y_binary = (train_df.label != 'normal.').astype(int)
test_y_binary = (test_df.label != 'normal.').astype(int)

# Separate the X values
train_x = train_df.drop('label', axis=1)
test_x = test_df.drop('label', axis=1)

# Normalize the X values
train_x = normalize(train_x)
test_x = normalize(test_x)

# Create test datasets for each output category to be evaluated individually
for category, x_filename, y_filename in zip(one_hot_labels, TEST_X_CATEGORIES, TEST_Y_CATEGORIES):
    test_x_cat = test_df[test_df['label'].isin([category])]
    test_y_cat = pd.Series(test_x_cat['label']).to_frame(name='label')

    for i, new_col in zip(range(1, 11), one_hot_labels):
        test_y_cat.insert(i, new_col, 0)

    test_y_cat[category] = 1
    test_y_cat.drop('label', axis=1, inplace=True)

    test_x_cat = test_x_cat.drop('label', axis=1)
    test_x_cat = normalize(test_x_cat)

    test_x_cat.to_csv(x_filename, header=False, index=False)
    test_y_cat.to_csv(y_filename, header=False, index=False)


train_y.to_csv(TRAIN_DATA_Y, header=False, index=False)
test_y.to_csv(TEST_DATA_Y, header=False, index=False)

train_y_binary.to_csv(TRAIN_DATA_Y_BINARY, header=False, index=False)
test_y_binary.to_csv(TEST_DATA_Y_BINARY, header=False, index=False)

train_x.to_csv(TRAIN_DATA_X, header=False, index=False)
test_x.to_csv(TEST_DATA_X, header=False, index=False)
