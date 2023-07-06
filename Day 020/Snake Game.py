from turtle import Screen, Turtle

window = Screen()
window.setup(600, 600)
window.bgcolor("black")
window.title("Snake Game")


def first_body():
    snake = []
    for i in range(3):
        body = Turtle()
        body.color("white")
        body.shape("square")
        body.penup()
        body.speed(0)
        body.goto(-20 * i, 0)
        snake.append(body)
    return snake


window.listen()
snake = first_body()


def up():
    snake[0].speed(0)
    snake[0].setheading(90)


def right():
    snake[0].speed(0)
    snake[0].setheading(0)


def left():
    snake[0].speed(0)
    snake[0].setheading(180)


def down():
    snake[0].speed(0)
    snake[0].setheading(270)


def move(snake):
    for j in range(len(snake)):
        window.onkey(fun=right, key="d")
        window.onkey(fun=left, key="a")
        window.onkey(fun=up, key="w")
        window.onkey(fun=down, key="s")
        print(snake[j].heading())
        if j == 0:
            print(snake[j].heading())
            if snake[j].heading() == 0:
                snake[j].speed(1)
                x, y = snake[j].position()
                snake[j].goto(x + 20, y)
            elif snake[j].heading() == 180:
                snake[j].speed(1)
                x, y = snake[j].position()
                snake[j].goto(x - 20, y)
            elif snake[j].heading() == 270:
                snake[j].speed(1)
                x, y = snake[j].position()
                snake[j].goto(x, y - 20)
            else:
                snake[j].speed(1)
                x, y = snake[j].position()
                snake[j].goto(x, y + 20)
        else:
            snake[j].speed(1)
            x, y = snake[j - 1].position()
            snake[j].goto(x, y)


play = True

while play:
    move(snake)

window.exitonclick()
