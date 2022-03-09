from turtle import Turtle, Screen

# create and decorate the turtle
sloomie_the_turtle = Turtle()
sloomie_the_turtle.shape("turtle")
sloomie_the_turtle.color("pink")

# create the screen
screen = Screen()

# move the turtle
def move():
    sloomie_the_turtle.forward(100)
    sloomie_the_turtle.right(90)
    sloomie_the_turtle.forward(100)
    sloomie_the_turtle.right(90)
    sloomie_the_turtle.forward(100)
    sloomie_the_turtle.right(90)
    sloomie_the_turtle.forward(100)

def moveForwards():
    sloomie_the_turtle.forward(10)

def moveBackwards():
    sloomie_the_turtle.backward(10)

def moveCounterClockwise():
    sloomie_the_turtle.left(10)

def moveClockwise():
    sloomie_the_turtle.right(10)    

def sketch():
    screen.listen()
    screen.onkey(key="w", fun=moveForwards)
    screen.onkey(key="s", fun=moveBackwards)
    screen.onkey(key="a", fun=moveCounterClockwise)
    screen.onkey(key="d", fun=moveClockwise)
    



sketch()
screen.exitonclick()