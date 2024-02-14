from turtle import Turtle
import random

class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 10
        self.y_move = 10






    def go_ball(self):
         x = self.xcor() + self.x_move
         y = self.ycor() + self.y_move
         self.goto(x,y)

    def reflect(self):
        self.y_move *= -1
    def paddle_re(self):
        self.x_move *= -1



