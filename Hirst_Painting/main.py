###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

x = -200
y = -200
tim.goto(x, y)
for i in range(1, 101):
    tim.dot(20, random.choice(rgb_colors))
    tim.fd(40)
    if i % 10 == 0:
        y += 40
        tim.goto(x, y)

screen = t.Screen()
screen.exitonclick()
