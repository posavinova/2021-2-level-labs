"""
Programming 2021
Seminar 8
Introduction into the OOP
"""

# Possible attributes for the 'Dog' class:
    ## height
    ## colour
    ## weight
    ## breed
    ## age
    ## name


class Dog:
    def __init__(self, name, breed, age, weight, height, favourite_food, colour='white'):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.height = height
        self.colour = colour
        self.favourite_food = favourite_food

    def bark(self):
        print(f'Bark, Bark, I am {self.name}')

    def run_to(self, place):
        print(f'{self.name} runs to {place}')

    def change_name(self, new_name):
        self.name = new_name

    def describe(self):
        print(self.name)
        print(self.age)
        print(self.breed)

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.breed}, {self.height}'


dog1 = Dog('Rex', 'Pug', 5, 4, 50, 'meat', 'beige')
print(dog1)
dog1.describe()

dog2 = Dog('Joe', 'Husky', 5, 7, 70, 'meat')
