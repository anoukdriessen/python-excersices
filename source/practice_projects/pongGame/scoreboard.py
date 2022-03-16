from turtle import Turtle, update
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lightgreen")
        self.penup()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        self.update()

    def update(self):
        self.clear() # clear the scoreboard before updating
        self.goto(-100, 125)
        self.write(self.score_p1, align=ALIGN, font=FONT)
        self.goto(100, 125)
        self.write(self.score_p2, align=ALIGN, font=FONT)

    def givePointToPlayer(self, player):
        if player == "p1":
            self.score_p1 += 1
        else:
            self.score_p2 += 1    
        self.update()    