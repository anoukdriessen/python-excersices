# welcome message tip calculator
print("Welcome to the tip calculator")

# ask the user what the total bill was
total = float(input("What was the total bill? $"))

# ask the user what % of tip we should use
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 of 15? "))
# calculate percentages = multiply a number by the percentage number devided by 100

# ask how many people are splitting the bill
num_of_people = int(input("How many people to split the bill? "))

# each person should pay ( total / num of people ) * tip%
#calc_with_tip = percentage_tip / 100 * total + total
calc_with_tip = total * (1 + percentage_tip / 100)

bill_per_person = calc_with_tip / num_of_people
# sum = round( (bill_per_person) , 2)
sum = "{:.2f}".format(bill_per_person)

# output
print(f"each person should pay: ${sum}")