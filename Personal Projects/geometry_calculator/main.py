#Alex Anderson, Geometry Calculator

# Shape classes (unchanged from the previous implementations)
class Circle:
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None

    def area(self):
        if self.radius:
            return round(3.14159 * self.radius ** 2, 2)
        return None

    def perimeter(self):
        if self.radius:
            return round(2 * 3.14159 * self.radius, 2)
        return None

    def formula(self):
        return "Area: π * radius^2, Perimeter: 2 * π * radius"

    def display_info(self):
        if self.radius:
            return f"Circle: Radius = {self.radius}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Radius must be positive"


class Rectangle:
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None

    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None

    def perimeter(self):
        if self.length and self.width:
            return round(2 * (self.length + self.width), 2)
        return None

    def formula(self):
        return "Area: length * width, Perimeter: 2 * (length + width)"

    def display_info(self):
        if self.length and self.width:
            return f"Rectangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Length and width must be positive"


class Square:
    def __init__(self, side):
        self.length = side if side > 0 else None
        self.width = side if side > 0 else None

    def area(self):
        if self.length and self.width:
            return round(self.length * self.width, 2)
        return None

    def perimeter(self):
        if self.length and self.width:
            return round(4 * self.length, 2)
        return None

    def formula(self):
        return "Area: side^2, Perimeter: 4 * side"

    def display_info(self):
        if self.length and self.width:
            return f"Square: Side = {self.length}, Area = {self.area()}, Perimeter = {self.perimeter()}"
        return "Side length must be positive"


class Triangle:
    def __init__(self, length, width):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None

    def area(self):
        if self.length and self.width:
            return round(0.5 * self.length * self.width, 2)
        return None

    def formula(self):
        return "Area: 0.5 * length * width"

    def display_info(self):
        if self.length and self.width:
            return f"Triangle: Length = {self.length}, Width = {self.width}, Area = {self.area()}"
        return "Length and width must be positive"


# 3d shape classes
class Sphere:
    def __init__(self, radius):
        self.radius = radius if radius > 0 else None

    def volume(self):
        if self.radius:
            return round((4 / 3) * 3.14159 * self.radius ** 3, 2)
        return None

    def surface_area(self):
        if self.radius:
            return round(4 * 3.14159 * self.radius ** 2, 2)
        return None

    def formula(self):
        return "Volume: (4/3) * π * radius^3, Surface Area: 4 * π * radius^2"

    def display_info(self):
        if self.radius:
            return f"Sphere: Radius = {self.radius}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Radius must be positive"


class Cube:
    def __init__(self, side):
        self.side = side if side > 0 else None

    def volume(self):
        if self.side:
            return round(self.side ** 3, 2)
        return None

    def surface_area(self):
        if self.side:
            return round(6 * (self.side ** 2), 2)
        return None

    def formula(self):
        return "Volume: side^3, Surface Area: 6 * side^2"

    def display_info(self):
        if self.side:
            return f"Cube: Side = {self.side}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Side length must be positive"


class Cuboid:
    def __init__(self, length, width, height):
        self.length = length if length > 0 else None
        self.width = width if width > 0 else None
        self.height = height if height > 0 else None

    def volume(self):
        if self.length and self.width and self.height:
            return round(self.length * self.width * self.height, 2)
        return None

    def surface_area(self):
        if self.length and self.width and self.height:
            return round(2 * (self.length * self.width + self.length * self.height + self.width * self.height), 2)
        return None

    def formula(self):
        return "Volume: length * width * height, Surface Area: 2 * (lw + lh + wh)"

    def display_info(self):
        if self.length and self.width and self.height:
            return f"Cuboid: Length = {self.length}, Width = {self.width}, Height = {self.height}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Dimensions must be positive"


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius if radius > 0 else None
        self.height = height if height > 0 else None

    def volume(self):
        if self.radius and self.height:
            return round(3.14159 * self.radius ** 2 * self.height, 2)
        return None

    def surface_area(self):
        if self.radius and self.height:
            return round(2 * 3.14159 * self.radius * (self.radius + self.height), 2)
        return None

    def formula(self):
        return "Volume: π * radius^2 * height, Surface Area: 2 * π * radius * (radius + height)"

    def display_info(self):
        if self.radius and self.height:
            return f"Cylinder: Radius = {self.radius}, Height = {self.height}, Volume = {self.volume()}, Surface Area = {self.surface_area()}"
        return "Radius and height must be positive"


