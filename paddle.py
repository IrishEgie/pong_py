from turtle import Turtle, Screen
screen = Screen()
rep = 25
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.goto(x_pos, y_pos)
        self.move_speed = 30
        self.moving_up = False
        self.moving_down = False

    def move_up(self):
        """Move the paddle up continuously while 'w' is pressed."""
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
            screen.ontimer(self.move_up, rep)  # Repeat every 50ms

    def move_down(self):
        """Move the paddle down continuously while 's' is pressed."""
        if self.moving_down:
            new_y = self.ycor() - self.move_speed
            self.goto(self.xcor(), new_y)
            screen.ontimer(self.move_down, rep)

    def start_moving_up(self):
        """Start moving the paddle up."""
        self.moving_up = True
        self.move_up()

    def start_moving_down(self):
        """Start moving the paddle down."""
        self.moving_down = True
        self.move_down()

    def stop_moving_up(self):
        """Stop moving the paddle up when the key is released."""
        self.moving_up = False

    def stop_moving_down(self):
        """Stop moving the paddle down when the key is released."""
        self.moving_down = False

    