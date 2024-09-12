from turtle import Turtle

FONT = ('Courier', 30, 'bold')
class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.goto(pos, 250)
        self.hideturtle()
        self.color("white")
        self.SCORE = -1
        self.write_score()

    def write_score(self):
        self.clear()
        self.SCORE +=1
        self.write(f"{self.SCORE} ", move=False, align='center', font=FONT)
        return self.SCORE