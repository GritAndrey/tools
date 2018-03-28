import functools
import json
def to_json(func):
    """This decorator converts the return value of the function to JSON format"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped
