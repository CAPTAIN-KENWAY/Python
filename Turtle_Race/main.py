import random
from turtle import Turtle, Screen
is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
choice = screen.textinput(title="Make your bet",
                          prompt="Which turtle will win the race? Pick a colour.")

turtles = []
p = -80
for i in range(6):
    turtles.append(Turtle("turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=p)
    p += 30

if choice:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winner=turtle.color()[0]
            is_race_on=False
            break
        turtle.forward(random.randint(1, 10))

if choice==winner:
    print(f"You've won! The {winner} turtle is the winner.")
else:
    print(f"You've lost! The {winner} turtle is the winner.")    
screen.exitonclick()
