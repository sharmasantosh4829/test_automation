"""This tool:
    1. Takes two property files of different languages as input.
    2. Compares key-value pairs in both the files.
    3. Removes reduntant key-value pairs.
    4. If key in 1st file found in 2nd, replaces value of key in 2nd by value in 1st file.
    5. Copy line from 1st to 2nd if line not in 2nd.
"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import os
import shutil
import sys
import re

# Appending root dir (test_automation) and core_lib to sys.path
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
              (os.path.dirname
               (os.path.abspath(__file__))), os.pardir)), "core_lib"))

sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
              (os.path.dirname
               (os.path.abspath(__file__))), os.pardir))))

# core_lib imports
from core_lib.ArchiveUtility import *


class FileCompare:
    """File comparison class file"""
    def __init__(self):
        self.tmpDir = os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
              (os.path.dirname
               (os.path.abspath(__file__))), os.pardir)), "temp")
        if not os.path.exists(self.tmpDir):
            os.mkdir(self.tmpDir)

        self.archiveDir = os.path.join \
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.dirname
                (os.path.abspath(__file__))), os.pardir)), "archive")

        sys.argv[1] = "--"
        file1 = sys.argv[2]
        file2 = sys.argv[3]

        self.file1 = shutil.copy(file1, os.path.join(self.tmpDir))
        self.file2 = shutil.copy(file2, os.path.join(self.tmpDir))

        self.file1_dict = self.load_properties(self.file1)
        self.file1_keys = self.file1_dict.keys()
        self.file2_dict = self.load_properties(self.file2)
        self.file2_keys = self.file2_dict.keys()

        self.keys_diff = []
        for key in self.file1_keys:
            if key not in self.file2_keys:
                self.keys_diff.append(key)

        self.keys_diff_1 = []
        for key in self.file2_keys:
            if key not in self.file1_keys:
                self.keys_diff_1.append(key)

        self.keys_modified_1 = []
        for k1 in self.file1_keys:
            k1=str(k1)
            for k2 in self.keys_diff_1:
                k2=str(k2)
                if k1 in k2:
                    self.keys_modified_1.append(k1)

        for key in self.keys_modified_1:
            if key in self.file2_keys:
                self.keys_modified_1.remove(key)

        self.keys_modified_2 = []
        for k1 in self.file1_keys:
            k1 = str(k1)
            for k2 in self.keys_diff_1:
                k2 = str(k2)
                if k1 in k2:
                    self.keys_modified_2.append(k2)

        dictionary = dict(zip(self.keys_modified_1, self.keys_modified_2))

        # [item for item in x if item not in y]
        self.new_keys_in_f2 = [item for item in self.keys_diff_1 if item not in self.keys_modified_2]

        self.lines = []
        with open(self.file2, "r") as fobj:
            self.lines = fobj.readlines()
        for key in self.new_keys_in_f2:
           for line in self.lines:
               if key in line:
                   self.lines.remove(line)
        with open(self.file2, "w") as fobj:
            for line in self.lines:
                fobj.write(line)

        self.lines = []
        with open(self.file2, "r") as fobj:
            self.lines = fobj.readlines()
        for key in self.keys_modified_1:
            for line in self.lines:
                if dictionary[key] in line:
                    line1 = line.replace(dictionary[key], key)
                    self.lines.remove(line)
                    self.lines.append(line1)
        with open(self.file2, "w") as fobj:
            for line in self.lines:
                fobj.write('\n')
                fobj.write(line)

        self.file2_dict = self.load_properties(self.file2)
        self.file2_keys = self.file2_dict.keys()

        self.tmp_lines = []
        with open(self.file1, "r") as fobj:
            self.lines = fobj.readlines()
            for key in self.keys_diff:
                if key not in self.file2_keys:
                    for line in self.lines:
                        if key in line:
                            self.tmp_lines.append(line)
        with open(self.file2, "a") as fobj:
            for line in self.tmp_lines:
                fobj.write('\n')
                fobj.write(line)

        with open(self.file2, "r") as fobj:
            self.lines = fobj.readlines()
            for line in self.lines:
                if re.match(r'^\s*$', line):
                # if len(line.strip())<1:
                    self.lines.remove(line)
        with open(self.file2, "w") as fobj:
            for line in self.lines:
                fobj.write(line)

        shutil.copy(self.file2, os.path.join(self.tmpDir, "copy.properties"))
        self.file3 = os.path.join(self.tmpDir, "copy.properties")

        self.lines = []
        with open(self.file3, "r") as fobj:
            self.lines = fobj.readlines()
        for tmp_line in self.tmp_lines:
            if tmp_line in self.lines:
                tmp_key = tmp_line.split("=")[0]
                self.lines.remove(tmp_line)
                self.lines.append(tmp_key)
        with open(self.file3, "w") as fobj:
            for line in self.lines:
                fobj.write('\n')
                fobj.write(line)

        with open(self.file3, "r") as fobj:
            self.lines = fobj.readlines()
            for line in self.lines:
                if re.match(r'^\s*$', line.strip()) or len(line.strip()) < 1:
                # if len(line.strip())<1:
                    self.lines.remove(line)
        with open(self.file3, "w") as fobj:
            for line in self.lines:
                fobj.write(line)

        with open(self.file2, "r") as fobj:
            self.lines = fobj.readlines()
            for line in self.lines:
                if re.match(r'^\s*$', line.strip()) or len(line.strip()) < 1:
                # if len(line.strip())<1:
                    self.lines.remove(line)
        with open(self.file2, "w") as fobj:
            for line in self.lines:
                fobj.write(line)

        with open(self.file3, "r") as fobj:
            self.lines = fobj.readlines()
            for line in self.lines:
                if re.match(r'^\s*$', line.strip()) or len(line.strip()) < 1:
                # if len(line.strip())<1:
                    self.lines.remove(line)
        with open(self.file3, "w") as fobj:
            for line in self.lines:
                fobj.write(line)

        ArchiveUtility(self.tmpDir, self.archiveDir, run_name="FileCompare")

        for filename in os.listdir(self.tmpDir):
            file_path = os.path.join(self.tmpDir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    if not filename.startswith("__init__.py"):
                        os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def load_properties(self, filepath, sep='=', comment_char='#'):
        """
        Read the file passed as parameter as a properties file.
        """
        props = {}
        with open(filepath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
        return props


if __name__ == '__main__':
    obj = FileCompare()
