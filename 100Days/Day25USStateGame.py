import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                    prompt="What is another states name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in state_list if state not in guessed]
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("learn_states.csv")
        break
    if answer_state in state_list:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

