from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Algerian", 18,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                content = data.read().strip()
                self.high_score = int(content) if content else 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0
            with open("data.txt", "w") as data:
                data.write("0")
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0,0,)
    #    self.write("Game Over.", align=ALIGMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
