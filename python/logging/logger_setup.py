#!/usr/bin/env python3

import logging as log_tool
import os
from datetime import datetime

# Set logger config
logger_name = 'my_script_logger'
current_datetime = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
logger_output_file_name = logger_name + '_' + current_datetime + '.log'
logger_output_folder_path = os.path.join(
    os.environ.get('HOME', os.getcwd(),
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
