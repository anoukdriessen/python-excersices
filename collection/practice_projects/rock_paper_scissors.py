from threading import Timer
import time
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
print("Welcome to the Rock Paper Scissors Game")

def playRound(user_chose):
    print("3")
    time.sleep(0.7)
    print("2")
    time.sleep(0.7)
    print("1")
    time.sleep(0.7)
    print("May the odds be forever in your favor...")
    time.sleep(0.7)
    return user_chose

def play():
    user_chose = 0
    pc_chose = 0

    # welcome
    print("What do you choose?\n Type [0] for Rock, [1] for Paper, OR [2] for Scissors")
    isWon = False

    while not isWon:
        # store the user's input
        valid_choice = False
        while not valid_choice:
            user_chose = int(input("I choose: "))
            if user_chose < 3:
                user_chose = True
            else:
                print("Invalid choice: Type [0] for Rock, [1] for Paper, OR [2] for Scissors")
                user_chose = False   

        # wish user good luck
        playRound(user_chose)
        # get random for pc
        pc_chose = random.randint(0, 2)

        # display result
        print(f"user_chose {user_chose}")
        print(f"pc_chose {pc_chose}")

    # winning conditions
    # Rock wins from Scissors
    # Paper wins from Rock
    # Scissors wins from Paper

    if user_chose == pc_chose:
        # game is a tie
        print()


t = Timer(5, play())
t.start()

t.cancel()
