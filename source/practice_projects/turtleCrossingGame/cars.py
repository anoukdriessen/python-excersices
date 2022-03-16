from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE = 5
SPEED_UP = 10

class Cars:
    def __init__(self):
        self.cars = [] # collection of all cars
        self.speed = MOVE

    def newCar(self):
        r = random.randint(1,7)
        if r == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))    # get a random color
            y = random.randint(-250, 250)       # generate random Y value
            car.goto(333, y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)    # move each car

    def level_up(self):
        self.speed += SPEED_UP
