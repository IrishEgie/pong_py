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
        self.x_move = random.choice([10, -10])  # Random initial x direction
        self.y_move = random.choice([10, -10])  # Random initial y direction
        self.move_speed = 0.1
        self.paddle_hit_cooldown = 0  # New cooldown attribute

    def move_ball(self):
        """Moves the ball across the screen with edge and paddle collision."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.edge_collision()

        if self.paddle_hit_cooldown > 0:
            self.paddle_hit_cooldown -= 1  # Decrease cooldown timer

    def edge_collision(self):
        """Detects collision with top and bottom screen edges."""
        if self.ycor() >= self.sc_height - 10:  # Top edge collision
            self.y_move *= -1  # Reverse vertical direction
        elif self.ycor() <= -self.sc_height + 10:  # Bottom edge collision
            self.y_move *= -1  # Reverse vertical direction

    def paddle_collision(self, paddle):
        """Detects collision with the paddle and reverses horizontal direction."""
        paddle_top = paddle.ycor() + 40  # Paddle's top edge
        paddle_bottom = paddle.ycor() - 40  # Paddle's bottom edge
        paddle_left = paddle.xcor() - 5  # Paddle's left edge
        paddle_right = paddle.xcor() + 5  # Paddle's right edge

        # Check if the ball is within the paddle's horizontal and vertical bounds
        if (paddle_left <= self.xcor() <= paddle_right) and (paddle_bottom <= self.ycor() <= paddle_top):
            if self.paddle_hit_cooldown == 0:
                self.x_move *= -1  # Reverse horizontal direction
                self.move_speed *= 0.9  # Increase speed after paddle hit
                self.paddle_hit_cooldown = 10  # Add cooldown for 10 frames

                # Ensure the ball moves slightly away from the paddle after the collision
                if self.x_move > 0:
                    self.setx(self.xcor() + 10)
                else:
                    self.setx(self.xcor() - 10)

    def reset_position(self):
        """Resets the ball to the center of the screen and gives a random direction."""
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset speed
        self.x_move = random.choice([10, -10])  # Randomize x direction
        self.y_move = random.choice([10, -10])  # Randomize y direction
