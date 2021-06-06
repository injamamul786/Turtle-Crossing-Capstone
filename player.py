from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.new_level()

    def new_level(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def l_left(self):
        x_cor = self.xcor() - 10
        self.goto(x_cor, self.ycor())

    def r_right(self):
        x_cor = self.xcor() + 10
        self.goto(x_cor, self.ycor())

    def finish(self):
        self.clear()
        self.goto(0, 0)
        self.hideturtle()
        self.write("You Win!", align="center", font=("Areal", 30, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.hideturtle()
        self.write("Game Over", align="center", font=("Areal", 30, "normal"))
