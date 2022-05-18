#####################################################
# Author: Bertrand Delvaux (2022)                   #
#                                                   #
# Script to mirror JBA's data to ARC backend server #
#                                                   #
#####################################################

import os
import pysftp

# connection parameters
HOSTNAME = 'sftp.floodforesight.com'
USERNAME = os.environ['JBA_USERNAME']
PASSWORD = os.environ['JBA_PASSWORD']
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


def indent(n):
    return n * '\t'


def createFolderIfNotExists(folder, n):
    if not(os.path.exists(folder)):
        print(f'{indent(n)}Creating {folder} folder')
        os.makedirs(folder)
    # switch to folder
    os.chdir(folder)
    return

# opening sftp connection
with pysftp.Connection(host=HOSTNAME, username=USERNAME, password=PASSWORD, cnopts=cnopts) as sftp:
    print("Connection successfully established ... ")

    # data
    n = 0  # indentation level
    data = 'data'
    createFolderIfNotExists(data, n)  # check if data folder exists
    data_path = os.path.abspath(os.getcwd())  # get absolute path for future reference

    #sftp.get_r('/', data_path, preserve_mtime=True)
    #sftp.get_r('/moz/raster/2022/04/28', data_path, preserve_mtime=False)
    sftp.get_r('/moz', data_path, preserve_mtime=False)
