from turtle import Turtle
ALIGN = "center"
FONT = ("Roboto", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("pink")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def addPointToScore(self):
        self.score += 1  
        self.clear()
        self.update()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAMEOVER\nyou scored {self.score} points", align=ALIGN, font=FONT)



