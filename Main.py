import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from snake_ai import get_next_move 

DIRECTIONS = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mon Jeux de Serpent")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake_segments = [(segment.xcor(), segment.ycor()) for segment in snake.segments]
    food_position = (food.xcor(), food.ycor())

    next_direction = get_next_move(snake_segments, food_position)

    if next_direction == "up":
        snake.up()
    elif next_direction == "down":
        snake.down()
    elif next_direction == "left":
        snake.left()
    elif next_direction == "right":
        snake.right()

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or \
       snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()