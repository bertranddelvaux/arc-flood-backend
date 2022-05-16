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

# opening sftp connection
with pysftp.Connection(host=HOSTNAME, username=USERNAME, password=PASSWORD) as sftp:
    print("Connection successfully established ... ")
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