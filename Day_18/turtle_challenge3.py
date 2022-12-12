import random
from tabnanny import check
import turtle as t
timmy = t.Turtle()
colors = [
    "#838B8B", '#00008B', '#008B8B', '#B8860B', '#FFB90F', '#EEAD0E', '#CD950C', '#8B6508',
    '#A9A9A9', '#006400', '#A9A9A9', '#BDB76B', '#8B008B', '#556B2F', '#CAFF70', '#BCEE68',
    '#A2CD5A', '#6E8B3D', '#FF8C00', '#FF7F00', '#EE7600', '#CD6600', '#8B4500', '#9932CC',
    '#BF3EFF', '#B23AEE', '#9A32CD', '#68228B', ]
side = 3
angle = 360/side
check_angle = 0
timmy.pencolor(random.choice(colors))
while side <= 10:
    timmy.fd(100)
    timmy.right(angle)
    check_angle += angle
    if round(check_angle) == 360:
        side += 1
        angle = 360/side
        check_angle = 0
        timmy.pencolor(random.choice(colors))

timmy.fd(100)


screen = t.Screen()
screen.exitonclick()
