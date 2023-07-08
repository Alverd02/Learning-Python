from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
screen.colormode(255)


def start():
    starter = Turtle()
    starter.speed(0)
    starter.hideturtle()
    starter.penup()
    starter.setx(-215)
    starter.sety(125)
    starter.right(90)
    starter.pendown()
    starter.pensize(5)
    starter.forward(250)
    starter.penup()
    starter.hideturtle()
    starter.forward(30)
    starter.write("Start", False, align="center", font=("Arial", 60, "normal"))


def end():
    ender = Turtle()
    ender.speed(0)
    ender.hideturtle()
    ender.penup()
    ender.setx(215)
    ender.sety(125)
    ender.right(90)
    ender.pendown()
    ender.pensize(5)
    ender.forward(250)
    ender.penup()
    ender.hideturtle()
    ender.forward(30)
    ender.write("Finish", False, align="center", font=("Arial", 15, "normal"))


def title():
    title_drawer = Turtle()
    title_drawer.speed(0)
    title_drawer.hideturtle()
    title_drawer.penup()
    title_drawer.left(90)
    title_drawer.forward(125)
    title_drawer.color("green")
    title_drawer.write("Turtle Race", False, align="center", font=("Arial", 50, "normal"))


def positions():
    colours = ["red", "orange", "yellow", "green", "blue", "violet"]
    turtles = []
    for i in range(1, 7):
        turtle = Turtle()
        turtle.speed(2)
        turtle.shape("turtle")
        turtle.color(colours[i - 1])
        turtle.fillcolor(colours[i - 1])
        turtle.penup()
        turtle.setpos(-235, -140 + 40 * i)
        turtles.append(turtle)

    return turtles


def race(turtles):
    winner = 0
    play = True
    while play:
        for i in turtles:
            i.forward(random.randint(10, 25))
            x_2, y_2 = i.position()
            if x_2 >= 205:
                winner = i
                play = False
                break
    return winner.color()


def game():
    start()
    end()
    title()
    turtles = positions()
    guess = screen.textinput(title="Make your bet", prompt="Which turtle will win? Guess the colour: ")
    winner_color = race(turtles)
    win = Turtle()
    win.hideturtle()
    win.penup()
    win.speed(0)
    if winner_color[0] == guess.lower():
        win.color(guess.lower())
        win.write("You win!!!", False, align="center", font=("Arial", 30, "normal"))
    else:
        win.color(winner_color[0])
        win.write("You lose!!!", False, align="center", font=("Arial", 30, "normal"))


game()


screen.exitonclick()
