import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Turtle()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()

    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 18:
            game_is_on = False
            player.collide()
            player.refresh()

    if player.is_at_finish_line() == True:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.player_point()




screen.exitonclick()
