import random
from turtle import Turtle

COLORS = ['red', 'green', 'orange', 'pink', 'blue', 'purple', 'brown']
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(0, 20)
        if random_chance == 3:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)



