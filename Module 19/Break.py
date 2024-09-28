#Take user input
a = input ("Enter a word: ")
#program to check break keyword
for i in a: #iterate for loop
  if (i == 'A'): #condition 1
  #display result
    print ("A is found") 
    break #break statement
  else:
  #display result
    print ("A not found")


# Take user input
a = input("Enter a word: ")

# Program to check for both 'A' and 'a'
found = False  # Variable to track if any 'A' or 'a' is found

for i in a:  # Iterate through the word
    if i == 'A' or i == 'a':  # Check if it's 'A' or 'a'
        print(f"{i} is found")
        found = True

if not found:  # If no 'A' or 'a' was found
    print("No 'A' or 'a' found in the word")

