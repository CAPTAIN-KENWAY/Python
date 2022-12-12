from tabnanny import check
import turtle as t
timmy=t.Turtle()
side=3
angle=360/side
check_angle=0
while side<=10:
    timmy.fd(100)
    timmy.right(angle)
    check_angle+=angle
    if check_angle==360:
        side+=1
        angle=360/side
        check_angle=0
    print(angle)
    print(f"check angle: {check_angle}")
    
    

screen=t.Screen()
screen.exitonclick()