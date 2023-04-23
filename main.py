from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key='Up')
screen.onkey(snake.down, key='Down')
screen.onkey(snake.left, key='Left')
screen.onkey(snake.right, key='Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increment()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300 or snake.head.xcor() < -300:
        scoreboard.reset()
        scoreboard.update_scoreboard()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            scoreboard.update_scoreboard()
            snake.reset()


screen.exitonclick()
