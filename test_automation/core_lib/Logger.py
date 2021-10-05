""" Generic Logger class which can be implemented by any module for logging"""

# system imports
import os
import sys
import traceback
import logging

# Appending root dir (test_automation), core_lib and logs dirs to sys.path.
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir)), "core_lib"))
sys.path.append(os.path.join\
            (os.path.abspath
             (os.path.join
              (os.path.dirname
               (os.path.abspath(__file__)), os.pardir))))


class Logger:

    def __init__(self, logger_name=None, log_dir=None):
        """Create new logger.
            :param logger_name: name of new logger, ``str``
            :param log_dir: logs directory path, ``abs path``
        """
        self.logger_name=logger_name
        self.file_handler=None
        self.stream_handler=None
        self.log_dir=log_dir
        self.file_handler_name=None

        if logger_name is None:
            self.logger_name=os.path.basename(__file__).replace('.py', '')
        self.logger = logging.getLogger(self.logger_name)

        if log_dir is None:
            self.log_dir = os.path.join\
                (os.path.abspath
                 (os.path.join
                  (os.path.dirname
                   (os.path.abspath(__file__)), os.pardir)), "logs")
        try:
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def set_logger_log_level(self, level=logging.DEBUG):
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

    def create_handler(self, handler_name=None, log_level=logging.DEBUG):
        """Create file handler.
            :param handler_name: name of the handler, ``str``
            :param log_level: log level of the file handler, default:debug, ``str`` or ``int``
        """
        try:
            if handler_name:
                self.file_handler_name = os.path.join \
                    (self.log_dir, handler_name)
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
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
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

    def logging_master(self, logger_name=None,
                       log_dir=None,
                       handler_name=None,
                       logger_log_level=logging.DEBUG,
                       handler_log_level=logging.ERROR,
                       log_format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'):
        """Master Api for from logger class.
            custom_logger = Logger('LoggerUtility')
            custom_logger.set_logger_log_level(logging.DEBUG)
            f_handler = custom_logger.create_handler('LoggerUtility.log', logging.ERROR)
            s_handler = custom_logger.create_handler()
            custom_logger.add_handler(f_handler)
            custom_logger.add_handler(s_handler)
            custom_logger.set_log_format(f_handler)
            custom_logger.set_log_format(s_handler)
        """
        self.logger_name = logger_name
        self.file_handler = None
        self.stream_handler = None
        self.log_dir = log_dir
        self.file_handler_name = None

        try:
            if logger_name is None:
                self.logger_name = os.path.basename(__file__).replace('.py', '')
            self.logger = logging.getLogger(self.logger_name)
            self.logger.setLevel(logger_log_level)
        except Exception as e:
            custom_logger.exception()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

        if log_dir is None:
            self.log_dir = os.path.join \
                (os.path.abspath
                 (os.path.join
                  (os.path.dirname
                   (os.path.abspath(__file__)), os.pardir)), "logs")
        try:
            if not os.path.exists(self.log_dir):
                os.mkdir(self.log_dir)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

        try:
            if handler_name:
                self.file_handler_name = os.path.join \
                    (self.log_dir, handler_name)
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


if __name__ == '__main__':
    custom_logger = Logger()
    # custom_logger.set_logger_log_level(logging.DEBUG)
    # f_handler = custom_logger.create_handler('LoggerUtility.log', logging.ERROR)
    # s_handler = custom_logger.create_handler()
    # custom_logger.add_handler(f_handler)
    # custom_logger.add_handler(s_handler)
    # custom_logger.set_log_format(f_handler)
    # custom_logger.set_log_format(s_handler)
    custom_logger.logging_master(handler_name='LoggerUtility.log')
    custom_logger.debug("Hi, This is a test Debug message", "Hello")
    custom_logger.info("Hi, This is an test Info message")
    custom_logger.warning("Hi, This is a test Warning message")
    custom_logger.error("Hi, This is a test Error message")
    custom_logger.critical("Hi, This is a test Critical message")
    custom_logger.exception("Hi, This is an test Exception message")