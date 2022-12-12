import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = t.Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def collision_with_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return 1

    def collision_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return 1

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]