from turtle import Turtle


class Paddle():
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.color('white')
        self.paddle.hideturtle()
        self.paddle.penup()
        self.paddle.shape('square')
        self.paddle.shapesize(4, 1, 1)

    def set_paddle_position(self, x, y):
        self.paddle.setx(x)
        self.paddle.sety(y)
        self.paddle.showturtle()

    def move_up(self):
        if self.paddle.ycor() != 135:
            self.paddle.sety(self.paddle.ycor() + 5)
        print(self.paddle.ycor(), self.paddle.ycor())

    def move_down(self):
        if self.paddle.ycor() != -125:
            self.paddle.sety(self.paddle.ycor() - 5)
        #print(self.paddle.ycor(), self.paddle.ycor())

        # x 320 -330
        # y 135 -125

    def get_paddle_y_cor(self):
        return self.paddle.ycor()