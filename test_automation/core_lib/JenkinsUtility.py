"""Module for jenkins operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import logging
import os
import sys
import jenkins
import xml.etree.ElementTree as ET

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
from core_lib.Logger import *


def convert_xml_file_to_str(path_to_config_file):
    """
    :param path_to_config_file: Path to config.xml, ''path''
    :return: string format of xml, ''str''
    """
    try:
        tree = ET.parse(path_to_config_file)
        root = tree.getroot()
        return ET.tostring(root, encoding=UTF_ENCODING, method=XML).decode()
    except Exception as e:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print(traceback.extract_tb(sys.exc_info()[2]))
        raise e


class JenkinsUtility:

    def __init__(self, url, username, password, timeout=DEFAULT_TIMEOUT):
        """Create handle to Jenkins instance.
            :param url: URL of Jenkins server, ``str``
            :param username: Server username, ``str``
            :param password: Server password, ``str``
            :param timeout: Server connection timeout in secs (default: 30), ``int``
        """
        self.url = url
        self.username = username
        self.password = password
        logger_name = os.path.basename(__file__).split('.')[0]
        handler_name = os.path.basename(__file__).replace(PY_FILE_EXT, LOG_FILE_EXT)
        self.jenkins_logger= Logger(logger_name=logger_name, handler_name=handler_name)

        # Instantiating Jenkins Server
        try:
            self.server = jenkins.Jenkins\
                (url=self.url,
                 username=self.username,
                 password=self.password,
                 timeout=timeout)
            self.user = self.server.get_whoami()
            self.version = self.server.get_version()
            self.jenkins_logger.info('Hello %s from Jenkins %s' % (self.user['fullName'], self.version))
        except BaseException:
            self.jenkins_logger.error(sys.exc_info()[0],
                                      sys.exc_info()[1],
                                      traceback.extract_tb(sys.exc_info()[2]))
            self.jenkins_logger.exception(traceback.extract_tb(sys.exc_info()[2]))
            raise

    def create_job(self, job_name, config_filename, jobs_config_dir=None):
        """:param job_name: Name of the Job which needs to be created, ``str``
           :param config_filename: None of the job's config.xml file, ``str``
           :param jobs_config_dir: Jenkins Jobs config files dir(default: jenkins_config), ``str``
        """
        if jobs_config_dir is None:
            jobs_config_dir = (os.path.join
                                   (os.path.abspath
                                    (os.path.join
                                     (os.path.dirname
                                      (os.path.abspath(__file__)), os.pardir)),
                                    CONFIG_DIR, JENKINS_CONFIG_STR))
            try:
                if not os.path.exists(jobs_config_dir):
                    os.mkdir(jobs_config_dir)
            except BaseException:
                self.jenkins_logger.error(sys.exc_info()[0],
                                          sys.exc_info()[1],
                                          traceback.extract_tb(sys.exc_info()[2]))
                self.jenkins_logger.exception(traceback.extract_tb(sys.exc_info()[2]))
                raise

        # Creating a new Jenkins Job
        try:
            jenkins_job_config_file = os.path.join(jobs_config_dir, config_filename)
            config_file_str = convert_xml_file_to_str(jenkins_job_config_file)
            self.server.create_job(job_name, config_xml=config_file_str)
        except BaseException:
            self.jenkins_logger.error(sys.exc_info()[0],
                                      sys.exc_info()[1],
                                      traceback.extract_tb(sys.exc_info()[2]))
            self.jenkins_logger.exception(traceback.extract_tb(sys.exc_info()[2]))
            raise


if __name__ == '__main__':
    jenkins_obj = JenkinsUtility("http://192.168.1.11:8080/", "santosh", "Ginni@18")
    # jenkins_obj.create_job("Daily_Build-FileCompareTool", "Daily_Build-FileCompareTool_config.xml")
    # jenkins_obj.create_job("Hourly_Build-FileCompareTool", "Hourly_Build-FileCompareTool_config.xml")
    # jenkins_obj.create_job("Periodic_Build-FileCompareTool", "Periodic_Build-FileCompareTool_config.xml")