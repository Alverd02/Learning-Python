from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball_object = []
        self.generate_ball()


    def generate_ball(self):
        ball = Turtle()
        ball.color("white")
        ball.shape("circle")
        ball.penup()
        self.ball_object.append(ball)

    def move_ball(self):
        self.ball_object[0].goto(self.ball_object[0].position()[0] + 10, 0)

