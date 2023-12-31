import random
from turtle import Turtle


# In your powerup.py
class PowerUp(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.penup()
		self.shapesize(0.5, 0.5)
		self.color("blue")
		self.speed("fastest")
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)
		self.refresh()

	def refresh(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)

# In your main.py
powerup = PowerUp()

# Inside your game loop
if snake.head.distance(powerup) < 15:
	powerup.refresh()
	score.score_display()
	score.current_score += 10  # or any other effect you want the power-up to have