from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Start screen
start_screen = Turtle()
start_screen.hideturtle()
start_screen.penup()
start_screen.goto(0, 0)
start_screen.write("Welcome to Pong! Press 's' to start.", align="center", font=("Courier", 24, "normal"))

screen.update()

def start_game():
	start_screen.clear()
	game_is_on = True
	while game_is_on:
		screen.update()
		ball.move()

		# Detect collision with wall
		if ball.ycor() > 280 or ball.ycor() < -280:
			ball.bounce_y()

		# Detect collision with paddle
		if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
			ball.bounce_x()

		# Detect R paddle misses
		if ball.xcor() > 380:
			ball.reset_position()
			scoreboard.l_point()

		# Detect L paddle misses:
		if ball.xcor() < -380:
			ball.reset_position()
			scoreboard.r_point()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "d")

start_game()

screen.mainloop()