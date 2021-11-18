import turtle
from turtle import Turtle, Screen

PLAYER_START_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.goto(PLAYER_START_POSITION)

    def player_move_up(self):
        new_y_value = self.ycor() + 20
        self.goto(self.xcor(), new_y_value)


