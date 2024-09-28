def square_and_filter_odd_even(start, end):
    # Generate list of squares in the specified range
    squares = [num ** 2 for num in range(start, end + 1)]
    
    # Separate the odd and even square values
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    
    # Print the results
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)
# Example usage
start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))
square_and_filter_odd_even(start_range, end_range)
