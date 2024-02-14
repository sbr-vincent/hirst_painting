# import colorgram
#
# colors = colorgram.extract('painting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()
x = -200
y = -100
color_list = [(244, 235, 48), (196, 12, 35), (218, 160, 70), (43, 80, 177), (237, 40, 140), (38, 215, 76), (237, 228, 5), (31, 40, 154), (206, 72, 22), (21, 149, 23), (201, 34, 98), (70, 11, 27), (182, 16, 11), (213, 164, 10), (218, 140, 195), (56, 15, 10), (17, 20, 48), (13, 95, 62), (79, 210, 159), (73, 73, 221), (83, 191, 220), (237, 158, 216), (94, 232, 200), (217, 82, 51), (5, 230, 239), (14, 64, 44)]
tim.setposition(x, y)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    y += 50
    tim.setposition(x, y)


screen.exitonclick()






