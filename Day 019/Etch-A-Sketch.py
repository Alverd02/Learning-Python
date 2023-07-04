from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


def move_backward():
    tim.back(50)


def counter_clockwise():
    tim.left(22.5)


def clockwise():
    tim.right(22.5)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=screen.reset)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)

screen.exitonclick()
