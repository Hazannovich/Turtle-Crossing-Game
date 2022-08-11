import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cars")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    if player.ycor() >= 280:
        scoreboard.update_score()
        player.back_to_start()
        car_manager.moving_speed *= 1.3
        screen.update()
        time.sleep(1)
    screen.update()

scoreboard.game_over()

screen.exitonclick()