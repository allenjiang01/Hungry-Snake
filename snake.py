from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake_head()
        self.create_snake()
        self.create_snake()

    def create_snake(self):
        s = Turtle()
        s.penup()
        s.shape('square')
        s.color('green')
        s.setpos(self.segments[-1].pos()[0], self.segments[-1].pos()[1])
        s.showturtle()
        self.segments.append(s)
        return s

    def create_snake_head(self):
        s = Turtle()
        s.penup()
        s.shape('square')
        s.color('green')
        s.setpos(0, 0)
        s.showturtle()
        self.segments.append(s)
        return s

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            self.segments[s].setpos(self.segments[s - 1].pos()[0], self.segments[s - 1].pos()[1])
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

