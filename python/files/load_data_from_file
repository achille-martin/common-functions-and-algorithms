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


import pandas as pd
import os

def load_data_from_file(
        dataset_file_path, 
        target_header=None, 
        target_cols=None, 
        metadata_rows_to_skip=0,
        separator=None,
        ):
    """ Method for loading data from file into a pandas dataframe
    """

    data_loaded = None
    
    try:
        # Extract full file path (to resolve symlinks and relative paths)
        # and extension from inputs
        dataset_file_full_path = os.path.realpath(
            dataset_file_path
        )
        _, dataset_file_extension = os.path.splitext(
            dataset_file_full_path
        )
        dataset_file_extension_no_dot = dataset_file_extension[1:]
        
        # Read the file depending on the specified extension
        if dataset_file_extension_no_dot == 'csv':
            if separator is None:
                separator = ',' 
            data_loaded = pd.read_csv(
                dataset_file_full_path,
                header=target_header,
                usecols=target_cols, 
                skiprows=metadata_rows_to_skip,
                sep=separator,
            )
        elif dataset_file_extension_no_dot == 'asc':
            if separator is None:
                separator = '\t' 
            data_loaded = pd.read_table(
                dataset_file_full_path,
                header=target_header,
                usecols=target_cols, 
                skiprows=metadata_rows_to_skip,
                sep=separator,
            )
        else:
            raise Exception(
                f"""
                file extension {dataset_file_extension_no_dot} NOT handled
                """
            )

        return data_loaded
    
    except Exception as e:
        raise Exception(
            f"""
            EXCEPTION CAUGHT: {e}
            Cannot load data from file: {dataset_file_path}
            Full file path is: {dataset_file_full_path}
            """
        )
