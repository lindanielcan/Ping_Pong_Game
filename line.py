from turtle import Turtle

class DashedLine():
    """
    This class draws a dashed line to represent the ping-pong table net.
    """
    def __init__(self):
        self.line = Turtle()
        self.line.color('white')
        self.line.hideturtle()
        self.line.penup()
        self.line.sety(-175)
        self.draw_line()

    def draw_line(self):
        """
        This function draws the dashed line.
        """
        for x in range(0, 20):
            self.line.pendown()
            self.line.sety(self.line.ycor()+10)
            self.line.penup()
            self.line.sety(self.line.ycor()+10)