from random import randint
def build_template_input():
        """
        output: return str, built-in input() function
        """
        return int(input('Введите размер поля: '))

def build_field(size):
    field_size = ['_'] * size # Создаем ряд на поле
    field = [] # Создаем пустое поле
    for _ in range(size):
        field.append(field_size[:]) # Добавляем нужное количество рядов в нашем полe

    return field # Возвращаем сгенерированное поле

def move_player(direction, field):
    if direction == 'right':
        for row in range(len(field)):
            for col in range(len(field)):
                if field[row][col] == 'x':
                    field[row][col] = '_'
                    field[row][col+1] = 'x' 
                    break
    if direction == 'left':
        for row in range(len(field)):
            for col in range(len(field)):
                if field[row][col] == 'x':
                    field[row][col] = '_'
                    field[row][col-1] = 'x' 
                    break

    if direction == 'up':
        for row in range(len(field)):
            for col in range(len(field)):
                if field[row][col] == 'x':
                    field[row][col] = '_'
                    field[row-1][col] = 'x' 
                    break
    if direction == 'down':
        for row in range(len(field)):
            for col in range(len(field)):
                if field[row][col] == 'x':
                    field[row][col] = '_'
                    field[row+1][col] = 'x' 
                    return field
    return field

def add_obstacles(field):
    chance = 55
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] != 'x':
                r_number = randint(1, 100)
                if r_number <= chance:
                    field[row][col] = 'o'
                    break
    return field

def blocked_obstacle(direction):
    print(f'Oops... Move to {direction} is blocked!')
    
def check_obstacle(direction, field, position):
    x, y = position
    status = True
    if 'direction' == 'up':


def game():
   
    size_of_template = build_template_input()
    field = add_obstacles(build_field(size_of_template))

    field[0][0] = 'x'
    [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
    
    gameStatus = True
    while gameStatus:
        user_direction = input('\nВыберите одно из направлений: up right down left или exit для выхода ')

        field = move_player(user_direction, field)


        if user_direction == 'exit':
            gameStatus = False

        [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля

game()
