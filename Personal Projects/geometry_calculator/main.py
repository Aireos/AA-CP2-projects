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


"""Class Implementation:
Create separate classes for different shapes: Circle, Rectangle, and Triangle
Implement a Square class as a subclass of Rectangle Include appropriate attributes for each shape (e.g., radius, length, width, base, height)
Shape Calculations:
Implement methods to calculate area and perimeter for each shape
Create a method to display all information about a shape Include a static method in each class to explain the formulas used
User Interface:
Design a text-based menu for interacting with the calculator
Allow users to create multiple shapes and switch between them
Include options to perform various calculations on the selected shape
Validation and Error Handling:
Implement input validation to ensure positive values for dimensions Handle potential errors (e.g., division by zero, invalid input types)
Shape Comparisons:
Create methods to compare two shapes (e.g., has_larger_area(), has_longer_perimeter())
Implement a feature to sort multiple shapes based on a chosen property (area or perimeter)
Bonus are only available to projects submitted on time that meet ALL of the minimum requirements.

BONUS:
3D Shape Extension 

Design and implement classes for 3D shapes (3 points)
Create methods for volume and surface area calculations (4 points)
Extend the user interface to incorporate 3D shape options (5 points)
Graphical Shape Visualization

Implement basic shape drawing functionality (3 points)
Scale drawings appropriately based on shape dimensions (4 points)
Add labels and measurements to the visual representations (5 points)
Shape Transformation Calculator

(Create functionality to calculate how shapes change when scaled, rotated, or translated. Include methods to determine new coordinates or dimensions after transformations.)

Implement scaling transformations for all shapes (3 points)
Add rotation calculations for applicable shapes (4 points)
Create methods for translation and coordinate shifts (5 points)
SUBMISSION:
Submit a link to your completed project on GitHub in properly structured folders.

NOTES:
Ensure your program uses proper mathematical formulas for all calculations
Comment your code to explain the purpose of each method and any complex logic
Use appropriate naming conventions for classes, methods, and variables
Round results to a reasonable number of decimal places for readability
Consider the user experience when designing your text-based interface
Test your program thoroughly to ensure all calculations are accurate"""