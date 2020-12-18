from functools import reduce

def summation(num):
    return reduce(lambda x, y: x+y, range (num + 1))

assert summation(1) == 1
assert summation(8) == 36
assert summation(22) == 253
assert summation(100) == 5050
assert summation(213) == 22791