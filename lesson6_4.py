l_and_o = (
    ('Я вода и по воде я плаваю. Хто я?', 'льдина'),
    ('Все меня топчут, a я - всё лучше', 'тропа'),
    ('Хто я?', 'хто я')
    )

def riddle(l,o):
    return l.lower() == o.lower()

print('Отгадайте 3 загадки')
first = 1

for l in l_and_o:
    print(f'{first} - загадка')
    print(f'{l[0]}')
    user_input = input('Ваш ответ: ')

    if riddle (l[1], user_input):
        print('Угадал')
    else:
        print('Неа')

    first += 1
