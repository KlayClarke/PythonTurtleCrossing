import time
from car_manager import CarManager
from car import Car
from turtle import Screen
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 290:
        player.reset_position()
        scoreboard.add_level()


    # elif player.distance(car_manager) < 20:
    #     print('splat')
    #     scoreboard.game_over()
    #     game_is_on = False

screen.exitonclick()
