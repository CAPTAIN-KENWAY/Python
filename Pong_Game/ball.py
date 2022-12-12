from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ydir = 1
        self.xdir = 1

    def bounce_y(self):
        self.ydir *= -1

    def bounce_x(self):
        self.xdir *= -1

    def move(self):
        x = self.xcor()+10 * self.xdir
        y = self.ycor()+10 * self.ydir
        self.goto(x, y)

    def restart(self):
        self.home()
        self.xdir *= -1
        #self.ydir *= -1
