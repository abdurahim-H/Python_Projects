import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = turtle.Turtle()

data_s = pandas.read_csv("50_states.csv")

length = len(data_s["state"])
c_gues = 0

answer_state = screen.textinput(title=f"{c_gues}/{length} Correct Guess", prompt="What's another state's name?").title()


print(length)

if answer_state in data_s["state"].values:
    state_data = data_s[data_s["state"] == answer_state]
    pen.penup()
    pen.goto(int(state_data["x"]), int(state_data["y"]))
    pen.pendown()
    pen.write(answer_state, font=("Arial", 9, "normal"))
    data_s = data_s[data_s["state"] != answer_state]
    length = len(data_s)
    c_gues += 1






screen.exitonclick()