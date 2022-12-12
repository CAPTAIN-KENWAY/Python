from turtle import Turtle
PADDLE_LENGTH = 1
PADDLE_WIDTH = 5


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=PADDLE_LENGTH, stretch_wid=PADDLE_WIDTH)
        self.goto(position)

    def move_up(self):
        y = self.ycor()+20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor()-20
        self.goto(self.xcor(), y)
