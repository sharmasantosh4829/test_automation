""" Generic Logger class which can be implemented by any module for logging"""

# system imports
import os
import sys
import traceback
import logging

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
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir)), LOGS_DIR))

# lib imports
import constants.GenericConstants


class Logger:

    def __init__(self, log_dir=None,
                       logger_name=None,
                       handler_name=None,
                       logger_log_level=constants.GenericConstants.debug,
                       handler_log_level=constants.GenericConstants.debug,
                       log_format=log_format):
        """Initialize the logger class.
            :param log_dir: logs dir, default: None, ``abs path``
            :param logger_name: name of the new logger, default: None, ``str``
            :param handler_name: name of the file handler, default: None, ``str``
            :param logger_log_level: log level of the logger, default: debug, ``str, int``
            :param handler_log_level: log level of the file handler, default: error, ``str, int``
            :param log_format: format of the logs line,
                    default:'%(asctime)s:%(name)s:%(levelname)s:%(message)s', ``str``
        """
        self.logger = None
        self.logger_name = None
        self.file_handler = None
        self.file_handler_name = None
        self.stream_handler = None

        if log_dir is None:
            log_dir = os.path.join\
                (os.path.abspath
                 (os.path.join
                  (os.path.dirname
                   (os.path.abspath(__file__)), os.pardir)), LOGS_DIR)
        try:
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            if logger_name is None:
                self.logger_name = os.path.basename(__file__).replace(PY_FILE_EXT, '')
                self.logger = logging.getLogger(self.logger_name)
            else:
                self.logger_name = logger_name
                self.logger = logging.getLogger(self.logger_name)
            self.logger.setLevel(logger_log_level)
            if handler_name is None:
                handler_name = (os.path.basename(__file__).replace(PY_FILE_EXT, LOG_FILE_EXT))
                self.file_handler_name = os.path.join \
                    (log_dir, handler_name)
            else:
                self.file_handler_name = os.path.join \
                    (log_dir, handler_name)
            self.file_handler = logging.FileHandler(self.file_handler_name)
            self.file_handler.setLevel(handler_log_level)
            self.logger.addHandler(self.file_handler)
            self.stream_handler = logging.StreamHandler()
            self.logger.addHandler(self.stream_handler)
            formatter = logging.Formatter(log_format)
            self.file_handler.setFormatter(formatter)
            self.stream_handler.setFormatter(formatter)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def create_log_dir(self, log_dir=None):
        """Create log dir if not already.
            :param log_dir: logs directory path, ``abs path``
        """
        if log_dir is None:
            log_dir = os.path.join\
                (os.path.abspath
                 (os.path.join
                  (os.path.dirname
                   (os.path.abspath(__file__)), os.pardir)), LOGS_DIR)
        try:
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            return log_dir
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def get_logger(self, logger_name=None):
        """Create new logger.
            :param logger_name: logger name, ``str``
        """
        try:
            if logger_name is None:
                self.logger_name=os.path.basename(__file__).replace(PY_FILE_EXT, '')
            else:
                self.logger_name=logger_name
            self.logger = logging.getLogger(self.logger_name)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def set_logger_log_level(self, level=debug):
        """Set log level of the new logger.
            :param level: log level, default: debug, ``int``
        """
        try:
            self.logger.setLevel(level)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def create_handler(self, handler_name=None, log_level=debug):
        """Create file handler.
            :param handler_name: name of the handler, ``str``
            :param log_level: log level of the file handler, default:debug, ``str`` or ``int``
        """
        try:
            if handler_name:
                self.file_handler_name = os.path.join \
                    (self.create_log_dir(), handler_name)
                self.file_handler = logging.FileHandler(self.file_handler_name)
                self.file_handler.setLevel(log_level)
                return self.file_handler
            else:
                self.stream_handler = logging.StreamHandler()
                return self.stream_handler
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def add_handler(self, handler_name):
        """add file handler to the logger.
            :param handler_name: name of the handler, ``str``
        """
        try:
            self.logger.addHandler(handler_name)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def set_log_format(self, handler):
        """set the log format of the handler
            :param handler: name of the handler, ``obj``
        """
        formatter = logging.Formatter(log_format)
        try:
            handler.setFormatter(formatter)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def debug(self, *msgs):
        """log the debug message to the logger
            :param msgs: messages to be logged, default: debug, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.debug(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def info(self, *msgs):
        """log the info message to the logger
            :param msgs: messages to be logged, default: info, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.info(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def warning(self, *msgs):
        """log the warning message to the logger
            :param msgs: messages to be logged, default: warning, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.warning(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def error(self, *msgs):
        """log the error message to the logger
            :param msgs: messages to be logged, default: error, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.error(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def critical(self, *msgs):
        """log the critical message to the logger
            :param msgs: messages to be logged, default: critical, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.critical(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def exception(self, *msgs):
        """log the exceptionn message to the logger
            :param msgs: messages to be logged, default: exception, ``tuple``
        """
        try:
            for msg in msgs:
                self.logger.exception(msg)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e


if __name__ == '__main__':
    custom_logger_obj1 = Logger()
    custom_logger_obj1.debug("Hi, This is a test Debug message", "Hello")
    custom_logger_obj1.info("Hi, This is an test Info message")
    custom_logger_obj1.warning("Hi, This is a test Warning message")
    custom_logger_obj1.error("Hi, This is a test Error message")
    custom_logger_obj1.critical("Hi, This is a test Critical message")
    custom_logger_obj1.exception("Hi, This is an test Exception message")