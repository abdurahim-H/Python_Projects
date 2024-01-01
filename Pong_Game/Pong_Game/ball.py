from turtle import Turtle
import pygame

pygame.mixer.init()

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 3
		self.y_move = 3
		self.move_speed = 0.1
		self.bounce_sound = pygame.mixer.Sound("/Users/abhudulo/Desktop/python_files/Pong_Game/Ponh_Game/archi_sonar_03-108206.mp3")  # Load the bounce sound

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1
		self.bounce_sound.play()  # Play the bounce sound

	def bounce_x(self):
		self.x_move *= -1
		self.move_speed *= 0.9
		self.bounce_sound.play()  # Play the bounce sound

	def reset_position(self):
		self.goto(0, 0)
		self.move_speed = 0.1
		self.bounce_x()