from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

steps = int(input("Number of steps: "))
angle = [0, 90, 180, 270]
velocity = int(input("Velocity (1-11): "))

tim.pensize(10)
screen.colormode(255)

if velocity == 11:
    velocity = 0
    tim.speed(velocity)
else:
    tim.speed(velocity)

def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for _ in range(steps):
    tim.pencolor(color())
    tim.forward(50)
    tim.right(random.choice(angle))

screen.exitonclick()
