import random
obs_percent = 50
def build_template_input():
        """
        output: return str, built-in input() function
        """
        return int(input('Введите размер поля: '))

def build_field(size):
    '''
    input: u - user_input_field(int)
    output: template
    '''
    field_size = ['_'] * size 
    field = [] 

    for _ in range(size):
        field.append(field_size[:])

    user_number = size
    x_pol = []
    for _ in range(user_number):
        chance = (2, 5, 7)
        for _ in range(user_number):
            rand_int = random.randrange(10)
            if rand_int in chance:
                    x_pol.append(['o'])
            else:
                    x_pol.append(['_']) 
    return field

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

def game():
   
    size_of_template = build_template_input()
    field = build_field(size_of_template)

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
