🐢 Turtle Race Game 🏁 

This is a simple and fun game built with Python's turtle module. The game allows you to bet on a colored turtle and watch as the turtles race across the screen.

🎮 How to Play

When you run the game, a prompt will appear asking you to guess which colored turtle will win the race. Enter the color of your choice and watch the race unfold!

📸 Game Screenshot
![Game Screenshot](https://i.imgur.com/t7HqiOf.png)

💻 Code Snippet
Here's a small snippet from the game code:


```python
for i in range (0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(-232, y_position[i])
    all_turtles.append(new_turtle)
```

This code creates six turtles, each with a different color, and places them at different positions on the y-axis.

🎨 Customizing the Turtles

You can customize the appearance of the turtles in the game. Here's how you can change the shape of the turtles:

```python
new_turtle.shape("circle") # changes the turtle shape to a circle
```

You can also change the size of the turtles:

```python
new_turtle.shapesize(2, 2) # changes the turtle size to twice the original size
```

🏆 Winning the Game

The game continues until one of the turtles crosses the finish line. If the winning turtle's color matches your bet, you win!

```python
if turtle.xcor() > 230:
	is_race_on = False
	winning_color = turtle.pencolor()
	if winning_color == user_bet:
		print(f"Congratulations, Your bet: {winning_color} won the game! ")
	else:
		print(f"Unfortunately, Your bet: {user_bet} lost the game! ")
```

🚪 Exiting the Game

To exit the game, simply click anywhere on the game screen.

```python
screen.exitonclick()
```

🎉 Enjoy the Game!

We hope you enjoy playing this simple and fun turtle race game. Happy betting and may the best turtle win!