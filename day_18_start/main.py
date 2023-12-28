import random
from turtle import Turtle, Screen
from random import randint


tim = Turtle()
tim.shape("turtle")
tim.width(10)
tim.speed("fastest")
# for i in range(0, 4):
#     tim.rt(90)
#     tim.forward(60)

# for i in range(3, 11):
#     angle = 360 / i
#     tim.color("#{:06x}".format(randint(0, 0xFFFFFF)))
#     for k in range(0, i):
#         tim.speed('fastest')
#         tim.rt(angle)
#         tim.forward(40)

# angles = [90, 180, 270, 360]
for i in range(200):
    tim.color("#{:06x}".format(randint(0, 0xFFFFFF)))
    angle = randint(0, 360)
    # angle = random.choice(angles)
    tim.setheading(angle)
    tim.speed('fastest')
    tim.forward(30)
#

# for _ in range(0, 360, 5):
#     tim.color("#{:06x}".format(randint(0, 0xFFFFFF)))
#     tim.setheading(_)
#     tim.rt(90)
#     tim.circle(100, 360)
#     tim.rt(90)




# import turtle
#
# screen = turtle.Screen()
# screen.title("Spirograph")
# screen.bgcolor("black")
#
# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("cyan")
# pen.width(2)
#
# big_radius = 100
# small_radius = 40
# distance = 60
#
# for _ in range(0, 360, 5):
#     pen.setheading(_)
#     pen.circle(big_radius)
#     pen.circle(small_radius)
#
#     pen.right(90)
#     pen.circle(distance)
#     pen.left(90)
#
# pen.hideturtle()
# screen.mainloop()










screen = Screen()
screen.exitonclick()