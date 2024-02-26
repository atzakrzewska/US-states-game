import pandas
import turtle

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

guessed_states = []

FONT = ("Helvetica", 10, "normal")


def display_name(this_state):
    state_data = data[data.state == this_state]
    x = int(state_data.x.iloc[0])
    y = int(state_data.y.iloc[0])

    name = turtle.Turtle()
    name.penup()
    name.hideturtle()
    name.goto(x, y)
    name.write(arg=this_state, move=False, align="center", font=FONT)


while len(guessed_states) < 50:
    screen.update()
    answered_state = screen.textinput(title="Guess the State",
                                      prompt=f"You've guessed {len(guessed_states)} states out of 50.\n"
                                             f"Which state is missing?")
    answered_state = str(answered_state).title()

    if answered_state in data['state'].values and answered_state not in guessed_states:
        guessed_states.append(answered_state)
        display_name(answered_state)

    if answered_state == "Exit":
        missing_states = [miss_state for miss_state in data.state if miss_state not in guessed_states]
        to_learn = pandas.DataFrame(missing_states)
        to_learn.to_csv("to_learn.csv")
        break

turtle.mainloop()
