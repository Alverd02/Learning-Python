import time
from turtle import Screen
from Snake import Snake
from Food import Food
import random

window = Screen()
window.setup(600, 600)
window.bgcolor("white")
window.title("Snake Game")
window.listen()
window.tracer(0)
window.colormode(255)

snake = Snake()
food = Food()

window.onkey(fun=snake.right, key="d")
window.onkey(fun=snake.left, key="a")
window.onkey(fun=snake.up, key="w")
window.onkey(fun=snake.down, key="s")

play = True
food.generate()

while play:
    window.update()
    time.sleep(0.1)
    snake.move()
    if abs(snake.squares[0].position()[0]-food.position[0]) < 20 and abs(snake.squares[0].position()[1]-food.position[1]) < 20:
        food.generate()
    else:
        pass
    if snake.find_border:
        snake.write()
        play = False

window.exitonclick()
