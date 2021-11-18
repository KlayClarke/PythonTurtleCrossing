from turtle import Turtle

FONT = ('Arial', 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=270)
        self.level = 0
        self.write(arg=f'Level: {self.level}', align='center', move=False, font=FONT)

    def update_level(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='center', move=False, font=FONT)

    def add_level(self):
        self.level += 1
        self.update_level()