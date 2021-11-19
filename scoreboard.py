from turtle import Turtle

FONT = ('Arial', 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-150, y=270)
        self.level = 1
        with open('data.txt', mode='r') as data:
            self.high_level = int(data.read())
        self.write(arg=f'Level: {self.level} Highest Level: {self.high_level}' f'', align='center', move=False,
                   font=FONT)

    def update_level(self):
        self.clear()
        if self.level > self.high_level:
            self.high_level = self.level
        with open('data.txt', mode='w') as data:
            data.write(f'{self.high_level}')
        self.write(arg=f'Level: {self.level} Highest Level: {self.high_level}' f'', align='center', move=False,
                   font=FONT)

    def add_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.level = 0
        self.write(arg=f'Level: {self.level} Highest Level: {self.high_level}' f'', align='center', move=False,
                   font=FONT)