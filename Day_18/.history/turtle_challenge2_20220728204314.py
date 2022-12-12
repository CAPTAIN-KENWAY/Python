import turtle as t
timmy=t.Turtle()
pos=timmy.position()
# for i in range(4):
#     timmy.fd(10)
#     timmy.goto(pos[0]+100,pos[1])
#     pos=timmy.position()

timmy.fd(10)
timmy.setx(pos[0]+100)
timmy.sety(pos[1])
screen=t.Screen()
screen.exitonclick()