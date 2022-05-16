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

def createFolderIfNotExists(folder):
    if not(os.path.exists(folder)):
        print(f'Creating {folder} folder')
        os.makedirs(folder)
    # switch to folder
    os.chdir(folder)
    return

# opening sftp connection
with pysftp.Connection(host=HOSTNAME, username=USERNAME, password=PASSWORD) as sftp:
    print("Connection successfully established ... ")

    # check if data folder exists
    folder = 'data'
    createFolderIfNotExists(folder)
    root_folder = os.path.abspath(os.getcwd())

    # list countries
    countries_list = sftp.listdir_attr()
    for country in countries_list:
        os.chdir(root_folder)
        folder = country.filename
        print(f'\tFound country {folder}')
        createFolderIfNotExists(folder)  # check if country exists
        # back to main folder

    # Switch to a remote directory
    sftp.cwd('moz')
    sftp.cwd('raster')
    sftp.cwd('2022')
    sftp.cwd('05')
    sftp.cwd('15')

    # Obtain structure of the remote directory '/opt'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
        print(attr.filename, attr)