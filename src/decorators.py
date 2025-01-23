from functools import wraps


def log(filename = None):
    """ "декоратор, логирующий начало и конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

                result = func(*args, **kwargs)

            except Exception as error:
                error_massage = f"{func.__name__} error TypeError"
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_massage + "\n")
                else:
                    print(error_massage)
                raise
            return result

        return wrapper

    return my_decorator
