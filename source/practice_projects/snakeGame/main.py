from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# setup screen
screen = Screen()
screen.setup(width=666, height=666)
screen.bgcolor("black")
screen.title("My amazing snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

# handle change directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def gameOver():
    scoreBoard.gameOver()
    return False

on = True
# move the snake
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        # refresh food to new position
        food.refresh()
        snake.eat()
        scoreBoard.addPointToScore()

    # detect collision with wall
    if snake.head.xcor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        on = gameOver()

    # if head collides with any segment in its tail
    # for segment in snake.snake:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         on = gameOver()
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            on = gameOver()


screen.exitonclick()