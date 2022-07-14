from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-5, 270)
        self.write(f"Score: {self.score}", align='center', font=('times new roman', 15, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('times new roman', 15, 'normal'))

    def game_over(self):
        self.color('white')
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.write("GAME OVER, PRESS SPACE TO RESTART", align='center', font=('times new roman', 20, 'normal'))