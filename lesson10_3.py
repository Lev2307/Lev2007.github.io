data_of_character = {}
classes = ['pirate', 'mage', 'druid']
items = ['sword', 'staff', 'pistol', 'shield']
potions = ['health', 'mana']
name = str(input('Choose name of your character: '))
class_of_character = str(input('Choose class of your character: pirate mage druid '))
item = str(input('Choose item to take with you: sword staff pistol shield '))
potion = str(input('Choose potion to take with you: health mana '))
guess = ''

while guess != classes:
    print(f'Wrong choice, try again: {classes}')
    break