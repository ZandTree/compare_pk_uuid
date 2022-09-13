import time
from functools import wraps
from django.db import connection, reset_queries


def calc_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # "Func {func.__name__} start working")
        reset_queries()
        start_queries = len(connection.queries)
        start_float = time.perf_counter()
        func(*args, **kwargs)
        end_float = time.perf_counter()
        end_queries = len(connection.queries)
        work_time_float = end_float - start_float
        return f"Took: {work_time_float} sec; queries qty: {end_queries-start_queries} done"

    return wrapper
