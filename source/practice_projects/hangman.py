import random as r
from turtle import right
# welcome
print("Welcome to hangman")
isWon = False

words = ["banaan","appel","wortel","paprika","meloen", "citroen"]
# print(r.choice(words)) # chose a random word
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# print(f"stages {len(stages)}")

def playRound():
    # generate a random word
    thisWord = r.choice(words)

    # generate as many blanks as letters in word
    guessedWord = []
    for _ in range(len(thisWord)):
        guessedWord.append("_")

    print(thisWord, guessedWord)
    guessed = False
    gameover = False

    count = 1
    lives = 6

    while not gameover and not guessed:
        # ask the user to guess a letter
        current_guess = input("Guess a letter... ").lower()

        for position in range(len(thisWord)):
            letter = thisWord[position]
            if current_guess == letter:
                # the letter is in the word
                guessedWord[position] = letter

        if current_guess not in thisWord:
            lives -= 1
            if lives == 0:
                gameover = True
                print("LOST!")
    
        print(f"Round [{count}] {guessedWord}")
        # check if the user has won
        message = "you've"

        if "_" not in guessedWord:
            # all blanks filled
            guessed = True
            message += " WON!"
        else:
            count += 1

        print(stages[lives])     


    print(f"{message}")

playRound()                    