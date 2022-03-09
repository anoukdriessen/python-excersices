from turtle import Screen
from paddle import Paddle

# create the screen
screen = Screen()
screen.setup(width=666, height=333)
screen.bgcolor("black")
screen.title("My amazing pong game")
screen.tracer(0)

# create and move a paddle
pad_1 = Paddle(310, 0)

# create a second paddle
pad_2 = Paddle(-318, 0)

# handle movement
screen.listen()
screen.onkey(pad_2.up, "w")
screen.onkey(pad_2.down, "s")
screen.onkey(pad_1.up, "Up")
screen.onkey(pad_1.down, "Down")

on = True
while on:
    screen.update()

# create the ball

# make the ball move constantly

# detect collicion with the wall -> bounce

# detect collicion with paddle

# detect when paddle misses

# keep track of score

# winning condition

screen.exitonclick()