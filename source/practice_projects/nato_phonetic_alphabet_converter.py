import pandas as pd

data = pd.read_csv("source/files/nato_phonetic_alphabet.csv")

# for (index, row) in data.iterrows():
    # print(f"{row.letter} has code {row.code}")    

alphabet = {(row.letter):(row.code) for (index, row) in data.iterrows() }
print(alphabet)

word = input("Enter a word: ").upper()
result = [alphabet[letter] for letter in word]
print(result)