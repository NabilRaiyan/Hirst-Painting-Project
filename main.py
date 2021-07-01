import random
import turtle as turtle_module
from turtle import Screen

color_list = [(139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162),
              (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89),
              (228, 167, 173), (189, 99, 107), (139, 33, 28)]

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dot_count = 100

for dot_count in range(1, number_of_dot_count + 1):
    timmy.dot(15, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()
