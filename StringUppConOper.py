#Congratulation of message
x="congratulations"
print("\n", str.upper(x))

#String Reverse Operation
#input a word
text = str(input("Enter a string: "))

# Reverse String 
# using step value as -1 to iterate in reverse
revText = text[::-1] 
text = revText

print("Reverse of Given String is:")
print(text)


#String Concatenation
# Take two strings as input from user
print("Enter the First Name: ")
strOne = input()

print("Enter the Second Name: ")
strTwo = input()

# Concatenate the two strings
# Using Addition Operator
strThree = strOne + strTwo
print("\nConcatenated Name is: ", strThree)