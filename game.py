from random import choice

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

    def get_quality(self):
        return self.name
    
potion1 = Potion('potion1', 50)
potion2 = Potion('apple', 50)
print(potion1 + potion2)