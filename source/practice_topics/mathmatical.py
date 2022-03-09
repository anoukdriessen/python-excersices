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

print("********************************************************************")

# write a program to caculate the paint needed for a specified area
import math

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
covarage = 5 # 1 can can cover 5 square meters

paint_calc(height = test_h, width= test_w, cover=covarage)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check if this number is a prime number: "))
prime_checker(number=n)

print("********************************************************************")

# count numbers of days in month 
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
