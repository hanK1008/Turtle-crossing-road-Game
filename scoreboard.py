
FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        # self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


    def update_level(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.score += 1
