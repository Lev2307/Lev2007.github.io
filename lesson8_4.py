def build_template_input():
        """
        output: return str, built-in input() function
        """
        return int(input('Введите размер поля: '))

def build_field(size):
        field_size = ['_'] * size # Создаем ряд на поле
        field = [] # Создаем пустое поле

        print(f'Пустое поле до добавления в него рядов {field}\n')
        for _ in range(size):
            field.append(field_size[:]) # Добавляем нужное количество рядов в нашем поле
        print(f'Поле после добавления в него рядов')
        [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
        return field # Возвращаем сгенерированное поле

def move_player(direction, field):
    if direction == 'right':
        for row in range(len(field)):
            for col in range(len(field)):
                if field[row][col] == 'x':
                    field[row][col] = '_'
                    field[row][col+1] = 'x' 
                    break
    return field

def game():
    gameStatus = True

    size_of_template = build_template_input()
    field = build_field(size_of_template)

    print(f'\nДобавляем стартовую локацию')
    field[0][0] = 'x'
    [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля

    user_direction = input('\nВведите направление: ')

    field = move_player(user_direction, field)
    print(f'\nПоле после движения направо')
    [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
        
game()
