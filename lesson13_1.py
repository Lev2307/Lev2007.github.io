from random import randint
class Potion():
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'This potion name: {self.name}'

    def __add__(self, other):
        self_len = len(self.name) 
        other_len = len(other.name)
        new_name = self.name[:self_len] + other.name[other_len:]
        new_quality = (self.quality + other.quality) // 2
        return Potion(new_name, new_quality)

        def check_quality(self):
            if self.quality > 75:
                print('Potion is very good')
            elif self.quality > 50:
                print('Potion is average')
            else:
                print('Potion has bad quality')

    def get_quality(self):
         return self.quality

    def get_name(self):
        return self.name


def QualityPotion(Potion):
    def special(self):
        return qualityPotion(self.name, self.quality + 20)

def notQualityPotion(Potion):
    def special(self):
        return notQualityPotion(self.name, self.quality - 20)

gamestatus = True
potions = {}

while True:
    potion_q_n = (input('What potion do you want to make? q - for quality, n - for non quality: ')).lower()
    if potion_q_n == 'exit':
        gamestatus = False
    else:
        potion_name = str(input('Enter potion name: '))
        potion_quality = randint(1, 100)

    if potion_q_n == 'q':
        new_potion = QualityPotion(potion_name, potion_quality)
    else:
        new_potion = notQualityPotion(potion_name, potion_quality)
        potions[potion_name] = new_potion
    
if len(potions) >= 2:
    action = input(f'Add(+) or Subtract(-) your potions? ').lower()
    potion1 = potions.popitem()[1]
    potion2 = potions.popitem()[1]
    if action == '+':
        mixed_potion = potion1 + potion2
    else:
        mixed_potion = potion1 - potion2

print('Start mixin potions...')
if mixed_potion.get_quality() < 30:
    print('Kaboom! Potion exploded! You die...')
    gamestatus = False
else:
    potions[mixed_potion.get_name()] = mixed_potion
    print(f'Your potions: {potions.keys()}')
    print(f'Potion quality: {mixed_potion.get_quality()}, Be careful next time!')