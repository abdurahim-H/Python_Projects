from turtle import Turtle

from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("Verdana", 15, "normal")

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.goto(0, 280)
		self.color("white")
		self.current_score = 0
		try:
			with open("high_score.txt", "r") as f:
				self.high_score = int(f.read())
		except ValueError:
			self.high_score = 0
		self.score_display()

	def game_over(self):
		if self.current_score - 1 > self.high_score:
			self.high_score = self.current_score - 1
			with open("high_score.txt", "w") as f:
				f.write(str(self.high_score))
		self.goto(0, 0)
		self.clear()
		self.write(f"GAME OVER WITH SCORE OF {self.current_score - 1}", align=ALIGNMENT, font=FONT)

	def score_display(self):
		self.clear()
		self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
		self.current_score += 1