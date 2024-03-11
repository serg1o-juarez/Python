from turtle import Turtle
FONT = ('courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-280,y=260)
        self.write(f'Level: {self.score}', align='left', font=FONT)

    def clear_level(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color('red')
        self.write(f"GAME OVER", align="center", font=("Times New Roman", 50, 'bold'))
