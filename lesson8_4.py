from random import randint

obs_percent = 50
def build_template_input():
        """
        output: return str, built-in input() function
        """
        return int(input('Введите размер поля: '))

def build_field(size):
        field_size = ['_'] * size # Создаем ряд на поле
        field = [] # Создаем пустое поле

        for _ in range(size):
            field.append(field_size[:]) # Добавляем нужное количество рядов в нашем поле
        # print(f'Поле после добавления в него рядов')
        # [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
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


def build_obstacles(field1, field):
    for row in range(len(field)):
        for col in range(len(field)):
            if field1 < 5:
                field[row][col] = 'o'
                
    return field
def game():
   
    size_of_template = build_template_input()
    field = build_field(size_of_template)

    field1 = randint(0, 100)
    field[0][0] = 'x'
    [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
    
    gameStatus = True
    while gameStatus:
        user_direction = input('\nВыберите одно из направлений: up right down left или exit для выхода ')

        field = obstacles(field1, field)
        field = move_player(user_direction, field)
            
        if user_direction == 'exit':
            gameStatus = False
        [print(row) for row in field] # Эту часть можешь удалить как поймешь процесс отрисовки поля
game()
