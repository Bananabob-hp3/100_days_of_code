import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"


screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()



game_is_on = True
data = pandas.read_csv("50_states.csv")
correct_guess = []
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Whats another states's name").title()
    answer = data[data.state == answer_state]
    if answer_state in data.state.values:
        correct_guess.append(answer_state)
        x = answer.x.values[0]
        y = answer.y.values[0]
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)

    if answer_state == "Exit": 
        left_states = [state for state in data.state.values if state not in correct_guess]
        game_is_on = False
        new_data = pandas.DataFrame(left_states)
        new_data.to_csv("States_To_Larn.csv")

    if len(correct_guess) == 50:
        game_is_on = False






turtle.mainloop()
