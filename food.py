from turtle import Turtle
import random

FOOD_SIZE_SCALE = 0.5

TURTLE_SIZE = 20

random.seed()


class Food(Turtle):

    def __init__(self, screen_size_width, screen_size_height):
        super().__init__(shape="circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=FOOD_SIZE_SCALE, stretch_len=FOOD_SIZE_SCALE)

        self.screen_width = screen_size_width
        self.screen_height = screen_size_height
        self.new_location()

    def new_location(self):
        x_max_abs = int(self.screen_width / 2 - (TURTLE_SIZE / 2))
        y_max_abs = int(self.screen_height / 2 - (TURTLE_SIZE / 2))
        x_coordinate = random.randint(-x_max_abs, x_max_abs)
        y_coordinate = random.randint(-y_max_abs, y_max_abs)
        self.goto(x=x_coordinate, y=y_coordinate)
