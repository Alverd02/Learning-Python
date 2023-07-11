from turtle import Screen
from Paddle import Paddle
from PongBall import Ball
from turtle import Turtle
import time

window = Screen()
window.setup(800, 600)
window.bgcolor("black")
window.title("Pong Game")
window.listen()
window.tracer(0)


def generate_table():
    table = Turtle()
    table.hideturtle()
    table.penup()
    table.goto(0, 300)
    table.pensize(7)
    table.color("white")
    table.setheading(270)

    for i in range(6):
        table.pendown()
        table.forward(50)
        table.penup()
        table.forward(50)


paddles = Paddle()
ball = Ball()

window.onkey(fun=paddles.up_player1, key="w")
window.onkey(fun=paddles.down_player1, key="s")
window.onkey(fun=paddles.up_player2, key="Up")
window.onkey(fun=paddles.down_player2, key="Down")

generate_table()

play = True
while play:
    window.update()
    time.sleep(0.02)
    ball.move_ball()

window.exitonclick()
