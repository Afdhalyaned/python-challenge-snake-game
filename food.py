from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.penup()
        random_X = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_X, random_y)
