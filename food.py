from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('brown')
        self.new_food()

    def new_food(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
