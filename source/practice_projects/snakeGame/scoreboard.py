from turtle import Turtle
ALIGN = "center"
FONT = ("Roboto", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("source/files/highscore_snake.txt", mode="r") as f:
            self.highscore = int(f.read())
        self.color("pink")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align=ALIGN, font=FONT)

    def addPointToScore(self):
        self.score += 1  
        self.update()

    # def gameOver(self):
        # self.goto(0,0)
        # self.write(f"GAMEOVER\nyou scored {self.score} points", align=ALIGN, font=FONT)

    def gameOver(self):
        if self.score > self.highscore: # if the current score is higher than the current highscore
            self.highscore = self.score
            # write highscore to file
            with open("source/files/highscore_snake.txt", mode="w") as f:
                f.write(str(self.highscore))  
        self.score = 0  
        self.update()




