import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")

# ask the user the number of letters
amountOfLetters = int(input("How many letters would you like in your password?\n"))
amountOfSymbols = int(input("How many symbols would you like in your password?\n"))
amountOfNumbers = int(input("How many numbers would you like in your password?\n"))

# show user choices
print(f"You chose {amountOfLetters} letter(s), {amountOfSymbols} symbol(s) and {amountOfNumbers} number(s)")
length = amountOfLetters + amountOfSymbols + amountOfNumbers

# generate password
generatedPassword = []
for number in range(0, length):
    if amountOfLetters is not 0:
        # letter = letters[r.randint(0, len(letters)-1)]
        generatedPassword += r.choice(letters)
        amountOfLetters -= 1
    elif amountOfNumbers is not 0:
        # number = numbers[r.randint(0, len(numbers)-1)]
        generatedPassword += r.choice(numbers)
        amountOfNumbers -= 1
    elif amountOfSymbols is not 0:
        # symbol = symbols[r.randint(0, len(symbols)-1)]
        generatedPassword += r.choice(symbols)
        amountOfSymbols -= 1

password = ""
r.shuffle(generatedPassword) # shuffle items in list
for item in generatedPassword:
    password += item

# show result
print(f"Here is your password: {password}")