#!/usr/bin/env python3

# MIT License

# Copyright (c) 2024 Achille MARTIN

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

# Code heavily inspired from:
# https://stackoverflow.com/questions/75734160/convert-dictionary-keys-with-dotted-names-to-nested-dictionaries
# by Masklinn

def convert_dotted_dict_to_std_dict(input_dict):
    """
    Convert a dict with dotted keys (e.g. my_key.my_sub_key = '')
    into a standard dict (e.g. my_key: {my_sub_key: ''})
  
    Parameters
    ----------
    input_dict: dict
        Dictionary to convert
  
    Returns
    -------
    dict
        Dictionary converted
    """
    
    output_dict = {}
    for key, value in input_dict.items():
        current_dict = output_dict
        *keys, leaf = key.split('.')
        for k in keys:
            current_dict = current_dict.setdefault(k, {})
        current_dict[leaf] = value
    
    return output_dict

# Application example:
# Input dictionary
# >>> {'key_1.key_11': 'value_11', 'key_1.key_12': 'value_12', 'key_2': 'value_2'}
# Output dictionary
# >>> {'key_1': {'key_11': 'value_11', 'key_12': 'value_12'}, 'key_2': 'value_2'}
