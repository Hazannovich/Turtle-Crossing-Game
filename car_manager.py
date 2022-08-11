import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.forward(self.moving_speed)

    def new_car(self):
        if random.randint(0, 5) == 0:
            car = Turtle()
            car.shape("square")
            car.color(COLORS[random.randint(0, 5)])
            car.turtlesize(stretch_len=2)
            car.pu()
            car.goto(280, random.randint(-250, 250))
            car.setheading(180)
            self.cars.append(car)
