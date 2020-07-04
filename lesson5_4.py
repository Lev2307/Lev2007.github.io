print('''Попробуй отгадать загадку
- Кто может поднять и передвинуть и коня, и слона? ''')
answer_of_the_riddle = 'Шахматист'
answer = str(input('Ответ: '))
reply = 'сдаюсь'
while answer == answer_of_the_riddle:
     print('Это правильный ответ! ')
     break
else:
   
    print('Ответ неверный, попробуй ещё! Если не хочешь то напиши - сдаюсь ')



give_up = str(input('Ответ: '))
    
if  give_up == reply:
    print('Правильный ответ - Шахматист ')        

