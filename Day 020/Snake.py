from turtle import Turtle
class Snake:
    def __init__(self):
        self.squares = []
        self.snake_body()
        self.find_border = False
        self.food_eaten = 0
        self.score = 0
        self.score_message = []
        self.write_score()
    def write(self):
        if self.find_border == 1:
            message = Turtle()
            message.goto(0, 150)
            message.write("You lose!!", False, align="center", font=("Arial", 60, "normal"))
    def write_score(self):
        message = Turtle()
        self.score_message.clear()
        self.score_message.append(message)
        message.penup()
        message.hideturtle()
        message.goto(0, 275)
        message.write(f"Score = {self.score}", False, align="center", font=("Arial", 15, "normal"))
    def snake_body(self):
        for i in range(3):
            if i == 0:
                body = Turtle()
                body.color(0, 51, 0)
                body.shape("square")
                body.penup()
                body.goto(-20 * i, 0)
                self.squares.append(body)
            else:
                body = Turtle()
                body.color(0, 102, 51)
                body.shape("square")
                body.penup()
                body.goto(-20 * i, 0)
                self.squares.append(body)
    def move(self):
        for j in reversed(range(len(self.squares))):
            if j == 0:
                self.squares[0].forward(20)
                for k in self.squares[1:]:
                    if k.distance(self.squares[0]) < 10:
                        self.find_border = True
                if self.squares[0].xcor() > 295 or self.squares[0].xcor() < -295:
                    self.find_border = True
                elif self.squares[0].ycor() > 295 or self.squares[0].ycor() < -295:
                    self.find_border = True
            else:
                x, y = self.squares[j - 1].position()
                self.squares[j].goto(x, y)
    def more_body(self):
        for i in range(self.food_eaten):
            body = Turtle()
            body.color(0, 102, 51)
            body.shape("square")
            body.penup()
            body.goto(self.squares[-1].position())
            self.squares.append(body)
            self.food_eaten = 0
    def up(self):
        if not self.squares[0].heading() == 270:
            self.squares[0].setheading(90)
    def right(self):
        if not self.squares[0].heading() == 180:
            self.squares[0].setheading(0)
    def left(self):
        if not self.squares[0].heading() == 0:
            self.squares[0].setheading(180)
    def down(self):
        if not self.squares[0].heading() == 90:
            self.squares[0].setheading(270)