import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

cars= []
for random_car in range(0, 100):
    car_random_car = CarManager()
    cars.append(car_random_car)

screen.listen()
screen.onkey(fun=player.move_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car= random.choice(cars)
    car.move_car()


    # car = CarManager()



screen.exitonclick()
