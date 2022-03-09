from turtle import Screen

# create the screen
screen = Screen()
screen.setup(width=666, height=333)
screen.bgcolor("black")
screen.title("My amazing pong game")
screen.tracer(0)

# handle movements
screen.listen()
# screen.onkey("w")
# screen.onkey("s")
# screen.onkey("Up")
# screen.onkey("Down")
 
# create and move a paddle

# create a second paddle

# create the ball

# make the ball move constantly

# detect collicion with the wall -> bounce

# detect collicion with paddle

# detect when paddle misses

# keep track of score

# winning condition

screen.exitonclick()