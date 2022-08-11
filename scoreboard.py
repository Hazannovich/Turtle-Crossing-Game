from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.goto(-280, 260)
        self.hideturtle()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over, you reached level: {self.level}", False, "center", FONT)


