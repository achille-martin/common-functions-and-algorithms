#!/usr/bin/env python3

# MIT License

# Copyright (c) 2023-2024 Achille MARTIN

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging as log_tool
import os
from datetime import datetime

# Set logger config
logger_name = 'my_script_logger'
current_datetime = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
logger_output_file_name = logger_name + '_' + current_datetime + '.log'
logger_output_folder_path = os.path.join(
    os.environ.get(
        'HOME', 
        os.getcwd()
    ),
    'log',
)
logger_output_prefix_format = "[%(asctime)s] [%(levelname)s] - %(message)s"
logger_logging_level = "DEBUG"

# Instantiate logger object
try:
    os.makedirs(logger_output_folder_path, exist_ok=True)
    logger = log_tool.getLogger(__name__)
    logger.setLevel(logger_logging_level)
    logger_output_file_path = os.path.join(
        logger_output_folder_path, 
        logger_output_file_name,
    )
    file_handler = log_tool.FileHandler(logger_output_file_path)
    formatter = log_tool.Formatter(logger_output_prefix_format)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
except Exception as e:
    raise Exception(
        f"""
        Cannot instantiate logger {logger_name}
        EXCEPTION CAUGHT: {e}
        """
    )


if __name__ == "__main__":
    logger.info("Script started")
    logger.info("Script terminated")
