# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f'Cat: {self.name}'

# fluffy = Cat('Fluffy')

# print(fluffy)

# class Foo():
#     def __init__(self,number):
#         self.number = number

#     def __str__(self):
#         return f'Cat: {self.number}'

#     def __add__(self,other):
#         result = self.number + other.number
#         return Foo(result)

# a = Foo(1)
# b = Foo(1)

# c = a + b
# print(c)

class Fraction():
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    
    def __str__(self):
        return f'{self.numer} / {self.denom}'
    
    def __add__(self, other):
        new_numer = self.numer * other.denom + self.numer * other.denom
        new_denom = self.denom * self.denom
        return Fraction(new_numer, new_denom)

    def __sub__(self,other):
        new_numer = self.numer * other.denom - self.numer * other.denom
        new_denom = self.denom * self.denom
        return Fraction(new_numer, new_denom)

    def convert(self):
        return self.numer / self.denom
    def get_number(self):
        return self.number

    def set_number(self):
        return self.denom


oneHalf = Fraction(1,2)
secondHalf = Fraction(2, 3)
print(oneHalf + secondHalf)
print(oneHalf.convert())