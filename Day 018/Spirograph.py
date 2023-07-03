from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.speed(0)

number = int(input("Number of circles: "))

for i in range(number):
    tim.pencolor(color())
    tim.circle(150)
    tim.left(360 / number)

screen.exitonclick()
