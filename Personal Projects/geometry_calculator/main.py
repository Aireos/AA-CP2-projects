#Alex Anderson, Geometry Calculator

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2  # Using an approximation for π

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square with side {self.length}"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"

# Example usage
circle = Circle(radius=5)
triangle = Triangle(base=10, height=8)
rectangle = Rectangle(length=4, width=6)
square = Square(side=4)

print(circle)          # Circle with radius 5
print("Area:", circle.area())  # Area: 78.53975
print("Perimeter:", circle.perimeter())  # Perimeter: 31.4159

print(triangle)        # Triangle with base 10 and height 8
print("Area:", triangle.area())  # Area: 40.0

print(rectangle)       # Rectangle with length 4 and width 6
print("Area:", rectangle.area())  # Area: 24.0
print("Perimeter:", rectangle.perimeter())  # Perimeter: 20

print(square)          # Square with side 4
print("Area:", square.area())  # Area: 16.0
print("Perimeter:", square.perimeter())  # Perimeter: 16