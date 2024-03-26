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

import time
from functools import wraps

def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print the execution time of the decorated function."""
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print(
            '{func_name} took {exec_time}s'.format(
                func_name=func.__name__, 
                exec_time=round(t_total, 2),
            )
        )
        return result
    return wrapper

# Usage
# @execution_timer
# def <func_to_evaluate>(<args>):
#     <your function code>
