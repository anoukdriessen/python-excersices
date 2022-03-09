from turtle import Turtle
import random

# use Turtle as superclass
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-300, 300)
        randomY = random.randint(-300, 300)
        self.goto(randomX, randomY)
