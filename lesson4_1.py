user_input = int(input('Введите первое число: '))
user_input2 = int(input('Введите второе число: '))
result = user_input + user_input2
result2 = user_input * user_input2
if result < 1000:
    print(f'Сумма {user_input} и {user_input2} = {result}')
else:
    print (f'Произведение {user_input} и {user_input2} = {result2}')
    
