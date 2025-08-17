from turtle import Turtle
from ball import Ball
USER_PADDLE_START_POSITION = [(-340, 20), (-340, 10), (-340, 0), (-340, -10), (-340, -20), (-340, -30)]
PC_PADDLE_START_POSITION = [(330, 20), (330, 10), (330, 0), (330, -10), (330, -20), (330, -30)]
GAME_IS_ON = True

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.user_segments = []
        self.pc_segments = []
        self.pc_direction = "up"
        self.create_user_paddle()
        self.create_pc_paddle()
        self.user_head = self.user_segments[0]
        self.user_tail = self.user_segments[5]
        self.pc_head = self.pc_segments[0]
        self.pc_tail = self.pc_segments[5]

    # I create the two game's paddle
    def create_user_paddle(self):
        for position in USER_PADDLE_START_POSITION:
            new_segment = Turtle("square")
            new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.user_segments.append(new_segment)

    def create_pc_paddle(self):
        for position in PC_PADDLE_START_POSITION:
            new_segment = Turtle("square")
            new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.pc_segments.append(new_segment)

    def user_move_up(self):

        # muovi tutti i segmenti verso la posizione del segmento superiore
        if self.user_head.ycor() + 30 < 240:
            for seg_num in range(len(self.user_segments) - 1, 0, -1):
                new_x = self.user_segments[seg_num - 1].xcor()
                new_y = self.user_segments[seg_num - 1].ycor()
                self.user_segments[seg_num].goto(new_x, new_y+50)

            # muovi la testa (primo segmento) verso l’alto
            x = self.user_head.xcor()
            y = self.user_head.ycor() + 60
            self.user_head.goto(x, y)
        else:
            pass

    def user_move_down(self):
        if self.user_tail.ycor() -30 > -230:
            for seg_num in range(len(self.user_segments)-1):
                new_x = self.user_segments[seg_num + 1].xcor()
                new_y = self.user_segments[seg_num + 1].ycor()
                self.user_segments[seg_num].goto(new_x, new_y-50)

            x = self.user_tail.xcor()
            y = self.user_tail.ycor() - 60
            self.user_tail.goto(x, y)
        else:
            pass

    def pc_move_up(self):

        for seg_num in range(len(self.pc_segments) - 1, 0, -1):
            new_x = self.pc_segments[seg_num - 1].xcor()
            new_y = self.pc_segments[seg_num - 1].ycor()
            self.pc_segments[seg_num].goto(new_x, new_y )
        x = self.pc_head.xcor()
        y = self.pc_head.ycor() + 10
        self.pc_head.goto(x, y)

    def pc_move_down(self):
        for seg_num in range(len(self.pc_segments) - 1):
            new_x = self.pc_segments[seg_num + 1].xcor()
            new_y = self.pc_segments[seg_num + 1].ycor()
            self.pc_segments[seg_num].goto(new_x, new_y )

        x = self.pc_tail.xcor()
        y = self.pc_tail.ycor() - 10
        self.pc_tail.goto(x, y)

    def pc_follow_ball(self, ball):
        """Muove il paddle del PC seguendo la palla."""
        if ball.ycor() > self.pc_segments[0].ycor():
            self.pc_move_up()
        elif ball.ycor() < self.pc_segments[-1].ycor():
            self.pc_move_down()


