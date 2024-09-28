def calculator():
    # Input numbers and operation
    num1 = float(input("Enter first number: "))
    operation = input("Choose operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform the calculation based on the chosen operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation."

    return f"Result: {result}"

# Run the calculator
print(calculator())
