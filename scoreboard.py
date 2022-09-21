from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super().__init__()
        self.game_level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(250, 250)
        self.write(arg=self.game_level, align="center", font=FONT)
        self.game_level += 1


        #Work on attribute game_level its not working
