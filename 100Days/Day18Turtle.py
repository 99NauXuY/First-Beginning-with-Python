from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy_the_turtle.color(R, G, B)


def make_square():
    for durchlauf in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


def dash_line():
    for durchlauf in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


def draw_shape(anzahl):
    for shapes in range(3, anzahl+1):
        change_color()
        for draw in range(0, shapes):
            timmy_the_turtle.forward(50)
            timmy_the_turtle.right(360/shapes)


def draw_random_walk(anzahl):
    direction = [0, 90, 180, 270]
    for i in range(anzahl):
        change_color()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(random.choice(direction))


def draw_spirograph(size):
    timmy_the_turtle.speed("fastest")
    for i in range(int(360/size)):
        change_color()
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()
