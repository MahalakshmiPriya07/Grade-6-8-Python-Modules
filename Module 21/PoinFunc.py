import math

class Point:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    def distance_to(self, other):
        """Calculate the distance to another point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def display(self):
        """Display the coordinates of the point."""
        print(f"Point coordinates: ({self.x}, {self.y})")

# Main program
if __name__ == "__main__":
    # Create two points
    point1 = Point(3, 4)
    point2 = Point(6, 8)

    # Display the coordinates of the points
    point1.display()
    point2.display()

    # Calculate and print the distance between the two points
    distance = point1.distance_to(point2)
    print(f"Distance between point1 and point2: {distance:.2f}")
