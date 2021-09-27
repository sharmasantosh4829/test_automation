"""Class file for jenkins operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import jenkins


class JenkinsUtility:

    def __init__(self, url, username, password):
        try:
            self.server = jenkins.Jenkins(url=url, username=username, password=password)
            self.user = self.server.get_whoami()
            self.version = self.server.get_version()
            print('Hello %s from Jenkins %s' % (self.user['fullName'], self.version))
        except jenkins.JenkinsException:
            print("Unable to connect. "
                  "\nPlease check username, password and  make sure  jenkins server is running.")


if __name__ == '__main__':
    jenkins_obj = JenkinsUtility("", "", "")