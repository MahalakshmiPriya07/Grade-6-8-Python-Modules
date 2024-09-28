def split_list(numbers):
    mid = len(numbers) // 2
    return numbers[:mid], numbers[mid:]

# Static list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Split the list
first_half, second_half = split_list(numbers)

# Print the results
print("First half:", first_half)
print("Second half:", second_half)
