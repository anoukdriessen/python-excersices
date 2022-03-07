# a condition is a choice: IF some condition -> do this OTHERWISE do this
# in python we have a IF / ELSE statement

isItRaining = False
isItSnowing = True

if isItRaining:
    # do this if it is raining
    print("make sure to bring an umberella")
elif not isItRaining and isItSnowing:
    # do this is it is not raining but is snowing
    print("do you wanna build a snowman?")
else:
    # do this
    print("there is no rain and it is not snowing")

# comparison operators

# a > b     is a greater than b
# a < b     is a less than b
# a >= b    is a greater than or equal to b
# a <= b    is a less then or equal to b
# a == b    is a is equal to
# a != b    is a is not equal to


# write a program that works out whether a given number is an odd or even number
number = int(input("What number do you choose?"))

if number % 2 == 0:
    # number is even
    print(f"{number} is an EVEN number")
else:
    # number is odd
    print(f"{number} is an ODD number")


# write an bmi converter with information based on the outcome
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

# BMI is calculated by dividing a persons weight (in kg) by the square of their height (in m)
# the square is calculated l x b, in this case height * height = square of height

# convert the outcome to a whole number
#bmi = int(int(weight) / (float(height) * float(height)))
bmi = round( weight / ( height ** 2 ) )

if bmi < 18.5:
    print(f"Your BMI is: {bmi}, you are underweight.")
else:
    if bmi < 25:
        print(f"Your BMI is: {bmi}, you have a normal weight.")
    else:
        if bmi < 30:
            print(f"Your BMI is: {bmi}, you are slightly overweight.")
        else:
            if bmi < 35:
                print(f"Your BMI is: {bmi}, you are obese.")
            else:
                print(f"Your BMI is: {bmi}, you are clinically obese.")


# write a program that works out whether a given year is a leap year
year = int(input("What year do we need to check?"))
# a leap year occures on every year that is evenly divisible by 4
isLeapYear = False

if year % 4 == 0:
    # year is divisible by 4 -> Leap year!
    if year % 100 != 0:
        # year is not divisible by 100 -> Leap year!
        isLeapYear = True
    else:    
        # year is divisible by 100 -> Not a Leap year!
        if year % 400 == 0:
            # year is divisible by 400 -> Leap year!
            isLeapYear= True

if isLeapYear:
    print("Leap year.")
else:
    print("Not leap year.")    


# write a program to automate a pizza order
price_small = 15
price_medium = 20
price_large = 25

price_pepperoni = 2
price_pepperoni_extra = 3

price_cheese = 1

print("Welcome to Python Pizza Deliveries!")
# ask the user what kind of pizza they would like to order
size = input("What size pizza do you want? S, M, or L ")
# ask the user if they want to add some veggie pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N ")
# ask the user if they want to add extra cheese
extra_cheese = input("Do you want extra cheese? Y or N ")

wantsPepperoni = add_pepperoni == "Y"
wantsCheese = extra_cheese == "Y"

total = 0
# the size of the pizza
if size == "S":
    # small pizza
    total += price_small
    if wantsPepperoni:
        total += price_pepperoni 
elif size == "M":
    # medium pizza
    total += price_medium
    if wantsPepperoni:
        total += price_pepperoni_extra
else:
    # large pizza
    total += price_large
    if wantsPepperoni:
        total += price_pepperoni_extra

if wantsCheese:
    total +=  price_cheese

print(f"Your final bill is: ${total}")    


# write a program that tests the compatibility between two peoples
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# convert both name's to lowercase
name1 = name1.lower()
name2 = name2.lower()

# take both people's name and check for the number of thimes the letters in the word TRUE occurs
count_true_name = name1.count("t")
count_true_name += name1.count("r")
count_true_name += name1.count("u")
count_true_name += name1.count("e")
count_true_name += name2.count("t")
count_true_name += name2.count("r")
count_true_name += name2.count("u")
count_true_name += name2.count("e")

count_love_name = name1.count("l")
count_love_name += name1.count("o")
count_love_name += name1.count("v")
count_love_name += name1.count("e")
count_love_name += name2.count("l")
count_love_name += name2.count("o")
count_love_name += name2.count("v")
count_love_name += name2.count("e")

result = str(count_true_name) + str(count_love_name)
#print(result)
result = int(result)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}")        