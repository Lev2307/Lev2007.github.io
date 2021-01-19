from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        print("Date and time: {:%Y-%m-%d %H:%M}".format(datetime.now()))
        print(f"The name of function is : {func.__name__}")
        print(f"Function arguments: {args}")
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        print(" ")
        return result
    return wrapper

@logger
def add_one(*num):
    return sum(num) + 1

@logger
def another_func(x, y, z):
    return x * y + z

add_one(2, 4, 5)
another_func(1, 2, 3)