import time
from functools import wraps

def decor_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return {
            "result": result,
            "time": end-start
        }

    return wrapper