from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorepong import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce("x")

    # Detect miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    # Winner
    if score.l_score == 3:
        game = False
        score.game_over(1)
    elif score.r_score == 3:
        game = False
        score.game_over(2)
screen.exitonclick()