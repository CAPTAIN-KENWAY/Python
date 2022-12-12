from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore = 0
        self.rscore = 0
        self.display_score()
        

    def l_point(self):
        self.lscore += 1
        self.clear()
        self.display_score()

    def r_point(self):
        self.rscore += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))
