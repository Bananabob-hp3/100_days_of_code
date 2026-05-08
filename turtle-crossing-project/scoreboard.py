from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.point}", align="left", font=("Corier", 24, "normal"))

    def player_point(self):
        self.point += 1
        self.update_score()
