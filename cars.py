from turtle import Turtle
import random

COLORS = ['red', 'green', 'orange', 'pink', 'blue', 'purple', 'brown']


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=3, outline=None)

    def generate_car(self):
        self.color(random.choice(COLORS))


