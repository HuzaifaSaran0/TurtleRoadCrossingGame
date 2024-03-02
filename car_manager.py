import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.Move_inc = 10
        # self.Move()

    def Create_Cars(self, choice, value):
        random_choice = random.randint(1, choice)
        if random_choice <= value:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def Move(self):
        for car in self.cars:
            car.backward(self.Move_inc)
