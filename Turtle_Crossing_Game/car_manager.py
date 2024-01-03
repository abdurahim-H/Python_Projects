# from turtle import Turtle
# from random import randint


# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
# car_list = []


# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         # self.car_list = None
#         self.shape("square")
#         self.shapesize(stretch_len=2.5, stretch_wid=1.2)
#         self.color(COLORS[randint(0, len(COLORS) - 1)])
#         self.penup()
#         self.goto(250, y=randint(-240, 240))
#         self.speed = STARTING_MOVE_DISTANCE

#     def move(self):
#         self.backward(self.speed)

# def car_generate():
#     new_car = CarManager()
#     car_list.append(new_car)



# car_manager.py
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_list = []

class CarManager(Turtle):
	def __init__(self, x=250):
		super().__init__()
		self.shape("square")
		self.shapesize(stretch_len=2.5, stretch_wid=1.2)
		self.color(COLORS[randint(0, len(COLORS) - 1)])
		self.penup()
		self.goto(x, y=randint(-249, 249))
		self.speed = STARTING_MOVE_DISTANCE

	def move(self):
		self.backward(self.speed)

	def set_speed(self, speed):
		self.speed = speed



def car_generate(x = 250):
	new_car = CarManager(x)
	car_list.append(new_car)

