"""
Rectangle Class: Create a Rectangle class with width and height attributes, and methods to calculate area, perimeter, and whether it's a square.
"""

class Rectangle:
    def __init__(self, _width, _height):
        self._width = _width
        self._height = _height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width + self._height) * 2

    def is_square(self):
        return self._width == self._height

shape = Rectangle(3, 5)

print(shape.area())
print(shape.perimeter())
print(shape.is_square())

shape.width = 4
shape.height = 4

print(shape.area())
print(shape.perimeter())
print(shape.is_square())

