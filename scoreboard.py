from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.penup()
        self.color("green")
        self.hideturtle()
        self.goto(-270, 250)
        self.write(f"LEVEL:{self.level}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL:{self.level}", align="left", font=FONT)

