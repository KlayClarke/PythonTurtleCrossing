from turtle import Turtle
import random

COLORS = ['red', 'green', 'orange', 'pink', 'blue', 'purple', 'brown']
DEFAULT_X_POSITION = 310
Y_POSITIONS = [-210, -170, -130, -90, -50, -10, 30, 70, 110, 150, 190]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=1.5, outline=None)

    def car_move(self):
        new_x_value = self.xcor() - 1
        self.goto(x=new_x_value, y=self.ycor())

    def generate_car(self):
        self.color(random.choice(COLORS))
        random_y_position = random.choice(Y_POSITIONS)
        self.goto(x=DEFAULT_X_POSITION, y=random_y_position)






