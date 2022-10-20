'''

    wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)    #  black wolf, 4 legs
print(sheep1)    #  white sheep, 4 legs
print(sheep2)    #  white sheep, 4 legs
print(snake)    #   brown snake, 0 legs
print(parrot)    #  black parrot, 2 legs

c1 = Cage(1)   # ID numbers
c1.add_animals(wolf, sheep1, sheep2)
print(c1)

#    Cage 1:
# 1 black wolf, 4 legs
# 2 white sheep, 4 legs
# 3 white sheep, 4 legs

c2 = Cage(2)
c2.add_animals(snake, parrot)
print(c2)

#    Cage 2:
# 1 brown snake, 0 legs
# 2 black parrot, 2 legs

z = Zoo()
z.add_cages(c1, c2)
print(z)

#     Cage 1:
# 1 black wolf, 4 legs
# 2 white sheep, 4 legs
# 3 white sheep, 4 legs
#     Cage 2:
# 1 brown snake, 0 legs
# 2 black parrot, 2 legs

print(z.animals_by_color('black'))
# 1 black wolf, 4 legs
# 2 black parrot, 2 legs

print(z.number_of_legs())
#     14

'''


from numpy import outer


class Animal:
    def __init__(self, color, legs):
        self.animal = self.__class__.__name__
        self.color = color
        self.legs = legs

    def __repr__(self):
        return f"{self.color} {self.animal}, {self.legs} legs"


class Wolf(Animal):
    def __init__(self, color, legs=4):
        super().__init__(color, legs)


class Sheep(Animal):
    def __init__(self, color, legs=4):
        super().__init__(color, legs)


class Snake(Animal):
    def __init__(self, color, legs=0):
        super().__init__(color, legs)


class Parrot(Animal):
    def __init__(self, color, legs=2):
        super().__init__(color, legs)


wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)
print(sheep1)
print(sheep2)
print(snake)
print(parrot)


class Cage:
    def __init__(self, id):
        self.id = id
        self.animals = list()

    def __repr__(self):
        output = f"Cage {self.id}:\n"
        output += f"\n".join(f"\t{index} {animal}" for index, animal
                             in enumerate(self.animals, 1))

        return output

    def add_animals(self, *args):
        self.animals += args


c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print(c1)

c2 = Cage(2)
c2.add_animals(snake, parrot)
print(c2)


class Zoo:
    def __init__(self):
        self.cages = list()

    def __repr__(self):
        output = f"\n".join(f"{cage}" for cage in self.cages)

        return output

    def add_cages(self, *args):
        self.cages += args

    def animals_by_color(self, color):
        color_animals = [animal for cage in self.cages
                         for animal in cage.animals
                         if animal.color == color.lower()]

        output = f"\n".join(f"{animal}" for animal in color_animals)

        return output

    def number_of_legs(self):
        number_of_legs = 0
        number_of_legs += sum([animal.legs for cage in self.cages
                               for animal in cage.animals])
        return number_of_legs


z = Zoo()
z.add_cages(c1, c2)
print(z)

print(z.animals_by_color('black'))
print(z.number_of_legs())
