import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
screen.colormode(255)

def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for i in range(1, 7):
    turtle_i = Turtle()
    turtle_i.shape("turtle")
    turtle_i.fillcolor(colour())
    turtle_i.penup()
    turtle_i.setx(-235)
    turtle_i.sety(-140+40*i)

guess = screen.textinput(title="Make your bet", prompt="Which turtle will win? Guess the colour: ")




screen.exitonclick()
