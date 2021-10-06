"""Generic file to keep all the constants at one place"""

import logging

# ***Dir Names *** #
ARCHIVE_DIR= "archive"
ARTIFACTS_DIR= "artifacts"
CONFIG_DIR= "config"
CONSTANTS_DIR= "constants"
CORE_LIB_DIR= "core_lib"
DATA_DIR= "data"
LIB_DIR= "lib"
LOGS_DIR= "logs"
PROJECTS_DIR= "projects"
REPORT_DIR= "report"
TEMP_DIR= "temp"

# *** Logging Constants *** #
debug=logging.DEBUG=10
info=logging.INFO=20
warning=logging.WARNING=30
error=logging.ERROR=40
critical=logging.CRITICAL=50
log_format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'

# *** File Extensions *** #
PY_FILE_EXT= ".py"
LOG_FILE_EXT= ".log"

# *** File Encoding *** #
UTF_ENCODING='utf8'
XML='xml'

# *** Timeouts *** #
DEFAULT_TIMEOUT=30

# *** Jenkins Constants *** #
JENKINS_CONFIG_STR= 'jenkins_config'

