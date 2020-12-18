my_list = [8, 2, 0]

my_list.sorted(my_list, key=lambda x: x[-1])
print(my_list)


# def flip(d, a):
#     return a.sorted(key=lambda x: x[d])


# assert flip('L', [1, 4, 5, 3, 5]) == [5, 5, 4, 3, 1]
# assert flip('R', [3, 2, 1, 2]) == [1, 2, 2, 3]