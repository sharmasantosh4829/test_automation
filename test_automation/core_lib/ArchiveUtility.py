"""Class file for Archiving operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
from datetime import datetime
import os
import sys
import zipfile

# Appending root dir (test_automation), core_lib, constants and logs dirs to sys.path.
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir))))

from constants.GenericConstants import *

sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir)), CORE_LIB_DIR))
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir)), CONSTANTS_DIR))


def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as z:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                z.write(os.path.join(root, file))
            for directory in dirs:
                z.write(os.path.join(root, directory))


class ArchiveUtility:
    '''src: source folder path
    dst: destination folder path'''
    def __init__(self, src, dst, run_name=None):
        self.src = src
        self.dst = dst
        self.archive_dir = os.path.join \
            (os.path.abspath
             (os.path.join
              (os.path.dirname
                (os.path.abspath(__file__)), os.pardir)), ARCHIVE_DIR)
        self.folder_name = str(run_name) + "_" + datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
        # zip_folder(self.src, os.path.join(self.archive_dir, self.folder_name))
        zip_folder(self.src, os.path.join(self.dst, self.folder_name))


if __name__ == '__main__':
    archive_obj = ArchiveUtility("", "")