#!/usr/bin/env python3

def range_min_max(values):
    """
    Get the range of a sorted list of values
  
    Parameters
    ----------
    values: iterable of float
        A list of numbers
  
    Returns
    -------
    (float, float)
        Min of values, Max of values
    """
    
    minimum_value = min(values)
    maximum_value = max(values)

    return (minimum_value, maximum_value)
