# import random
# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# turtle.colormode(255)
# print(timmy.shape("classic"))
# timmy.speed("fastest")
# timmy.hideturtle()
#
# color_list = [
#      (198, 13, 32), (248, 236, 25), (40, 76, 188),
#      (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
#      (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31),
#      (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
#      (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168),
#      (93, 233, 198), (65, 231, 239), (217, 88, 51)
# ]
#
# for i in range (-160, 240, 40):
#      for k in range (-160, 240, 40):
#           timmy.penup()
#           timmy.goto(k, i)
#           timmy.pendown()
#           timmy.dot(20, random.choice(color_list))
#
# screen = Screen()
# screen.exitonclick()

import random
import turtle
from turtle import Turtle, Screen

def draw_dot(turtle, x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(20, color)

timmy = Turtle()
turtle.colormode(255)
timmy.shape("classic")
timmy.speed("fastest")
timmy.hideturtle()

color_list = [
     (198, 13, 32), (248, 236, 25), (40, 76, 188),
     (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
     (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31),
     (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
     (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168),
     (93, 233, 198), (65, 231, 239), (217, 88, 51)
]

points = [(x, y) for x in range(-160, 240, 40) for y in range(-160, 240, 40)]
colors = random.choices(color_list, k=len(points))

for point, color in zip(points, colors):
    draw_dot(timmy, *point, color)

screen = Screen()
screen.exitonclick()