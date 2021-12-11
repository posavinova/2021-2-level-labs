# Vehicle
    # Attributes:
        # max_speed
        # colour
    # Methods:
        # move

class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour

    def move(self):
        print('I am moving.')


# Car
    # Attribute:
        # max_speed
        # colour
        # fuel
    # Methods:
        # move
        # stay


class Car(Vehicle):
    def __init__(self, fuel, max_speed, colour):
        self.fuel = fuel
        super().__init__(max_speed, colour)

    def move(self):
        print(f'Car is moving at {self.max_speed}.')


lada = Car('gasoline', 120, 'yellow')


# Bicycle
    # Attributes:
        # number_of_wheels
        # colour
        # max_speed
    # Methods:
        # move
        # freestyle

class Bicycle(Vehicle):
    def __init__(self, colour, max_speed, number_of_wheels):
        super().__init__(max_speed, colour)
        self.number_of_wheels = number_of_wheels
        self.__number_of_passengers = 1

    def freestyle(self):
        print('I am freestyling.')


stels = Bicycle('yellow', 30, 2)
print(stels.colour)
stels.move()
stels.freestyle()
