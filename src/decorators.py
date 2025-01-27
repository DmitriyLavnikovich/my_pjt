from functools import wraps

from pyexpat.errors import messages


# def log(filename = None):
#     """ "декоратор, логирующий начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""
#
#     def my_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 if filename:
#                     with open(filename, "a") as file:
#                         file.write(f"{func.__name__} ok\n")
#                 else:
#                     print(f"{func.__name__} ok")
#
#                 result = func(*args, **kwargs)
#
#             except Exception as error:
#                 error_massage = f"{func.__name__} error TypeError"
#                 if filename:
#                     with open(filename, "a") as file:
#                         file.write(error_massage + "\n")
#                 else:
#                     print(error_massage)
#                 raise
#             return result
#
#         return wrapper
#
#     return my_decorator

def log(filename = None):
    """ "декоратор, логирующий начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} ok")
            except Exception as e:
                error_massage = f"{func.__name__} error TypeError"
                print(error_massage)
                raise
            return result
        if filename:
            try:
                with open(filename, "a") as file:
                    file.write(f"{func.__name__} ok\n")
            except:
                error_massage = f"{func.__name__} error TypeError"
                with open(filename, "a") as file:
                    file.write(error_massage + "\n")
        return wrapper

    return my_decorator
