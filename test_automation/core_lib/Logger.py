""" Generic Logger class which can be implemented by any module for logging"""

import sys
import traceback
import logging


class Logger:

    def __init__(self, logger_name):
        """Create new logger.
            :param logger_name: name of new logger, ``str``
        """
        self.log_level=None
        self.file_handler=None
        self.stream_handler=None
        try:
            self.logger = logging.getLogger(logger_name)
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
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
            print(sys.exc_info()[2])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def create_handler(self, handler_name=None, log_level=logging.DEBUG):
        """Create file handler.
            :param handler_name: name of the handler, ``str``
            :param log_level: log level of the file handler, default:debug, ``str`` or ``int``
        """
        try:
            if handler_name:
                self.file_handler = logging.FileHandler(handler_name)
                self.file_handler.setLevel(log_level)
                return self.file_handler
            else:
                self.stream_handler = logging.StreamHandler()
                return self.stream_handler
        except Exception as e:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
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
            print(sys.exc_info()[2])
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
            print(sys.exc_info()[2])
            print(traceback.extract_tb(sys.exc_info()[2]))
            raise e

    def log(self, level, *msgs):
        """log the message to the logger
            :param level: log level, default: debug, ``int``
        """
        if level == logging.DEBUG or 10:
            try:
                for msg in msgs:
                    self.logger.debug(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e
        elif level == logging.INFO or 20:
            try:
                for msg in msgs:
                    self.logger.info(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e
        elif level == logging.WARNING or 30:
            try:
                for msg in msgs:
                    self.logger.warning(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e
        elif level == logging.ERROR or 40:
            try:
                for msg in msgs:
                    self.logger.error(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e
        elif level == logging.CRITICAL or 50:
            try:
                for msg in msgs:
                    self.logger.critical(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e
        else:
            try:
                for msg in msgs:
                    self.logger.exception(msg)
            except Exception as e:
                print(sys.exc_info()[0])
                print(sys.exc_info()[1])
                print(traceback.extract_tb(sys.exc_info()[2]))
                raise e


if __name__ == '__main__':
    custom_logger = Logger('LoggerUtility')
    custom_logger.set_logger_log_level(logging.ERROR)
    f_handler = custom_logger.create_handler('LoggerUtility.log', logging.ERROR)
    s_handler = custom_logger.create_handler()
    custom_logger.add_handler(f_handler)
    custom_logger.add_handler(s_handler)
    custom_logger.set_log_format(f_handler)
    custom_logger.set_log_format(s_handler)
    custom_logger.log(10, "Debug log int")
    custom_logger.log(logging.DEBUG, "Debug log str")
    custom_logger.log(20, "Info log int")
    custom_logger.log(logging.INFO, "Info log str")
    custom_logger.log(30, "warning log int")
    custom_logger.log(logging.WARNING, "warning log str")
    custom_logger.log(40, "error log int")
    custom_logger.log(logging.ERROR, "error log str")
    custom_logger.log(50, "critical log int")
    custom_logger.log(logging.CRITICAL, "critical log str")
    custom_logger.log("exception log")