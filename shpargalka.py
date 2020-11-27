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