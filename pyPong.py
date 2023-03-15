#Simple Pong game
#By Thulias


import turtle
import winsound
import random
import time


wn = turtle.Screen()
wn.title("Pong by @thuliast")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Possible ball starting moves
ball_x_start = [-0.3, 0.3]      # Positive value the ball goes from left to right, negative value goes the opposite
ball_y_start = [0.3, 0.4, 0.5]  # Different y values


# Paddle A
paddle_a = turtle.Turtle()  #Object
paddle_a.speed(0)   #Speed of animation of the paddle, not movement speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()  #Object
paddle_b.speed(0)   #Speed of animation of the paddle, not movement speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()  # Object
ball.speed(0)   # Speed of animation of the paddle
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice(ball_x_start) # Every time the game starts, it has a random X axis speed
ball.dy = random.choice(ball_y_start) # Every time the ball moves, it has a random Y axis speed

# Pen (for score)
pen = turtle.Turtle()
pen.speed(0)    # Animation, not move speed
pen.color("white")
pen.penup() # Stop the pen from moving
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor() # Determine the y coordinate where the paddle is
    y += 20 #Increase y to go up
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # Determine the y coordinate where the paddle is
    y -= 20 #Increase y to go up
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # Determine the y coordinate where the paddle is
    y += 20 #Increase y to go up
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # Determine the y coordinate where the paddle is
    y -= 20 #Increase y to go up
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w") # When W is pressed call paddle_a_up function
wn.onkeypress(paddle_a_down, "s") # When s is pressed call paddle_a_down function
wn.onkeypress(paddle_b_up, "Up") # When W is pressed call paddle_b_up function
wn.onkeypress(paddle_b_down, "Down") # When s is pressed call paddle_b_down function



# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290) # Upper border of the screen
        ball.dy *= -1   # Reverse the direction when ball reaches upper border
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290) # Lower border of the screen
        ball.dy *= -1   # Reverse the direction when ball reaches lower border
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390: # When ball "scores" (reaches left or right border) the ball position resets
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # Add 1 to player A score
        pen.clear() # Refresh the screen so that scores don't overexpose themselves
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

    if ball.xcor() < -390: # When ball "scores" (reaches left or right border) the ball position resets
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # Add 1 to player B score
        pen.clear() # Refresh the screen so that scores don't overexpose themselves
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 12, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # Score check. The first player who reaches 20 wins
    if (score_a >= 20) or (score_b >= 20):
        ball.setx(0)    # Stop the ball
        ball.sety(0)
        pen.penup()
        pen.hideturtle()
        pen.goto(0,-260)
        pen.write("GAME OVER!!", align="center", font=("Courier", 20, "normal"))
        time.sleep(5)
        wn.quit()
        