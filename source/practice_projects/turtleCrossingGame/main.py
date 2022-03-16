import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=666, height=666)
screen.title("My awesome Turtle Crossing Game")
screen.bgcolor("white")
screen.tracer(0)

# create the turtle
player = Player()

# create the cars
cars = Cars()

# create the scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.moveUp, "Up")       # turtle moves only forward -> "Up" key

on = True
while on:
    time.sleep(0.1)
    screen.update()

    # cars are randomly generated along the y-axis and will move from right to left
    cars.newCar()
    cars.move()

    # when turtle collides with a car -> game over
    for car in cars.cars:
        if car.distance(player) < 20:
            on = False
            scoreboard.game_over()

    # when turtle hits top edge of the screen -> level up
    if player.hasFinished():
        player.start()
        # on the next level the scoreboard gets updated and the car speed increases
        cars.level_up()
        scoreboard.levelUp()


screen.exitonclick()