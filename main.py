import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkey(player.player_move_up(), key='Up')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
