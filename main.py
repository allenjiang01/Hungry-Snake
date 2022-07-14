from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_X = 600
SCREEN_Y = 600
SCREEN_COLOR = 'black'
SCREEN_TITLE = 'Hungry Snake'


def start_game():
    # SNAKE SETUP
    snake = Snake()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    # FOOD SETUP
    food = Food()

    # SCOREBOARD SETUP
    scoreboard = Scoreboard()

    is_playing = True

    while is_playing:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.segments[0].distance(food) < 20:
            food.new_food()
            snake.create_snake()
            scoreboard.increase()

        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
                snake.segments[0].ycor() < -280:
            scoreboard.game_over()
            is_playing = False

        for s in snake.segments[1:]:
            if snake.segments[0].distance(s) < 10:
                scoreboard.game_over()
                is_playing = False
                break


def make_screen():
    screen.setup(SCREEN_X, SCREEN_Y)
    screen.bgcolor(SCREEN_COLOR)
    screen.title(SCREEN_TITLE)
    screen.tracer(0)
    screen.listen()
    start_game()


def restart():
    screen.clear()
    make_screen()
    screen.onkey(restart, 'space')


# SCREEN SETUP
screen = Screen()
restart()

screen.exitonclick()
