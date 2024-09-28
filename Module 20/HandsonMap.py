# Function to square a number
def square(x):
    return x ** 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map to apply the square function to each number
squared_numbers = list(map(square, numbers))

# Print the original and squared numbers
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
