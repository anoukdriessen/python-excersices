from turtle import Screen, Turtle

# setup screen
screen = Screen()
screen.setup(width=666, height=666)
screen.bgcolor("black")
screen.title("My amazing snake game")

# create the starting snake body
# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

snake = []
starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)
    snake.append(segment)



screen.exitonclick()