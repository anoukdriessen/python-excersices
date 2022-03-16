from turtle import Turtle

START_AT = (0, -280)
MOVE = 10
FINISH_LINE = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def moveUp(self):
        self.forward(MOVE)

    def start(self):
        self.goto(START_AT)

    def hasFinished(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
