from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

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

# create the ball
ball = Ball()

on = True
while on:
    time.sleep(0.1)
    screen.update()
    # make the ball move constantly
    ball.move()

    # detect collision with wall
    if ball.ycor() > 145 or ball.ycor() < -145:
        ball.bounceY()

    # detect collision with paddle
    if (ball.distance(pad_1) < 50 and ball.xcor() > 290) or (ball.distance(pad_2) < 43 and ball.xcor() > -330):
        ball.bounceX()   

    # detect paddle missing ball
    if ball.xcor() > 330:
        ball.reset()
    if ball.xcor() < -330:
        ball.reset()



# detect collicion with the wall -> bounce

# detect collicion with paddle

# detect when paddle misses

# keep track of score

# winning condition

screen.exitonclick()