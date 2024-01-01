import random
from turtle import Turtle

class PowerUp(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape("circle")
		self.color("blue")
		self.speed("fastest")
		self.goto(random.randint(-300, 300), random.randint(-300, 300))

