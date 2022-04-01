from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.goto(320, random.randint(-240, 240))

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)


