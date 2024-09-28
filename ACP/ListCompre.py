# Task 1: Create a list of odd numbers under the input value
user_input = int(input("Enter a number: "))
odd_numbers = [num for num in range(user_input) if num % 2 != 0]
print("List of odd numbers under", user_input, ":", odd_numbers)

# Task 2: Create a list of fruits and capitalize the first letter of each fruit
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("List of fruits with capitalized first letters:", capitalized_fruits)
