from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.penup()
        self.go_to_start()
        self.left(90)


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def collide(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Corier", 80, "normal")) 

    def refresh(self):
        self.goto(0, -250)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
