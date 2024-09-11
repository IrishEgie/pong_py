from turtle import Turtle, Screen
from paddle import Paddle
import time

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


turtle = Turtle()

screen = Screen()
screen.setup(width=900, height=600)
screen.title("Pong")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)
screen_height = abs(screen.window_height())/2
screen_width = abs(screen.window_width()/2)



# dash()
# Create paddle on the right side of the screen
paddle = Paddle(x_pos=390, y_pos=0)
screen.update()


screen.exitonclick()


