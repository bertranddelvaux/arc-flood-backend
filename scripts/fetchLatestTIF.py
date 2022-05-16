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
with pysftp.Connection(host=HOSTNAME, username=USERNAME, password=PASSWORD) as sftp:
    print("Connection successfully established ... ")

    # check if data folder exists
    folder = 'data'
    createFolderIfNotExists(folder, n=0)
    root_folder = os.path.abspath(os.getcwd())

    # list countries
    countries = [c.filename for c in sftp.listdir_attr()]
    for country in countries:
        os.chdir(root_folder)  # switch to root_folder
        n = 1
        print(f'{indent(n)}Found country {country}')
        createFolderIfNotExists(country, n)  # check if country exists

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