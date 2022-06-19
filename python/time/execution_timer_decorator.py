import time
from functools import wraps

def execution_timer(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    t_start = time.time()
    result = func(*args, **kwargs)
    t_total = time.time() - t_start
    print('{func_name} took {exec_time}s'.format(
      func_name=func.__name__, 
      exec_time=round(t_total, 2)
    ))
    return result
  return wrapper

# Usage
# @execution_timer
# def <func_to_evaluate>(<args>):
# # your function code
