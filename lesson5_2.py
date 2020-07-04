number = int(input('Введите положительное число: '))
dividers = []

for i in range(number , 0, -1):
    if number % i == 0:
        dividers.append(i)
        
print(f'Делители числа {number}: {dividers}')
