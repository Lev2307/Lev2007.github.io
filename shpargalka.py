# LISTS
my_list = ['apple', 'cheese', 'strawberry']

fruit = 'apple' in my_list
print(fruit)

len(my_list)

my_list.reverse()
print(my_list)

sorted_list = sorted(my_list)

my_list.sort(key=lambda x: x[-1])
print(my_list)

my_list.append('mango')

my_list.insert(5, 'cherry')
print(my_list)

my_list.remove('apple')

my_list.pop(0)

my_list.clear()


# List Comprehensions

comp_list = [i for i in range(5)]
print(comp_list)

double_list = [i * 2 for i in range(5)]
print(double_list)

# TUPLES
my_tuple = 'apple', 'banana', 'orange'
my_tuple = ('apple', 'banana', 'orange')
my_tuple = tuple('apple')

my_tuple.count('p')

my_tuple.index('p')

my_tuple = 'Mike', 'Moscow', 'Teacher'
name, city, proffesion = my_tuple
print(name)
print(city)
print(proffesion)

# Unpacking *advanced
my_tuple = (1, 2, 3, 4, 5, 6)
first, *rest, last = my_tuple
print(first)
print(rest)
print(last)

*any_first, prev, last = my_tuple
print(my_tuple)
print(prev)
print(last)

foo = 'abcd'
f, *m, l = foo
print(f, m, l)
bar = {'first key': 1, 'second_key': 2}
f, l = bar
print(f, l)


# DICTIONARY
my_dict = {'key_1': 1, 'key_2': 2}

my_dict = dict(key_1=1, key_2=2)

value = my_dict['key_1']

my_dict['new_key'] = 3

del my_dict['key_1']

removed_value = my_dict.pop('key_2')

last_value = my_dict.popitem()

for k in my_dict.keys():
    print(k)

for v in my_dict.values():
    print(v)

for k, v in my_dict.items():
    print(k, v)

# Важно есть связанность у делимых объектов

my_list = [1, 2, 3]

other_list = my_list

other_list[0] = 4
print(my_list[0])

other_dict = my_dict

other_dict['key_1'] = 4
print(my_dict['key_1'])

# COPY
my_list = [1, 2, 3]
other_list = my_list.copy()
other_list = list(my_list)

other_list[0] = 4
print(my_list[0])

my_dict = {'key_1': 1, 'key_2': 2}
other_dict = my_dict.copy()
other_dict = dict(my_dict)

other_dict['key_1'] = 4
print(my_dict['key_1'])

# SETS
my_set = {1, 2, 3, 4}

my_set = set([1, 2, 3, 4])

my_set = {1, 1, 2, 2}
print(my_set)

unique = set('arnold')
print(unique)

my_set = {1, 2}

my_set.add(3)
print(my_set)

my_set = {1, 2, 3, 4}

my_set.remove(3)
print(my_set)

my_set.discard(3)
my_set.discard(2)
print(my_set)

removed_data = my_set.pop()
print(removed_data)

my_set.clear()
print(my_set)

my_set = {1, 2, 3}

for i in my_set:
    print(i)

evens = {2, 8, 10}
odds = {1, 3, 7}
primes = {2, 3, 5}

union = evens.union(odds)
print(union)

intersection = evens.intersection(primes)
print(intersection)

# STRINGS

my_string = ' Hello world! '
print(my_string)

no_spaces = my_string.strip()
print(no_spaces)

to_list = my_string.split()
print(to_list)

upper = my_string.upper()
lower = my_string.lower()

first_string = 'Hello world'
second_string = 'Display beautiful'

collection = [first_string, second_string]

for i in collection:
    print(i.rjust(20, '#'))


some_float = 12.45676
my_string_format = f'String data: {second_string} -- number data: {some_float:.2f}'
print(my_string_format)

some_list = [('banana', 5), ('potato', 2), ('tomato', 10)]
for veg,price in some_list:
    print(f'name: {veg:<10} price: {price:03d} $')

# Время на данный момент
from datetime import datetime
today = "Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now())
print(today)

string = 'Hello world'

