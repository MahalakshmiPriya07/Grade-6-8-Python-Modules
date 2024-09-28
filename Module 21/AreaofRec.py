# Define a function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Input values for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and display the result
area = area_of_rectangle(length, width)
print(f"The area of the rectangle is: {area}")
