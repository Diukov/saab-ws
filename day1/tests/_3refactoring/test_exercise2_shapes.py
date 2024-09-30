import unittest
from day1._3refactoring.exercise2_shapes import Circle, Square, EquilateralTriangle

class TestShapes(unittest.TestCase):
    def test_circle(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), 78.5398, places=4)
        self.assertAlmostEqual(circle.perimeter(), 31.4159, places=4)

    def test_square(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)
        self.assertEqual(square.perimeter(), 16)

    def test_triangle(self):
        triangle = EquilateralTriangle(6)
        self.assertAlmostEqual(triangle.area(), 15.5885, places=4)
        self.assertEqual(triangle.perimeter(), 18)

if __name__ == '__main__':
    unittest.main()