string.startswith('Hello')
string.endswith('world')

string.find('ell') # return 1
string.count('l') # return 3

replaced = string.replace('Hello', 'Bye Bye')
print(replaced)

some_iterable = ['a', 'b', 'c']

my_str = ''.join(some_iterable)
print(my_str)

# LAMBDA Functions

my_lambda = lambda x: x + 5

print(my_lambda(5))

# та же самая функция
def my_lambda(x):
    return x + 5

# Lambdas

my_lambd = lambda x, y: x + y
print(my_lambd(5, 2))

unsorted_list = [(10, -100), (5, 43), (1000, 97846)]

sorted_list = sorted(unsorted_list, key=lambda x: x[0])
print(sorted_list)

sorted_list = sorted(unsorted_list, key=lambda x: x[1])
print(sorted_list)

my_st = '12345'

to_list_of_ints = list(map(lambda x: int(x), my_st))
print(to_list_of_ints)

my_list = [1, 2, 3 , 5, 4, '6']

converted_list = list(map(lambda x: int(x), my_list))
print(converted_list)

filter_list = list(filter(lambda x: type(x) is str, my_list))
print(filter_list)

from functools import reduce
m_list = [1, 2, 3, 4, 5, 6]

reduced_list = reduce(lambda x, y: x + y, m_list)
print(reduced_list)

w_list = ['w', 'o', 'r', 'l', 'd']
reduce_list = reduce(lambda x, y: x + y, w_list)
print(reduce_list)

# Generation of spiski

only_evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(only_evens)

some_value = False
my_ternary = 10 if some_value else 20

print(my_ternary)

cub = [i for i in range(100) if i ** 3 % 3 == 0]
print(cub)

# args and kwards
def my_func(a, b, *args, **kwards):
    print(a, b)
    print(args)
    print(kwards)

my_func(1, 2, 3, 4, 5, foo=6, bar=7)

def func(a, d, b):
    print(a, d, b)

some_dict = {'a': 1, 'd': 2, 'b': 3}
func(**some_dict)

Декораторы

def decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

@decorator
def print_name():
    print('Mike')

print_name()

def square_decorator(func):
    def wrapper(*args, **kwards):
        result = func(*args, **kwards)
        return result * result
    return wrapper


@square_decorator
def add_some(x):
    return x + 5

print(add_some(20))

def repeater(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwards):
            for _ in range(times):
                result = func(*args, **kwards)
            return result
        return wrapper
    return decorator_repeat

@repeater(times=3)
def say_hello():
    print('Hello')

say_hello()

def check_permission(func):
    def wrapper(*args, **kwards):
        arg = args[0]
        user = args[1]
        if user == 'admin':
            return func(arg, user)
        else:
            return 'Denied'
    return wrapper

@check_permission
def extraordinary_func(argument, user):
    return argument + 10 if user else argument - 10

user = 'admin'
print(extraordinary_func(10, user))


count = 0
def counter(func):
    def wrapper(*args, **kwargs):
        global count
        result = func(*args, **kwargs)
        count += 1
        print(count)
        return result
    return wrapper

@counter
def some_func():
    print('Hello')

some_func()
some_func()
some_func()
some_func()


# Модули и генераторы

from collections import Counter 

my_string = 'aaabbbbcccccdddsds'

my_counter = Counter(my_string)
print(my_counter)

print(my_counter.most_common(1))
print(tuple(my_counter.elements()))

from collections import namedtuple

Some_class = namedtuple('Name', 'a, b')

foo = Some_class(1, 2)

print(foo)
print(foo.a, foo.b)

def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
first = next(gen)
print(first)

def timer(n):
    print('Starting generator...')
    while n > 0:
        yield n
        n -= 1

count = timer(3)

print(next(count))

import json

my_dict = {"class": "Mage", "level": 5, "items": ["sword", "potion"]}

with open('converted.json', 'w') as f:
    json.dump(my_dict, f, indent=4)

to_json = json.dumps(my_dict, indent=4)
print(to_json)

with open('converted.json', 'r') as f:
    python_data = json.load(f)
    print(python_data)

