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
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_level()


screen.listen()
screen.onkey(fun=player.move_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

# detecting collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

# Leveling Up
    if player.ycor() >= 270:
        player.player_reset()
        car_manager.next_level()
        scoreboard.update_level()


screen.exitonclick()
