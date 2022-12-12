import turtle as t
timmy=t.Turtle()

for i in range(20):
    if i%2==0:
        timmy.pendown()
        timmy.fd(10)
    else:
        timmy.penup()
        timmy.fd(10)
    

screen=t.Screen()
screen.exitonclick()