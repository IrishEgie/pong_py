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

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen_height = abs(screen.window_height()/2)
screen_width = abs(screen.window_width()/2)

dash()
# Create paddle on the right side of the screen
paddle1 = Paddle(x_pos=-380, y_pos=0, sc_width=screen_width ,sc_height=screen_height )
paddle2 = Paddle(x_pos=375, y_pos=0, sc_width=screen_width ,sc_height=screen_height)
ball = Ball()

game_is_on = True
while game_is_on:
    paddle1.listen_keys_1()
    paddle2.listen_keys_2()
    screen.update()

screen.exitonclick()


