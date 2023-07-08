import time
from turtle import Screen
from Snake import Snake
from Food import Food

window = Screen()
window.setup(600, 600)
window.bgcolor("white")
window.title("Snake Game")
window.listen()
window.tracer(0)
window.colormode(255)

snake = Snake()

window.onkey(fun=snake.right, key="d")
window.onkey(fun=snake.left, key="a")
window.onkey(fun=snake.up, key="w")
window.onkey(fun=snake.down, key="s")



def game():
    food = Food()
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
