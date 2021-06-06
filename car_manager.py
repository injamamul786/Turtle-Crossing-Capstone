from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
number_of_car = 15


class CarManager:
    def __init__(self):
        self.car_list = []
        for car in range(number_of_car):
            timmy = Turtle()
            timmy.color(choice(COLORS))
            timmy.shape("square")
            timmy.penup()
            timmy.setheading(180)
            timmy.shapesize(1, 2)
            self.car_list.append(timmy)
            timmy.setpos(randint(-300, 300), randint(-300, 300))

    def new_position(self):
        for i in range(number_of_car):
            x_cor = self.car_list[i].xcor()
            if x_cor < -300:
                self.car_list[i].goto(300, randint(-300, 300))

    def move(self):
        for i in range(number_of_car):
            self.car_list[i].forward(MOVE_INCREMENT)
