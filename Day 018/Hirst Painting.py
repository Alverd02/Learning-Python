from turtle import Turtle, Screen
import random
"""
Extracting colors from an image
"""
# import colorgram
#
# colors = colorgram.extract("circuito-interstellar-islandia.jpg", 30)
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     rgb_color = (r, g, b)
#     colors[i] = rgb_color

color_list = [(115, 83, 70), (13, 9, 10), (247, 231, 224), (193, 145, 124), (241, 229, 235), (77, 58, 53),
              (114, 96, 99), (167, 148, 157), (160, 117, 101), (222, 180, 167), (139, 120, 125), (205, 183, 192),
              (246, 185, 132), (94, 59, 31), (73, 58, 60), (185, 118, 67), (4, 5, 7), (9, 11, 10)]

screen = Screen()
screen.colormode(255)

# length = 10*(50) = 500
# window_center = (0, 0)
# window_width = 960
# window_height = 810

def draw_row(row):
    for i in range(10):
        dot = Turtle()
        dot.hideturtle()
        dot.speed(8)
        dot.penup()
        dot.shape("circle")
        dot.pensize(20)
        dot.setposition(-250 + 50 * i, -250 + 50 * row)
        dot.pendown()
        dot.showturtle()
        dot.color(random.choice(color_list))


for j in range(10):
    draw_row(j)

screen.exitonclick()
