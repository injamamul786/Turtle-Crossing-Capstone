import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
sleep_time = 0.1
scoreboard = Scoreboard()
number = 10
while number > 0:
    screen.clear()
    scoreboard.increase_score()
    screen.tracer(0)
    car = CarManager()
    player = Player()

    screen.listen()
    screen.onkey(fun=player.up, key="Up")
    screen.onkey(fun=player.down, key="Down")
    screen.onkey(fun=player.l_left, key="Left")
    screen.onkey(fun=player.r_right, key="Right")

    game_is_on = True
    while game_is_on:
        time.sleep(sleep_time)
        screen.update()
        car.move()
        car.new_position()
        if player.ycor() > 280:
            player.finish()
            game_is_on = False
            number -= 1
            time.sleep(1)
            sleep_time *= (10/12)
        for i in range(15):
            if player.distance(car.car_list[i]) < 20:
                game_is_on = False
                player.game_over()
                level_continue = False
                number = 0
screen.exitonclick()
