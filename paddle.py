from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,side):
        super().__init__()

        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(1, 5)
        self.left(90)
        self.penup()


        self.side = side.lower()
        self.pad_pos()

    def pad_pos(self):

        if self.side == "r":
            self.goto(300,0)
        else:
            self.goto(-300,0)





