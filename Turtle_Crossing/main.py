import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=player.move)
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i % 6 == 0:
        cars.generate_cars()
    i += 1
    cars.move_car()
    if player.check_finish() == True:
        scoreboard.increase_level()
        cars.increase_speed()
    for car in cars.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

screen.exitonclick()
