from ball import Ball
from turtle import Screen
from line import DashedLine
from paddle import Paddle
import time
import random
from score_board import ScoreBoard


class Game:
    def __init__(self):
        """
        The game contains a ping-pong ball, two paddles, two score boards, a dashed line represents the table net.
        """
        self.window = Screen()
        self.window.title('Ping Pong Game')
        self.window.bgcolor('black')
        self.window.setup(width=700, height=350)
        self.window.tracer(0)
        self.ball = Ball()
        self.left_player_score_board = ScoreBoard(-70, 150)
        self.left_player_score = 0
        self.right_player_score_board = ScoreBoard(30, 150)
        self.right_player_score = 0
        self.level = 0.03

        self.line = DashedLine()
        self.ball_start_directions = [random.randint(0, 70), random.randint(120, 240),
                                      random.randint(290, 350)]

        self.left_paddle = Paddle()
        self.right_paddle = Paddle()

    def run_game(self):
        """
        The functions makes the game run.
        """
        self.event_listener()

        self.left_paddle.set_paddle_position(-330, 0)
        self.right_paddle.set_paddle_position(320, 0)
        self.ball.ball.setheading(random.choice(self.ball_start_directions))

        while True:
            time.sleep(self.level)
            self.ball.run_ball(self.left_paddle.get_paddle_y_cor(), self.right_paddle.get_paddle_y_cor())

            if self.ball.right_ball_missed():
                self.left_player_score += 1
                self.left_player_score_board.update_score_board(self.left_player_score)
                self.ball.reset_ball_position_and_heading(self.ball_start_directions)
            elif self.ball.left_ball_missed():
                self.right_player_score += 1
                self.right_player_score_board.update_score_board(self.right_player_score)
                self.ball.reset_ball_position_and_heading(self.ball_start_directions)

            self.set_game_level()

            if self.left_player_score == 5 or self.right_player_score == 5:
                game_over = ScoreBoard(-25, 0)
                game_over.score.clear()
                game_over.score.write('Game Over.')
                break
            self.window.update()

        self.window.exitonclick()

    def event_listener(self):
        """
        The function sets listeners for the key pressed.
        """
        self.window.onkeypress(self.left_paddle.move_up, 'w')
        self.window.onkeypress(self.left_paddle.move_down, 's')
        self.window.onkeypress(self.right_paddle.move_up, 'Up')
        self.window.onkeypress(self.right_paddle.move_down, 'Down')

        self.window.listen()

    def set_game_level(self):
        """
        The function resets the game level, every time the player gets to a higher level,
        the speed of the game gets faster.
        """
        if self.left_player_score == 1 or self.right_player_score == 1:
            self.level = 0.025
        elif self.left_player_score == 2 or self.right_player_score == 2:
            self.level = 0.020
        elif self.left_player_score == 3 or self.right_player_score == 3:
            self.level = 0.015
        elif self.left_player_score == 4 or self.right_player_score == 4:
            self.level = 0.01
        elif self.left_player_score == 5 or self.right_player_score == 5:
            self.level = 0.05
