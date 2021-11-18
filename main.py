import time
from car_manager import CarManager
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

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print('Splat')
            player.reset_position()
            game_is_on = False

    if player.ycor() > 290:
        player.reset_position()
        scoreboard.add_level()

screen.exitonclick()
