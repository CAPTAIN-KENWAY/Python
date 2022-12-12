import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        x = 300
        y = random.randint(-250, 250)
        car.setheading(180)
        car.goto(x, y)
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
