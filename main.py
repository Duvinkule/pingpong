from turtle import Turtle,Screen
from paddle import  Paddle
from pong import Pong
from score import Scoreboard
import  time

screen = Screen()
score = Scoreboard()
screen.setup(width=800,height=600)
screen.listen()
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
paddle_1 = Paddle("r")
paddle_2 = Paddle("l")
ball = Pong()

game_on = True

def go_up_1():
    paddle_1.forward(30)
def go_up_2():
    paddle_2.forward(30)
def go_back_1():
    paddle_1.back(30)
def go_back_2():
    paddle_2.back(30)
screen.onkey(go_up_1,"Up")
screen.onkey(go_back_1,"Down")
screen.onkey(go_up_2,"w")
screen.onkey(go_back_2,"s")


while game_on:

    time.sleep(0.09)
    screen.update()
    ball.go_ball()
    if (ball.distance(paddle_1) < 55) or (ball.distance(paddle_2) < 55):

        ball.paddle_re()
        score.point()


    elif((ball.ycor() < -300) or (ball.ycor() > 300)):
        ball.reflect()



    elif((ball.xcor() < -400) or (ball.xcor() > 400)):
        score.game_over()
        game_on = False











screen.exitonclick()