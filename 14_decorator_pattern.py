"""
Decorator Pattern: Write a decorator function that measures and prints the execution time of any function it decorates.
"""

from time import time
from functools import wraps

def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{end - start:.2f} seconds")
        return result

    return wrapper

@record_time
def recorded_func(n=35):
    return slow_function(n)

def slow_function(n=35):
    """A deliberately slow function that calculates Fibonacci numbers recursively.
    This will take a few seconds to execute with n=35."""
    if n <= 1:
        return n
    return slow_function(n-1) + slow_function(n-2)

result = recorded_func()
print(f"Result: {result}")
