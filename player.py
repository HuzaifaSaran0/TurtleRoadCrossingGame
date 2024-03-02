from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_POINT = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # self.Color = "black"
        self.color("black")
        self.MOVE_DISTANCE = 10
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.choice = 14
        self.Turn = False
        self.value = 3

    def Turtle_Move(self):
        if self.ycor() < FINISH_POINT:
            self.forward(self.MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)
            self.choice -= 1
            self.Turn = True

    def Accident(self):
        self.color("red")
