from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, sc_width, sc_height):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.sc_width = sc_width
        self.sc_height = sc_height
      
      # Ball coordinate, speed & paddle cooldown properties
        self.x_move = random.choice([15,-15])
        self.y_move = random.choice([15,-15])
        self.move_speed = 0.075
        self.paddle_hit_cooldown = 0


        self.last_touch = None  # Tracks the last paddle that touched the ball

    def move_ball(self):
        """Moves the ball across the screen with edge and paddle collision."""
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)
        self.ball_edge_collision()

        if self.paddle_hit_cooldown > 0:
            self.paddle_hit_cooldown -= 1

    def ball_edge_collision(self):
        """Detects collision with top and bottom screen edges."""
        if self.ycor() >= self.sc_height - 10 or self.ycor() <= -(self.sc_height - 10):
            self.y_move *= -1

    def ball_bounce(self):
        """Reverses the horizontal direction of the ball."""
        self.x_move *= -1
        if self.x_move > 0:
            self.setx(self.xcor() + 20)
        else:
            self.setx(self.xcor() - 20)
   
    def paddle_collision(self, paddle1, paddle2):
        """Detects collision with the paddles and reverses horizontal direction."""
        # Paddle 1 (left paddle)
        if self.xcor() < -370:  # Check for left paddle
            if paddle1.ycor() + 40 >= self.ycor() >= paddle1.ycor() - 40:  # Paddle's exact top and bottom
                if self.paddle_hit_cooldown == 0 and self.xcor() <= -310:
                    self.x_move *= -1
                    self.move_speed *= 1
                    self.paddle_hit_cooldown = 10
                    self.last_touch = paddle1  # Record last touch by paddle1
                    
        # Paddle 2 (right paddle)
        elif self.xcor() > 370:  # Check for right paddle
            if paddle2.ycor() + 50 >= self.ycor() >= paddle2.ycor() - 50:  # Paddle's exact top and bottom
                if self.paddle_hit_cooldown == 0 and self.xcor() >= 310:
                    self.x_move *= -1
                    self.move_speed *= 1
                    self.paddle_hit_cooldown = 10
                    self.last_touch = paddle2  # Record last touch by paddle2
                    


    def reset_position(self):
        """Resets the ball to the center of the screen and gives a random direction."""
        self.goto(0, 0)
        self.move_speed = 0.075
        self.x_move = random.choice([15,-15])
        self.y_move = random.choice([15,-15])
        self.paddle_hit_cooldown = 0
        self.last_touch = None  

    def get_last_touch(self):
        """Returns the last paddle that touched the ball."""
        return self.last_touch