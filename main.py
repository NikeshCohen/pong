from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen specifications
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Creating the paddles from the Paddle class
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Creating a ball from the Ball class
ball = Ball()

# Creating a scoreboard from the Scoreboard class
scoreboard = Scoreboard()

# Event listeners
screen.listen()

# Right paddle
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# Left paddle
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

game_running = True

# Game loop
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right-paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left-paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball goes out of bounds

    # Right paddle
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.left_point()

    # Left paddle
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.right_point()


screen.exitonclick()
