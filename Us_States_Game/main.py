import turtle as t
import pandas
screen = t.Screen()
image = "./blank_states_img.gif"
screen.title("U.S. States Game")
screen.setup(width=730, height=506)
screen.addshape(image)
t.shape(image)

state = t.Turtle()
state.hideturtle()
state.penup()
state.speed("fastest")

data = pandas.read_csv("./50_states.csv")
state_list = data["state"].to_list()
answered_list = []
guess = 0
states_to_learn = []

while len(answered_list) < 50:
    answer = screen.textinput(title=f"{guess}/50 Guess the state",
                              prompt="What is the another state").title()
    if answer == "Exit":
        for state in state_list:
            if state not in answered_list:
                states_to_learn.append(state)
        state_dict = {
            "state": states_to_learn
        }
        df = pandas.DataFrame(state_dict)
        df.to_csv("./states_to_learn.csv")
        break
    if answer in state_list:
        i = state_list.index(answer)
        coordinates = data[data.state == state_list[i]]
        x = int(coordinates.x)
        y = int(coordinates.y)
        state.goto(x, y)
        state.write(state_list[i])
        guess += 1
        answered_list.append(answer)
