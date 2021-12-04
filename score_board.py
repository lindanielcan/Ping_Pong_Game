import turtle


class ScoreBoard():
    """
    This class constructs and manages the score board.
    """
    def __init__(self, x_cor, y_cor):
        self.score = turtle.Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color('white')
        self.score.setx(x_cor)
        self.score.sety(y_cor)
        self.player_score = 0
        self.score.write(f'Score: {self.player_score}', font=('Ariel', 8, 'normal'))

    def update_score_board(self, new_score):
        """
        This function sets the score on the score board.
        """
        self.score.clear()
        self.score.write(f'Score: {new_score}', font=('Ariel', 8, 'normal'))
