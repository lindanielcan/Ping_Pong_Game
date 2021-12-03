from ball import Ball
from turtle import Screen
from line import DashedLine
from paddle import Paddle
import time
from random import randint

class Game():
    def __init__(self):
        self.ball = Ball()
        self.line = DashedLine()
        self.left_paddle = Paddle()
        self.right_paddle = Paddle()
        self.window = Screen()
        self.window.title('Ping Pong Game')
        self.window.bgcolor('black')
        self.window.setup(width=700, height=350)


    def run_game(self):
        time.sleep(0.1)
        self.event_listener()
        self.left_paddle.set_paddle_position(-330, 0)
        self.right_paddle.set_paddle_position(320, 0)
        self.ball.ball.setheading(randint(0, 360))

        while True:
            self.ball.set_ball_heading(self.left_paddle.get_paddle_y_cor(), self.right_paddle.get_paddle_y_cor())

        self.window.exitonclick()


    def event_listener(self):
        self.window.onkeypress(self.left_paddle.move_up, 'w')
        self.window.onkeypress(self.left_paddle.move_down, 's')
        self.window.onkeypress(self.right_paddle.move_up, 'Up')
        self.window.onkeypress(self.right_paddle.move_down, 'Down')

        self.window.listen()
