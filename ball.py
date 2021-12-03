from turtle import Turtle



class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.hideturtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.sety(40)
        self.ball.setx(40)
        self.ball.showturtle()

    def set_ball_heading(self, left_y_cor, right_y_cor):
        if int(self.ball.ycor()) == 163:
            if 0 <= self.ball.heading() < 90:
                self.ball.setheading(360 - self.ball.heading())
            if 90 <= self.ball.heading() < 180:
                self.ball.setheading(360 - self.ball.heading())
        elif int(self.ball.ycor()) == -156:
            if 180 <= self.ball.heading() < 270:
                self.ball.setheading(360 - self.ball.heading())
            if 270 <= self.ball.heading() < 360:
                self.ball.setheading(360 - self.ball.heading())
        if int(self.ball.xcor()) == 299:
            if int(right_y_cor - 20) < int(self.ball.ycor()) < int(right_y_cor + 20):
                if 0 <= self.ball.heading() < 90:
                    self.ball.setheading(360- self.ball.heading()+180)
                if 270 <= self.ball.heading() < 360:
                    self.ball.setheading(360-self.ball.heading()+180)
        elif int(self.ball.xcor()) == -309:
            if int(left_y_cor - 20) < int(self.ball.ycor()) < int(left_y_cor + 20):
                if 90 <= self.ball.heading() < 180:
                    self.ball.setheading(360- self.ball.heading()+180)
                if 180 <= self.ball.heading() < 270:
                    self.ball.setheading(360- self.ball.heading()+180)
        self.ball.forward(1)

# top = 163 down = -156
# left = -309 right = 299
