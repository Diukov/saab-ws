class Shape:
    """Base class for geometric shapes."""

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 ** 0.5 / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side



"""
Refactor the code to eliminate duplication by creating a base class
from which other classes inherit common methods.
"""
