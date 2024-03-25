#!/usr/bin/env python3

from mean import mean
import math

def standard_deviation(values, type='population'):
    """
    Get the standard deviation of a sorted list of values
  
    Parameters
    ----------
    values: iterable of float
        A list of numbers
    
    type: string
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
    if type == 'population':
        denominator = nb_values
    elif type == 'sample':
        denominator = nb_values - 1
    else:
        raise Exception(f"Type {type} NOT handled yet")
    
    standard_deviation = math.sqrt(deviation_sum/denominator)
    
    return standard_deviation
