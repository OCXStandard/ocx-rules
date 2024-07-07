#  Copyright (c) 2024. OCX Consortium https://3docx.org. See the LICENSE

import os
import sys

from loguru import logger

# To make sure that the tests import the modules this has to come before the import statements
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

logger.disable("ocx_rules")
