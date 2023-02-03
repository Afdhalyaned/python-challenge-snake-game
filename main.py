from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# screate setup for screen
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Game Ular")
screen.tracer(0)

# init snake class and food class
snake = Snake()
food = Food()
score_board = Scoreboard()

# key input
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# create while loop ke make snake moving
game_is_on = True
while game_is_on:
    # create update screen to adjust animation
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.inscrease_score()

    # detect collision with wall
    if snake.head.xcor() > 430 or snake.head.xcor() < -430 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score_board.game_over()


screen.exitonclick()
