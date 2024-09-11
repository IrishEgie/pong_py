from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()  # Prevents drawing when moving
        self.shapesize(stretch_wid=4, stretch_len=.5)  # Paddle size
        self.goto(x_pos, y_pos)  # Position the paddle
