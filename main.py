import time
from cars import Cars
from turtle import Screen
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)

player = Player()

car = Cars()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 290:
        player.reset_position()
        scoreboard.add_level()

screen.exitonclick()
