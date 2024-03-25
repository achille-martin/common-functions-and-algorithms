def mean(values):
    """
    Get the mean of a sorted list of values
  
    Parameters
    ----------
    values: iterable of float
        A list of numbers
  
    Returns
    -------
      float
    """
    
    mean = sum(values) / len(values)
    
    return mean
