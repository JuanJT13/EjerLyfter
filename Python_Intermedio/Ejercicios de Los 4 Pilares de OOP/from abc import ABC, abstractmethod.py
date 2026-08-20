from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height





    # Herencia múltiple:
# Sirve para que una clase herede atributos o métodos
# de dos o más clases al mismo tiempo.

class Flyer:
    def fly(self):
        print("I can fly")


class Swimmer:
    def swim(self):
        print("I can swim")


class Duck(Flyer, Swimmer):
    pass