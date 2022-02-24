import random as r      # python has a random module

print(r.randint(1,10))  # random integer between a / b
print(r.random())       # random float between 0 and 1

print(r.random() * 5)   # random float number between 0 and 4.999...

# write a program to toss a virtual coin
# it will randomly tell the user Heads or Tails

side = r.randint(0,1)
if side == 1:
    print("Heads")
else:
    print("Tails")  

# write a program to decide who is going to pay the bill
# ask the user for all the names and store the values in a list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[r.randint(0, len(names) -1 )]} is going to buy the meal today!")    
