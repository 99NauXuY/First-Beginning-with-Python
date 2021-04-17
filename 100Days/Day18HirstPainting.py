# import colorgram as cg
# colors = cg.extract('Image.jpg', 10)
# color_set = []
# for each in colors:
#    r = each.rgb.r
#    g = each.rgb.g
#    b = each.rgb.b
#    rgb_set = (r, g, b)
#    color_set.append(rgb_set)
# print(color_set)

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(240, 239, 238), (239, 67, 34), (236, 35, 119), (152, 27, 62), (6, 150, 96), (238, 209, 222),
              (206, 224, 230), (245, 166, 34), (44, 190, 232), (183, 158, 46)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()