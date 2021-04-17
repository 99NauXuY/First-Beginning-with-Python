from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
FONT2 = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self, player):
        self.goto(0, 0)
        if player == 1:
            self.write("Player 1 wins!", align=ALIGNMENT, font=FONT2)
        if player == 2:
            self.write("Player 2 wins!", align=ALIGNMENT, font=FONT2)