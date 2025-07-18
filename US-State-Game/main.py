import csv
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.values

game_still_on = True
t = turtle.Turtle()
guessed = []

while len(guessed) < 50:
    user_answer = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                   prompt="What's another state's name? ").title()
    if user_answer == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed:
                missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("States to learn.csv")
        break
    if user_answer in all_state:
        t.hideturtle()
        t.penup()

        state_data = data[data.state == user_answer]

        t.goto(state_data.x.item(), state_data.y.item())
        t.write(user_answer)
        guessed.append(user_answer)

#states_to_learn.csv


