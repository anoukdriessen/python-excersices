import pandas as pd

data = pd.read_csv("source/files/nato_phonetic_alphabet.csv")

# for (index, row) in data.iterrows():
    # print(f"{row.letter} has code {row.code}")    

alphabet = {(row.letter):(row.code) for (index, row) in data.iterrows() }
# print(alphabet)

def generate():
    word = input("Enter a word: ").upper()

    try:
        result = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")   
        generate() # run code again
    else:
        print(result)

generate()        