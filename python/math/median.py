def median(values):
  """
  Get the median of a sorted list of values

  Parameters
  ----------
  values: iterable of float
    A list of numbers

  Returns
  -------
    float
  """
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median
