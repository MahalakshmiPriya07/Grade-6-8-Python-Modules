def calculate_average(tup):
    return sum(tup) / len(tup)

# Example tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the averages
average1 = calculate_average(tup1)
average2 = calculate_average(tup2)

print("Average of tup1:", average1)
print("Average of tup2:", average2)
