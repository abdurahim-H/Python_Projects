from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.tilt(90)
        self.penup()
        self.go_to_start()
        self.new_y = 0

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y


    def go_to_start(self):
        self.goto(STARTING_POSITION)
