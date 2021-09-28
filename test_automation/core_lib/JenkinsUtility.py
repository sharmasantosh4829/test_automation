"""Class file for jenkins operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import jenkins
import xml.etree.ElementTree as ET

def convert_xml_file_to_str(path_to_config_file):
    tree = ET.parse(path_to_config_file)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8', method='xml').decode()


class JenkinsUtility:

    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url
        try:
            self.server = jenkins.Jenkins(url=self.url, username=self.username, password=self.password)
            self.user = self.server.get_whoami()
            self.version = self.server.get_version()
            print('Hello %s from Jenkins %s' % (self.user['fullName'], self.version))
        except jenkins.JenkinsException:
            print("Unable to connect. "
                  "\nPlease check username, password and  make sure  jenkins server is running.")

    # def create_job(self, job_name):
    #     try:
    #         self.server.create_job()


if __name__ == '__main__':
    jenkins_obj = JenkinsUtility("http://192.168.1.11:8080", "santosh", "Ginni@18")