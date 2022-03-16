from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.movementX = 10
        self.movementY = 10
        self.speed = 0.1

        
    def move(self):
        newX = self.xcor() + self.movementX
        newY = self.ycor() + self.movementY
        self.goto(newX, newY)

    # ball bounces on wall
    def bounceY(self):
        self.movementY *= -1

    # ball bounces on paddle
    def bounceX(self):
        self.movementX *= -1  
        self.speed *= 0.9  

    def reset(self):
        self.goto(0,0)
        self.speed = 0.1
        self.bounceX()