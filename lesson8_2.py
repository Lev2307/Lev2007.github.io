def build_pyramid(r):
    for i in range(r // 2):
        print('*' * (i + 1))

    for i in range((r // 2) + 1,0,-1):
        print('*' * (i))

user_input = int(input('Введите число: '))

if user_input % 2 == 0:
    print('Введите нечётное число')
else:
    build_pyramid(user_input)

