# import time
# import random
# from turtle import Screen, Turtle
# from player import Player
# import car_manager
# from scoreboard import Scoreboard

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
# screen.listen()

# player = Player()
# level = Scoreboard()

# screen.onkey(player.move_up, "Up")

# game_is_on = True
# counter = 0
# car_generate_rate = 6

# for _ in range(14):
#     car_manager.car_generate(random.randint(-200, 200))

# while game_is_on:
#     time.sleep(0.1)
#     screen.update()

#     if counter % car_generate_rate == 0:
#         car_manager.car_generate()
#     counter += 1

#     for i, car in enumerate(car_manager.car_list):
#         car.move()
#         if player.distance(car) < 22:
#             game_is_on = False

#     if player.is_at_finish_line():
#         level.increase_level()
#         player.go_to_start()
#         car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
#         for car in car_manager.car_list:
#             car.set_speed(car_manager.STARTING_MOVE_DISTANCE)
#         car_generate_rate = max(1, car_generate_rate - 2)
#         print("You've succesfully reaced to the finish line")


# main.py
import time
import random
from turtle import Screen, Turtle
from player import Player
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()  # Instantiate the Scoreboard class
scoreboard.update_scoreboard()  # Update the scoreboard at the start of the game

screen.onkey(player.move_up, "Up")

game_is_on = True
counter = 0
car_generate_rate = 6

for _ in range(14):
    car_manager.car_generate(random.randint(-200, 200))

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % car_generate_rate == 0:
        car_manager.car_generate()
    counter += 1

    for i, car in enumerate(car_manager.car_list):
        car.move()
        if player.distance(car) < 22:
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.increase_level()  # Increase the level
        player.go_to_start()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        for car in car_manager.car_list:
            car.set_speed(car_manager.STARTING_MOVE_DISTANCE)
        car_generate_rate = max(1, car_generate_rate - 2)
        print("You've successfully reached the finish line!")
