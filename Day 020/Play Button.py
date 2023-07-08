from turtle import Turtle

class Play_Button:
    def generate_button(self):
        play_button = Turtle()
        play_button.color("blue")
        play_button.pensize(15)
        play_button.speed(0)
        play_button.goto(0, 270)
        play_button.forward(50)
        play_button.right(90)
        play_button.forward(20)
        play_button.right(90)
        play_button.forward(100)
        play_button.right(90)
        play_button.forward(20)
        play_button.right(90)
        play_button.forward(50)