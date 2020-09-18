class Player():
    def attack(self):
        print(f'{self.name} attacks')

class Barbarian(Player):
    def __init__(self,name):
        self.name = name
        self._class = 'barbarian'

class Mage(Player):
    def __init__(self,name):
        self.name = name
        self._class = 'mage'

barbarian_name = input('Your barbarian name: ')
mage_name = input('Your mage name: ')

barb = Barbarian(barbarian_name)
mage = Mage(mage_name)

