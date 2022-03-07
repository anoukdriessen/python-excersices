# Data Types

# String is a string of characters
myVar = "I am a String"
print("printing a string\n", type(myVar), myVar)

print("********************************************************************")

print("printing the first char from the string: ", myVar[0])                # indexes start at 0
print("printing the last char from the string: ", myVar[len(myVar) - 1])    # take the length of the string - 1


print("********************************************************************")

# integer is a whole number
myVar = 666
print("printing a integer\n", type(myVar), myVar)
# large numbers can be written with _ to make it better readable for humans
myVar = 66_66_666_99_99_999
print("printing a large integer\n", type(myVar), myVar)

print("********************************************************************")

# Float (floating point numbers)
myVar = 6.66
print("printing a float\n", type(myVar), myVar)

print("********************************************************************")

# Boolean (only two values)
# myVar = True;
myVar = False;
print("printing a boolean\n", type(myVar), myVar)

print("********************************************************************")

# converting a datatype integer to string
num_char = len(input("What's your name? \nMy name is... "))

#print("Your name has " + num_char + " characters")                         # provides an TypeError
num_char = str(num_char)                                                    # convert integer to string
print("Your name has " + num_char + " characters")                          # no more error

print("********************************************************************")
