import colorgram as gram
from turtle import Turtle, Screen
import random as r

# extracts the 10 most common colors from the picture given
extraction = gram.extract("hirst_paint.jpg", 10)

# covert extracted colors from picture into list of unnamed tuples, usable for rgb colors in turtle
color_palette = []
for color in extraction:
    color_palette.append((color.rgb.r, color.rgb.g, color.rgb.b))

# initial screen and turtle setup
tur = Turtle()
tur.speed(7)
tur.hideturtle()
tur.penup()

scr = Screen()
scr.colormode(255)
position_x = -225
position_y = -225

tur.goto(position_x, position_y)

# main cycle - prints 10 lines of 10 dots
for _ in range(1, 11):
    for i in range(1, 11):
        tur.pendown()
        tur.dot(20, r.choice(color_palette))
        tur.penup()
        tur.forward(50)
    position_y += 50
    tur.goto(position_x, position_y)

scr.exitonclick()
