from functools import wraps

def save_options(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)


        return result
    return wrapper
