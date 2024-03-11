from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WALL = 280
HEIGHT = 600
WIDTH = 800
screen = Screen()
### prevents paddles starting in center and moving to edge.
screen.tracer(0)
### ^ requires screen.update()
screen.bgcolor('black')
screen.setup(height=HEIGHT, width=WIDTH)
screen.title("🏓 PONG 🏓")
screen.listen()

### paddles
right_paddle = Paddle((350, 0), 'blue')
left_paddle = Paddle((-350,0), 'red')
screen.onkey(right_paddle.move_up_paddle, 'Up')
screen.onkey(right_paddle.move_down_paddle, "Down")
screen.onkey(left_paddle.move_up_paddle, 'w')
screen.onkey(left_paddle.move_down_paddle, "s")

### ball
ball = Ball()
ball.move_ball()

### Scoreboard
scoreboard = ScoreBoard()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > WALL or ball.ycor() < -WALL:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
