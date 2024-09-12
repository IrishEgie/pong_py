from turtle import Turtle, Screen
screen = Screen()
rep = 25
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos, sc_width, sc_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.goto(x_pos, y_pos)
        self.sc_width = sc_width
        self.sc_height = sc_height
        self.move_speed = 30
        self.moving_up = False
        self.moving_down = False
        

    def move_up(self):
        """Move the paddle up continuously while 'w' is pressed."""
        if self.moving_up:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
            self.edge_collision()
            screen.ontimer(self.move_up, rep)  # Repeat every 25ms

    def move_down(self):
        """Move the paddle down continuously while 's' is pressed."""
        if self.moving_down:
            new_y = self.ycor() - self.move_speed
            self.goto(self.xcor(), new_y)
            self.edge_collision()
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

    def listen_keys_1(self):
        screen.listen()
        screen.onkeypress(self.start_moving_up, "w")
        screen.onkeypress(self.start_moving_down, "s")
        screen.onkeyrelease(self.stop_moving_up, "w")
        screen.onkeyrelease(self.stop_moving_down, "s")
    
    def listen_keys_2(self):
        screen.onkeypress(self.start_moving_up, "Up")
        screen.onkeypress(self.start_moving_down, "Down")
        screen.onkeyrelease(self.stop_moving_up, "Up")
        screen.onkeyrelease(self.stop_moving_down, "Down")

    def edge_collision(self):
        """Ensures the paddle does not move beyond the screen's top or bottom edge."""
        if self.ycor() >= self.sc_height - 50:  # Restrict moving beyond top
            self.sety(self.sc_height - 50)
            
        elif self.ycor() <= -self.sc_height + 50:  # Restrict moving beyond bottom
            self.sety(-self.sc_height + 55)
      