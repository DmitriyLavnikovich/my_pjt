import functools

from pyexpat.errors import messages


def log(filename=None):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, 'a') as file:
                    file.write(message + '\n')
            else:
                print(message)

            return result
        return wrapper
    return my_decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)