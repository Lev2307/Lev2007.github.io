#я не знаю как эту ошибку исправить =/
def palindrome(string):
    if string == string[::-1]:
        return True
    return False

user_input - input('Введи слово мб это палиндром')

if palindrome(user_input):
    print(f'Это {user_input} - палиндром')
else:
    print('НЕ ПОВЕЗЛО')
