from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()  # Prevents drawing when moving
        self.shapesize(stretch_wid=1, stretch_len=1)  # Paddle size
        self.goto(0, 0)  # Position the paddle