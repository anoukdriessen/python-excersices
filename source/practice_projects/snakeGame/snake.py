from pickletools import UP_TO_NEWLINE
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.createSnake()
        self.head = self.snake[0]

    def createSnake(self):    
        # create the snakes body
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def eat(self):
        self.addSegment(self.snake[-1].position())

    def move(self):
        for segmentNr in range(len(self.snake) - 1, 0, -1):
            newX = self.snake[segmentNr - 1].xcor()
            newY = self.snake[segmentNr - 1].ycor()
            self.snake[segmentNr].goto(newX, newY)
        self.snake[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



