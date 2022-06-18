import time

# Context manager
@contextlib.contextmanager
def execution_timer():
  """
  Time the execution of a context block.
  
  Yields
  ------
    None
  """
  start = time.time()
  yield
  end = time.time()
  print('Elapsed: ' + str(round(end - start), 2) + 's')

# Usage
# with execution_timer():
#   print('This should take approximately 0.25 seconds')
#   time.sleep(0.25)
