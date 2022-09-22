from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __int__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        # self.update_level()

    def update_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        # self.score += 1
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.score += 1
        # self.level_no += 1
        # self.level += 1


        #Work on attribute game_level its not working
