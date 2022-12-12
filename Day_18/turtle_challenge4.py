import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

directions=[0,90,180,270]
tim.pensize(10)
tim.speed(0)
for _ in range(200):
    tim.pencolor(random_colour())
    tim.setheading(random.choice(directions))
    tim.forward(20)

screen=t.Screen()
screen.exitonclick()