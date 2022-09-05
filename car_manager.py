from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_probabilty = random.randint(1, 6)
        if random_probabilty == 1:
            new_car = Turtle("square")
            # self.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.setheading(180)
            new_car.goto(320, random.randint(-240, 240))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def next_level(self):
        self.car_speed += MOVE_INCREMENT

