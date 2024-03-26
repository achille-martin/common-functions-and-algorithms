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

from mean import mean
import math

def standard_deviation(values, dataset_type='population'):
    """
    Get the standard deviation of a sorted list of values
  
    Parameters
    ----------
    values: iterable of float
        A list of numbers
    
    dataset_type: string
        Type of dataset
        'population' for whole population dataset
        'sample' for sample of population dataset

    Returns
    -------
    float
        Standard deviation of values
    """

    calculated_mean = mean(values)
    
    deviation_sum = sum([(i - calculated_mean)**2 for i in values])
    
    nb_values = len(values)
    denominator = None
    if dataset_type == 'population':
        denominator = nb_values
    elif dataset_type == 'sample':
        denominator = nb_values - 1
    else:
        raise Exception(f"Dataset type {dataset_type} NOT handled yet")
    
    standard_deviation = math.sqrt(deviation_sum/denominator)
    
    return standard_deviation
