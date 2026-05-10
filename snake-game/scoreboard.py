from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 23, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 269)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        print(f"score: {self.score}, high_score: {self.high_score}")
        if self.score > self.high_score:
            print("condition met")
            if self.score > 9:
                self.score += 5
                print(f"bonus applied, score now: {self.score}")
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




















# def game_over(self):
      #  self.clear()
     #   self.goto(0, 0)
    #    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
