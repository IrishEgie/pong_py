from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball 
import time
turtle = Turtle()
def dash():
    turtle.penup()
    turtle.hideturtle()
    turtle.pensize(5)
    turtle.goto(0, -270)
    turtle.setheading(90)
    turtle.color("white")
    run_dash = True
    while run_dash:
        if turtle.ycor() < screen_height:
            run_dash = True
        else: 
            run_dash = False
            print("Dash is finished")

        turtle.pendown()
        turtle.forward(25)
        turtle.penup()
        turtle.forward(25)

def edge_collision(paddle):
    """Ensures the paddle does not move beyond the screen's top or bottom edge."""
    if paddle.ycor() >= screen_height - 50:  # Restrict moving beyond top
        paddle.sety(screen_height - 50)
    elif paddle.ycor() <= -screen_height + 50:  # Restrict moving beyond bottom
        paddle.sety(-screen_height + 50)

screen = Screen()
screen.setup(width=900, height=600)
screen.title("Pong")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen_height = abs(screen.window_height())/2
screen_width = abs(screen.window_width()/2)

dash()
# Create paddle on the right side of the screen
paddle1 = Paddle(x_pos=-390, y_pos=0)
paddle2 = Paddle(x_pos=390, y_pos=0)
ball = Ball()

# Bind the keys to the paddle movement
screen.listen()
screen.onkeypress(paddle1.start_moving_up, "w")
screen.onkeypress(paddle1.start_moving_down, "s")
screen.onkeyrelease(paddle1.stop_moving_up, "w")
screen.onkeyrelease(paddle1.stop_moving_down, "s")


# You can also add a similar movement and collision for paddle2 if needed
screen.onkeypress(paddle2.start_moving_up, "Up")
screen.onkeypress(paddle2.start_moving_down, "Down")
screen.onkeyrelease(paddle2.stop_moving_up, "Up")
screen.onkeyrelease(paddle2.stop_moving_down, "Down")

game_is_on = True
while game_is_on:

    edge_collision(paddle1)
    edge_collision(paddle2)
    screen.update()

screen.exitonclick()


