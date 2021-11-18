from turtle import Turtle


x_position = 0
y_position = -280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.goto(x=x_position, y=y_position)

    def go_up(self):
        new_y_position = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_position)

    def reset_position(self):
        self.goto(x_position, y_position)

