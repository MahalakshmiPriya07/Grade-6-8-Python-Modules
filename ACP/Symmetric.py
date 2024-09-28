# Function to find symmetric difference
def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example A
set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}
symmetric_diff_a = find_symmetric_difference(set1_a, set2_a)
print("Symmetric difference for Set A:", symmetric_diff_a)

# Example B
set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}
symmetric_diff_b = find_symmetric_difference(set1_b, set2_b)
print("Symmetric difference for Set B:", symmetric_diff_b)
