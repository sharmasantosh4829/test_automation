"""Module for Config files operations"""

__author__ = "Santosh Sharma"
__credits__ = "Santosh Sharma"
__version__ = "1.0.1"
__maintainer__ = "Santosh Sharma"
__email__ = "ss10011987@gmail.com"
__status__ = "Development"

# system imports
import configparser
import os.path


class ConfigParserUtility:

    def __init__(self):
        # Instantiating Config Parser
        try:
            self.config = configparser.ConfigParser()
        except configparser.Error as e:
            raise RuntimeError("Unable to initialize ConfigParser") from e

    def create_conf_file(self, config_file):
        """Create handle to ConfigParser instance.
            :param config_file: new config file to be created, ``str``, default: None
        """
        try:
            if not os.path.exists(config_file):
                with open(config_file, "w") as file:
                    file.write("\n")
            else:
                raise RuntimeError("Unable")
        except configparser.Error as e:
            raise RuntimeError("Unable to create new config file") from e


if __name__ == '__main__':
    config_parser_obj = ConfigParserUtility()
    config_parser_obj.create_conf_file("")