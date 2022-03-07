print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# code written based on the flowchart 
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# the story
step1 = "You come across a crossroad, where do you want to go? [left / right]\n"
step2 = "There is a river in front of you, what do you want to do? [swim / wait]\n"
step3 = "There are three doors in front of you, a RED, YELLOW and BLUE, which door do you want to open? [R/Y/B]\n"

gameover = "GAME OVER"

choice1 = input(step1);
if choice1.lower() != "left":
    print("You went right...")
    print(f"You fell into a hole... {gameover}")
else:
    print("You went left...")
    choice2 = input(step2)
    print(choice2)
    if choice2.lower() != "wait":
        print("You chose to swim...")
        print(f"You've been attacked by a trout... {gameover}")
    else:
        print("You chose to wait...")
        choice3 = input(step3)
        if choice3.lower() == "r":
            print("You chose the red door")
            print(f"You've been burned by a fire... {gameover}")
        elif choice3.lower() == "y":
            print("You chose the yellow door")
            print("CONGRATS! YOU'VE WON!")
        elif choice3.lower() == "b":   
            print("You chose the blue door")
            print(f"You've been eaten by beasts... {gameover}")
        else:
            print(f"You chose no door, the floor fell from beneath you... {gameover}")         