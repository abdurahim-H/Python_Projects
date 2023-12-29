from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Guess which colored turtle will win the game: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-90, -60, -30, 0, 30, 60]
all_turtles = []

for i in range (0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-232, y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations, Your bet: {winning_color} won the game! ")
            else:
                print(f"Unfortunately, Your bet: {user_bet} lost the game! ")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()