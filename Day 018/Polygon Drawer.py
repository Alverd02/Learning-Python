from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

number = int(input("Number of polygons: "))
colors = ["black", "royal blue", "powder blue", "green yellow", "brown", "navajo white", "medium orchid", "goldenrod", "maroon", "olive", "teal", "red", "midnight blue", "medium violet red"]

for i in range(number):
    tim.pencolor(random.choice(colors))
    for _ in range(3+i):
        tim.forward(75)
        angle = (360/(3+i))
        tim.right(angle)


screen.exitonclick()
