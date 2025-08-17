from turtle import Turtle
MOVE_DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        """
        Inizializzazione della classe Snake:
        crea i segmenti e assegna il primo segmento come testa.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # la testa è il primo segmento

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        #aggiunge un nuovo segmento al serpente
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Fa muovere il serpente di 20 pixel in avanti
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    # def increase_snake(self):
