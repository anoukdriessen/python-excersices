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

def getIcon(nr):
    if nr == 0:
        # rock
        return rock
    elif nr == 1:
        # paper
        return paper
    elif nr == 2:
        return scissors   

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
                valid_choice = True
            else:
                print("Invalid choice: Type [0] for Rock, [1] for Paper, OR [2] for Scissors")
                user_chose = False   

        # wish user good luck
        playRound(user_chose)
        # get random for pc
        pc_chose = random.randint(0, 2)

        # display result
        # print(f"user_chose {user_chose}")
        # print(f"pc_chose {pc_chose}")

        # winning conditions
        # Rock wins from Scissors
        # Paper wins from Rock
        # Scissors wins from Paper
        print(f"YOU:\t{getIcon(user_chose)}\nPC:\t{getIcon(pc_chose)}")

        if user_chose == pc_chose:
            # game is a tie
            print('Game is a TIE, play again.')
        elif user_chose == 0:
            # player has chosen rock
            if pc_chose == 2:
                # pc chose scissors -> player wins
                print('You WON')
            else:
                print('You LOST')
        elif user_chose == 1:
            # player has chosen paper
            if pc_chose == 0:
                # pc chose rock -> player wins
                print('You WON')
            else:
                print('You LOST')
        elif user_chose == 2:
            # player has chosen scissors 
            if pc_chose == 1:
                # pc chose paper -> player wins
                print('You WON')
            else:
                print('You LOST')  

        print("Let's play again..")     

t = Timer(5, play())
t.start()

t.cancel()


     
