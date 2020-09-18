class Plant():
    def grow(self):
        print(f'{self.name} is growing!')

    def plant(self):
        print(f'Plant a {self.name} ')

class Fruit(Plant):
    def feed(self):
        self.feed_status += 1
        if self.feed_status >= 5:
            self.feed_status = 0
            self.grow()
        else:
            print(f'{5 - self.feed_status} times to feed remain!')

class Apple(Fruit):
    def __init__(self,name):
        self.name = name
        self.feed_status = 0


golden_apple = Apple('Golden Apple')

golden_apple.plant()
for _ in range(5):
    golden_apple.feed()

#     Получим
# Plant a Golden Apple 
# 4 times to feed remain!
# 3 times to feed remain!
# 2 times to feed remain!
# 1 times to feed remain!
# Golden Apple is growing!