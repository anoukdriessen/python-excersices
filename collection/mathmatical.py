# mathmatical operations
# the order of running mathmetical operations: PEMDAS
# [P] parentheses       ()
# [E] exponents         **
# [M] multiplication    * & [D] devision          /
# [A] addition          + & [S] subtraction       -

a = 2
b = 10

# add
c = a + b          # same outcome as b + a
print(str(c))

# subtract
c = a - b
d = b - a
print(str(c) + " //", str(d))

# multiply
c = a * b          # same outcome as b * a
print(str(c))

# devision (result is always a float)
c = a / b
d = b / a
print(str(c) + " //", str(d))

# power of x
x = 2
c = a ** x
d = b ** x
print(str(c) + " //", str(d))

print("********************************************************************")

# round a floating point number
sum = (8 / 3)
print("without round: ", sum)
print("converted to int: ", int(sum))
print("converted to int (//): ", 8 // 3)
print("with round: ", round(sum))
print("with round (3 decimals): ", round(sum, 3))

print("********************************************************************")

# get rid of most + and convertions with the f -string
score = 0
height = 1.8
isWinning = True

# f - string
print(f"Your score is {score},\nYour height is {height},\nAre you winning? -> {isWinning}")

print("********************************************************************")

# write a program that adds the digits in a 2 digit number ( input 35 -> output 3 + 5 = 8)
two_digit_number = input("Type a two digit number ")

first = two_digit_number[0]                                                 # take the first digit
second = two_digit_number[1]                                                # take the second digit
sum = int(first) + int(second)                                              # add the first and second digit

print(first + " + " + second + " = " + str(sum))                            # print the sum as String

print("********************************************************************")

# write a program that calculates the BMI by weight and height
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# BMI is calculated by dividing a persons weight (in kg) by the square of their height (in m)
# the square is calculated l x b, in this case height * height = square of height

# convert the outcome to a whole number
#bmi = int(int(weight) / (float(height) * float(height)))
bmi = int( int(weight) / ( float(height) ** 2 ) )

print(weight + " ÷ " + "(" + height + " x " + height + ")")
print(str(bmi))

print("********************************************************************")

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# link to article -> https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many:
# - days, 
# - weeks, 
# - months 
# we have left if we live until 90 years old.

# ask user what their current age is
age = input("What is your age? ")

num_until_90 = 90 - int(age);

days_until_90 = num_until_90 * 365                  # a year has 365 days
weeks_until_90 = num_until_90 * 52                  # a year has 52 weeks
months_until_90 = num_until_90 * 12                 # a year has 12 months

# output message: You have x days, y weeks and z months left
print(f"You have {days_until_90} days, {weeks_until_90} weeks and {months_until_90} months aleft")