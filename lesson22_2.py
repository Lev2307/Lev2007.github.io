from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):
        print("Date and time: {:%Y-%m-%d %H:%M}".format(datetime.now()))
        print(f"The name of function is : {func.__name__}")
        print(f"Function arguments: {args}")
        result = func(*args, **kwargs)
        print(f'Result: {result}')
        print(" ")

        f = open('text.txt', 'w+')
        f.write("Date and time: {:%Y-%m-%d %H:%M} \n".format(datetime.now()))
        f.write(f"The name of function is : {func.__name__} \n")
        f.write(f"Function arguments: {args} \n")
        f.write(f"Result: {result} \n")
        f.write("\n")
        f.close()

        f = open('text.txt', 'a')
        f.write("Date and time: {:%Y-%m-%d %H:%M} \n".format(datetime.now()))
        f.write(f"The name of function is : add_one \n")
        f.write(f"Function arguments: (2, 4, 5) \n")
        f.write("Result: 12")
        f.close()

        return result
    return wrapper

@logger
def another_func(x, y, z):
    return x * y + z


@logger
def add_one(*num):
    return sum(num) + 1

add_one(2, 4, 5)
another_func(1, 2, 3)


