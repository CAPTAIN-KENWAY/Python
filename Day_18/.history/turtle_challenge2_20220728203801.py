import turtle as t
timmy=t.Turtle()
for i in range(4):
    timmy.fd(100)
    timmy.left(90)
pos=timmy.position()
print(pos[0]+1)
timmy.setpos(pos[0]+1,pos[1]+1)
screen=t.Screen()
screen.exitonclick()