# User Interface
def main():
    print("\nGeometry Calculator:")
    shapes = []
    
    while True:
        try:
            print("\n1. Create a Circle")
            print("2. Create a Rectangle")
            print("3. Create a Square")
            print("4. Create a Triangle")
            print("5. Create a Sphere")
            print("6. Create a Cube")
            print("7. Create a Cuboid")
            print("8. Create a Cylinder")
            print("9. View All Shapes")
            print("10. Compare Shapes")
            print("11. View Shape Formulas")
            print("12. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                radius = float(input("Enter the radius of the circle: "))
                shapes.append(Circle(radius))

            elif choice == "2":
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                shapes.append(Rectangle(length, width))

            elif choice == "3":
                side = float(input("Enter the side length of the square: "))
                shapes.append(Square(side))

            elif choice == "4":
                length = float(input("Enter the length of the triangle: "))
                width = float(input("Enter the width of the triangle: "))
                shapes.append(Triangle(length, width))

            elif choice == "5":
                radius = float(input("Enter the radius of the sphere: "))
                shapes.append(Sphere(radius))

            elif choice == "6":
                side = float(input("Enter the side length of the cube: "))
                shapes.append(Cube(side))

            elif choice == "7":
                length = float(input("Enter the length of the cuboid: "))
                width = float(input("Enter the width of the cuboid: "))
                height = float(input("Enter the height of the cuboid: "))
                shapes.append(Cuboid(length, width, height))

            elif choice == "8":
                radius = float(input("Enter the radius of the cylinder: "))
                height = float(input("Enter the height of the cylinder: "))
                shapes.append(Cylinder(radius, height))

            elif choice == "9":
                if not shapes:
                    print("No shapes created yet")
                else:
                    for i, shape in enumerate(shapes, 1):
                        print(f"{i}. {shape.display_info()}")

            elif choice == "10":
                if len(shapes) < 2:
                    print("At least two shapes are needed to compare")
                else:
                    idx1 = int(input("Enter the number of the first shape: ")) - 1
                    idx2 = int(input("Enter the number of the second shape: ")) - 1
                    shape1 = shapes[idx1]
                    shape2 = shapes[idx2]

                    print("\nComparison Results:")
                    try:
                        if shape1.area() and shape2.area():
                            if shape1.area() > shape2.area():
                                print("Shape 1 has a larger area")
                            elif shape1.area() < shape2.area():
                                print("Shape 2 has a larger area")
                            else:
                                print("Both shapes have the same area")
                    except:
                        pass

                    try:
                        if shape1.perimeter() and shape2.perimeter():
                            if shape1.perimeter() > shape2.perimeter():
                                print("Shape 1 has a longer perimeter")
                            elif shape1.perimeter() < shape2.perimeter():
                                print("Shape 2 has a longer perimeter")
                            else:
                                print("Both shapes have the same perimeter")
                    except:
                        pass

                    try:
                        if shape1.volume() and shape2.volume():
                            if shape1.volume() > shape2.volume():
                                print("Shape 1 has a larger volume")
                            elif shape1.volume() < shape2.volume():
                                print("Shape 2 has a larger volume")
                            else:
                                print("Both shapes have the same volume")
                    except:
                        pass

            elif choice == "11":
                print("\nShape Formulas:")
                print("1. Circle: " + Circle(1).formula())
                print("2. Rectangle: " + Rectangle(1, 1).formula())
                print("3. Square: " + Square(1).formula())
                print("4. Triangle: " + Triangle(1, 1).formula())
                print("5. Sphere: " + Sphere(1).formula())
                print("6. Cube: " + Cube(1).formula())
                print("7. Cuboid: " + Cuboid(1, 1, 1).formula())
                print("8. Cylinder: " + Cylinder(1, 1).formula())

            elif choice == "12":
                print("Goodbye")
                break

            else:
                print("Invalid input")
        except:
            print("Invalid input")


# runs the program
main()