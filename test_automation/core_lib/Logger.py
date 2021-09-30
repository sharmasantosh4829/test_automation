"""Logger class which can be implemented by any module for logging"""

import os
import sys
import time
from time import strftime
import logging
import traceback


class Logger:

    def __init__(self, file_name, logs_dir=None):
        self.file_name = file_name
        self.format = "%Y-%m-%d_%H-%M-%S"

        if logs_dir is None:
            logs_dir = os.path.join(
                os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)), "logs")
        try:
            if not os.path.exists(logs_dir):
                os.mkdir(logs_dir)

            self.logFilePath = os.path.join(logs_dir, self.file_name)
        except:
            print(str(sys.exc_info()[0]))
            print(str(sys.exc_info()[1]))
            print(str(traceback.extract_tb(sys.exc_info()[2])))
            raise
        logging.basicConfig\
            (filename=self.file_name,
             format='%(asctime)s :: %(levelname)s :: %(message)s',
             level=logging.DEBUG)

    def _create_msg(self, *messages):
        logMsg = strftime(self.format) + ": "
        for m in messages:
            logMsg += str(m) + " "
            # print logMsg
        return logMsg

    def critical(self, *messages):
        logging.critical(self._create_msg(*messages))

    def error(self, *messages):
        logging.error(self._create_msg(*messages))

    def warning(self, *messages):
        logging.warning(self._create_msg(*messages))

    def info(self, *messages):
        logging.info(self._create_msg(*messages))

    def debug(self, *messages):
        logging.debug(self._create_msg(*messages))