from turtle import Turtle
import random


class Ball():
    """
    This class constructs and manages a ping pong ball.
    """
    def __init__(self):
        self.ball = Turtle()
        self.ball.hideturtle()
        self.ball.shape('circle')
        self.ball.color('red')
        self.ball.penup()
        self.ball.sety(40)
        self.ball.setx(40)
        self.ball.showturtle()

    def run_ball(self, left_y_cor, right_y_cor):
        """
        This function makes the ball run.
        """
        self.ball_hit_wall()
        self.ball_hit_paddle(left_y_cor, right_y_cor)
        self.ball.forward(3)

    def ball_hit_wall(self):
        """
        This function checks if the ball hits the wall or not, if the ball hits the wall, it changes its heading.
        """
        if 163 <= int(self.ball.ycor()) <= 166:
            self.ball.setheading(360 - self.ball.heading())
        if -159 <= int(self.ball.ycor()) <= -155:
            self.ball.setheading(360 - self.ball.heading())

    def ball_hit_paddle(self, left_y_cor, right_y_cor):
        """
        This function checks if the paddle hits the ball, if the ball was hit by the paddle, it changes its heading.
        """
        if 298 <= int(self.ball.xcor()) <= 300:
            if int(right_y_cor - 38) < int(self.ball.ycor()) < int(right_y_cor + 38):
                self.ball.setheading(360 - self.ball.heading() + 180)
        elif -309 <= int(self.ball.xcor()) <= -307:
            if int(left_y_cor - 38) < int(self.ball.ycor()) < int(left_y_cor + 38):
                self.ball.setheading(360 - self.ball.heading() + 180)

    def reset_ball_position_and_heading(self, heading):
        """
        This function resets a new position and a new heading for the ball.
        """
        self.ball.setx(0)
        self.ball.sety(0)
        self.ball.setheading(random.choice(heading))

    def left_ball_missed(self):
        """
        If the left player missed the ball, then the function will return True
        :return: True
        """
        if self.ball.xcor() >= 350:
            return True

    def right_ball_missed(self):
        """
        If the right player missed the ball, then the function will return True
        :return: True
        """
        if self.ball.xcor() <= -350:
            return True
