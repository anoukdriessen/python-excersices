print("Welcome to the PyPassword Generator")

# ask the user the number of letters
amountOfLetters = input("How many letters would you like in your password?\n")
amountOfSymbols = input("How many symbols would you like in your password?\n")
amountOfNumbers = input("How many numbers would you like in your password?\n")

# show user choices
print(f"You chose {amountOfLetters} letter(s), {amountOfSymbols} symbol(s) and {amountOfNumbers} number(s)")

# generate password
generatedPassword = "supersafe"

# show result
print(f"Here is your password: {generatedPassword}")