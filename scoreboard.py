from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-220, 260)

    def writing(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 22, "normal"))

    def IncLevel(self):
        self.level += 1
        print(self.level)

    def game_over(self):
        self.goto(-60, 0)
        self.write("Game Over", font=("Courier", 25, "bold"))
