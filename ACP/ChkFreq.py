# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user for the value to check
value_to_check = int(input("Enter the value to check its frequency: "))

# Calculate frequency of the value
frequency = list(test_dict.values()).count(value_to_check)

# Print the frequency
print(f"The frequency of the value {value_to_check} is: {frequency}")
