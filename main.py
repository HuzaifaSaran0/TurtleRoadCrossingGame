import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
Screen().listen()
Player1 = Player()
car = CarManager()
Level = Scoreboard()


def MoveInc():
    car.Move_inc += 2


Screen().onkey(fun=Player1.Turtle_Move, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.Create_Cars(Player1.choice, Player1.value)
    car.Move()
    Level.writing()
    if Player1.Turn:
        MoveInc()
        Level.IncLevel()
        Player1.Turn = False
    for C_car in car.cars:
        if C_car.distance(Player1) < 25:
            Player1.Accident()
            Screen().update()
            Level.game_over()
            game_is_on = False

Screen().exitonclick()
