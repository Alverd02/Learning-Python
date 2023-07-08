import random
from turtle import Turtle


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.already_generated = True

    def generate(self):
        apple = Turtle()
        if self.already_generated:
            apple.color("red")
            apple.shape("circle")
            apple.pensize(15)
            apple.penup()
            apple.goto(random.randint(-280, 280), random.randint(-280, 280))
        else:
            apple.goto(random.randint(-280, 280), random.randint(-280, 280))
