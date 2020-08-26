dates_of_people = { 'Albert Einstein': '14/03/1879', 'Ada Lovelace' : '10/12/1815', 'Guido van Rossum' : '31/01/1956'}

print(
    '''
    Welcome to the birthday dictionary. We know birdth dates of:
    Albert Einstein
    Ada Lovelace
    Guido van Rossum
    What birth date you want to know?
    '''
)
input_date = str(input('Enter a name: '))

if input_date in dates_of_people:
    print(f'{input_date} birthday is {dates_of_people[input_date]}')
else:
    print(f'We dont have recors for this name: {input_date}')
