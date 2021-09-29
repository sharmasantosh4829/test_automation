"""Class file for jenkins operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import os.path
import sys
import traceback
import jenkins
import xml.etree.ElementTree as ET


def convert_xml_file_to_str(path_to_config_file):
    tree = ET.parse(path_to_config_file)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8', method='xml').decode()


class JenkinsUtility:

    def __init__(self, url, username, password, timeout=30):
        '''Create handle to Jenkins instance.
            :param url: URL of Jenkins server, ``str``
            :param username: Server username, ``str``
            :param password: Server password, ``str``
            :param timeout: Server connection timeout in secs (default: 30), ``int``
        '''

        self.url = url
        self.username = username
        self.password = password
        self.timeout = timeout
        try:
            self.server = jenkins.Jenkins\
                (url=self.url,
                 username=self.username,
                 password=self.password,
                 timeout=self.timeout)
            self.user = self.server.get_whoami()
            self.version = self.server.get_version()
            print('Hello %s from Jenkins %s' % (self.user['fullName'], self.version))
        except jenkins.JenkinsException:
            print("Unable to connect. "
                  "\nPlease check username, password and  make sure  jenkins server is running.")

    def create_job(self, job_name, config_filename, jobs_config_dir=None):
        if jobs_config_dir is None:
            jobs_config_dir = (os.path.join
                                   (os.path.abspath
                                    (os.path.join
                                     (os.path.dirname
                                      (os.path.abspath(__file__)), os.pardir)), "config", "jenkins_config"))
            try:
                if not os.path.exists(jobs_config_dir):
                    os.mkdir(jobs_config_dir)
            except:
                print(str(sys.exc_info()[0]))
                print(str(sys.exc_info()[1]))
                print(str(traceback.extract_tb(sys.exc_info()[2])))
                raise
        try:
            jenkins_job_config_file = os.path.join(jobs_config_dir, config_filename)
            config_file_str = convert_xml_file_to_str(jenkins_job_config_file)
            self.server.create_job(job_name, config_xml=config_file_str)
        except jenkins.JenkinsException:
            print("Unable to create new job. "
                  "\nPlease check the config file")


if __name__ == '__main__':
    jenkins_obj = JenkinsUtility("", "", "")
    jenkins_obj.create_job("Daily_Build-FileCompareTool", "Daily_Build-FileCompareTool_config.xml")
    jenkins_obj.create_job("Hourly_Build-FileCompareTool", "Hourly_Build-FileCompareTool_config.xml")
    jenkins_obj.create_job("Periodic_Build-FileCompareTool", "Periodic_Build-FileCompareTool_config.xml")