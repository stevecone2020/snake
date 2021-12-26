from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}, HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.check_high_score()
        self.save_high_score()

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.goto(0, -20)
            self.write(f"You got a new high score of {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def load_high_score(self):
        with open ("data.txt") as self.file:
            self.high_score = int(self.file.read())
            return self.high_score

    def save_high_score(self):
        with open("data.txt", mode="w") as self.file:
            self.file.write(str(self.high_score))
