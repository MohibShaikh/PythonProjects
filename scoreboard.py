from turtle import Turtle

score_x = 0
score_y = 270
FONT = ('Times New Roman', 16, 'italic')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(score_x, score_y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def score_increment(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt', mode='w') as file:
            file.write(f'{self.high_score}')
        self.score = 0
