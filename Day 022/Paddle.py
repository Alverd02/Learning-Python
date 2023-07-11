from turtle import Turtle


class Paddle:
    def __init__(self):
        self.players = []
        self.left_paddle()
        self.right_paddle()

    def left_paddle(self):
        paddle = Turtle()
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(5, 1)
        paddle.penup()
        paddle.speed(0)
        paddle.goto(-380, 0)
        self.players.append(paddle)

    def right_paddle(self):
        paddle = Turtle()
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(5, 1)
        paddle.penup()
        paddle.speed(0)
        paddle.goto(370, 0)
        self.players.append(paddle)

    def up_player1(self):
        if not self.players[0].position()[1] > 230:
            self.players[0].shapesize(1, 5)
            self.players[0].setheading(90)
            self.players[0].forward(15)

    def down_player1(self):
        if not self.players[0].position()[1] < -230:
            self.players[0].shapesize(1, 5)
            self.players[0].setheading(270)
            self.players[0].forward(15)

    def up_player2(self):
        if not self.players[1].position()[1] > 230:
            self.players[1].shapesize(1, 5)
            self.players[1].setheading(90)
            self.players[1].forward(15)

    def down_player2(self):
        if not self.players[1].position()[1] < -230:
            self.players[1].shapesize(1, 5)
            self.players[1].setheading(270)
            self.players[1].forward(15)
