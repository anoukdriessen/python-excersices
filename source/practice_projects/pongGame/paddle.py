from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.7)
        self.penup()
        self.goto(x, y)

    def up(self):
        if self.ycor() + 20 < 160:
            newY = self.ycor() + 20
        else:
            newY = self.ycor()
        self.goto(self.xcor(), newY)
    
    def down(self):
        if self.ycor() - 20 > -160:
            newY = self.ycor() - 20
        else:
            newY = self.ycor()
        self.goto(self.xcor(), newY)