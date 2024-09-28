class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Take input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Create a Triangle object
triangle = Triangle(base, height)

# Calculate and print the area
print("The area of the triangle is:", triangle.area())
