first_list = [1,2,5,7]
second_list = [0]
third_list = [3,2]
first_list[3]
second_list[0]
third_list[1]

if first_list[-1] % 2 == 0: #Получить последнее число из списка нужно использовать [-1] индекс
    print(f'Последнее число {first_list[-1]} - чётное ')
else:
     print(f'Последнее число {first_list[-1]} - Нечётное ')
if second_list[-1] % 2 == 0:
    print(f'Последнее число {second_list[-1]} - чётное ')
else:
     print(f'Последнее число {second_list[-1]} - Нечётное ')    
if third_list[-1] % 2 == 0:
    print(f'Последнее число {third_list[-1]} - чётное ')
else:
     print(f'Последнее число {third_list[-1]} - Нечётное ')
