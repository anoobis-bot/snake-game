from turtle import Turtle

# Height / width of turtle in pixels
SECTION_PIXEL_SIZE = 20
# Number of starting sections the snake has
STARTING_NUM_SECTIONS = 3

EAST_HEAD = 0
NORTH_HEAD = 90
WEST_HEAD = 180
SOUTH_HEAD = 270


def create_section():
    new_section = Turtle(shape="square")
    new_section.color("white")
    return new_section


class Snake:
    def __init__(self):
        # The snake_body list acts as the snake itself. The snake is made up of square "turtles".
        # I will call each turtle as "section". New turtle objects are appended if the snake size grows.
        # The section below initializes the first STARTING_NUM_SECTIONS sections of the snake.
        # The snake initially points at east (heading == 0)

        self.snake_body = []
        for section_num in range(STARTING_NUM_SECTIONS):
            curr_section = create_section()

            curr_section.penup()

            x_offset = SECTION_PIXEL_SIZE * len(self.snake_body)
            curr_section.backward(x_offset)

            self.snake_body.append(curr_section)
        self.snake_head = self.snake_body[0]

    def add_section(self):
        new_section = create_section()

        tail_end_section = self.snake_body[len(self.snake_body) - 1]
        new_section.goto(x=tail_end_section.xcor(), y=tail_end_section.ycor())

    def move_forward(self):
        for section_index in range(len(self.snake_body) - 1, 0, -1):
            next_section = self.snake_body[section_index - 1]
            self.snake_body[section_index].goto(x=next_section.xcor(), y=next_section.ycor())

        self.snake_head.forward(SECTION_PIXEL_SIZE)

    def up_direction(self):
        if self.snake_head.heading() != SOUTH_HEAD:
            self.snake_head.setheading(NORTH_HEAD)

    def down_direction(self):
        if self.snake_head.heading() != NORTH_HEAD:
            self.snake_head.setheading(SOUTH_HEAD)

    def left_direction(self):
        if self.snake_head.heading() != EAST_HEAD:
            self.snake_head.setheading(WEST_HEAD)

    def right_direction(self):
        if self.snake_head.heading() != WEST_HEAD:
            self.snake_head.setheading(EAST_HEAD)