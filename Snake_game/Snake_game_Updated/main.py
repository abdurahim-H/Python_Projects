# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(600, 600)
# screen.bgcolor("black")
# screen.title("The Infamous Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# score = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")


# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         score.score_display()

#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         score.game_over()

#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             score.game_over()

# screen.exitonclick()

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SPEED_INCREASE = 0.01
current_speed = 0.1
lives = 3
game_is_paused = False

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Infamous Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

def toggle_pause():
	global game_is_paused
	game_is_paused = not game_is_paused

def draw_text(text, x, y, size=18):
	pen = Turtle()
	pen.hideturtle()
	pen.penup()
	pen.goto(x, y)
	pen.write(text, align="center", font=("Arial", size, "normal"))

draw_text("Welcome to the Snake Game!", 0, 0)
draw_text("Press any key to start", 0, -20)

def start_game():
	# clear the screen and start the game
	pen.clear()
	# rest of your game setup code

screen.onkey(start_game, "space")
screen.listen()

def game_over():
	draw_text("Game Over", 0, 0)
	draw_text(f"Your final score is: {score.current_score}", 0, -20)

screen.onkey(toggle_pause, "p")

while game_is_on:
	if not game_is_paused:
		screen.update()
		time.sleep(0.1)
		snake.move()

		if snake.head.distance(food) < 15:
			food.refresh()
			snake.extend()
			score.score_display()
			current_speed -= SPEED_INCREASE

		if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
			lives -= 1
			if lives == 0:
				game_is_on = False
				score.game_over()

		for segment in snake.segments[1:]:
			if snake.head.distance(segment) < 10:
				game_is_on = False
				score.game_over()

if not game_is_on:
	game_over()

screen.exitonclick()