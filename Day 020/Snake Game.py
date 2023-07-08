import time
from turtle import Screen
from Snake import Snake
from Food import Food
from turtle import Turtle

window = Screen()
window.setup(600, 600)
window.bgcolor("white")
window.title("Snake Game")
window.listen()
window.tracer(0)
window.colormode(255)


def play_button():
    button = Turtle()
    button.hideturtle()
    button.pensize(4)
    button.penup()
    button.goto(0, 240)
    button.write(f"PLAY", False, align="center", font=("Arial", 15, "normal"))
    button.pendown()
    button.forward(40)
    button.left(90)
    button.forward(23)
    button.left(90)
    button.forward(80)
    button.left(90)
    button.forward(23)
    button.left(90)
    button.forward(40)


def wait_for_click():
    global click
    window.update()
    click = False
    while not click:
        window.update()
    click = False
def clicked_position(x, y):
    global click
    global selected
    selected = False
    click = True
    if (-40) < x < 40 and 264 > y > 240:
        selected = True

snake = Snake()
food = Food()

window.onkey(fun=snake.right, key="d")
window.onkey(fun=snake.left, key="a")
window.onkey(fun=snake.up, key="w")
window.onkey(fun=snake.down, key="s")

play_button()
window.onclick(clicked_position)

while True:
    wait_for_click()
    if selected:
        break

play = True
while play:
    window.update()
    time.sleep(0.1)
    snake.move()
    if food.apple_object[0].distance(snake.squares[0]) < 20:
        snake.score_message[0].clear()
        snake.score += 1
        snake.write_score()
        snake.food_eaten += 1
        food.go_to()
        snake.more_body()
    if snake.find_border:
        snake.write()
        play = False


window.exitonclick()
