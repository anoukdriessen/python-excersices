import random as r

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[r.randint(0, len(names) -1 )]} is going to buy the meal today!")    
