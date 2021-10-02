""" Generic Logger class which can be implemented by any module for logging"""

import logging


class Logger:

    def __init__(self, logger_name, level=logging.DEBUG):
        """Create new logger.
            :param logger_name: name of new logger, ``str``
        """
        try:
            self.file_handler = None
            self.stream_handler = None
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(level)
        except Exception as e:
            raise RuntimeError("Unable to create logger") from e

    def create_file_handler(self, file_handler_name):
        """Create file handler.
            :param file_handler_name: name of new file handler, ``str``
        """
        try:
            self.file_handler = logging.FileHandler(file_handler_name)
        except Exception as e:
            raise RuntimeError("Unable to create file handler") from e

    def add_file_handler(self):
        """add file handler to the logger.
            :param file_handler_name: name of file handler, ``str``
        """
        try:
            self.logger.addHandler(self.file_handler)
        except Exception as e:
            raise RuntimeError("Unable to add file handler") from e

    def create_stream_handler(self):
        """Create stream handler.
        """
        try:
            self.stream_handler = logging.StreamHandler()
        except Exception as e:
            raise RuntimeError("Unable to create stream handler") from e

    def add_stream_handler(self):
        """add file handler to the logger.
        """
        try:
            self.logger.addHandler(self.stream_handler)
        except Exception as e:
            raise RuntimeError("Unable to add stream handler") from e

    def set_log_format(self, handler):
        """set the log format of the handler
            :param handler: name of the handler, ``obj``
        """
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
        try:
            handler.setFormatter(formatter)
        except Exception as e:
            raise RuntimeError("Unable to set log format") from e

    def set_log_level_to_handler(self, level=logging.DEBUG):
        """set the log format of the handler
            :param handler: name of the handler, default: None, ``obj``
            :param level: log level, default: debug, ``int``
        """
        try:
            self.file_handler.setLevel(level=logging.ERROR)
        except Exception as e:
            raise RuntimeError("Unable to set log level") from e


if __name__ == '__main__':
    custom_logger = Logger('JenkinsUtility')
    file_handler = custom_logger.create_file_handler('JenkinsUtility.log')
    custom_logger.set_log_format(file_handler)
    custom_logger.add_file_handler()
    custom_logger.create_stream_handler()
    stream_handler = custom_logger.create_stream_handler()
    custom_logger.add_stream_handler()
