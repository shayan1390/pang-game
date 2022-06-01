import turtle
import winsound
from random import choice
import os

WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600
Player_A = 0
Player_B = 0

window = turtle.Screen()
window.title("pong")
window.bgcolor("black")
window.setup(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(360, 0)


# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = choice([0.4, -0.4])
ball.dy = choice([0.4, -0.4])



# pen
pen_A = turtle.Turtle()
pen_A.speed(0)
pen_A.color("red")
pen_A.penup()
pen_A.hideturtle()
pen_A.goto(-30, 260)
pen_A.write(f"{Player_A}  |", align="center", font=("Courier", 24, "normal"))

pen_B = turtle.Turtle()
pen_B.speed(0)
pen_B.color("blue")
pen_B.penup()
pen_B.hideturtle()
pen_B.goto(20, 260)
pen_B.write(f"|  {Player_B}", align="center", font=("Courier", 24, "normal"))

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")




# main game loop
while True:
    window.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Player_A += 1
        pen_A.clear()
        pen_A.write(f"{Player_A}  |", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bang.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Player_B += 1
        pen_B.clear()
        pen_B.write(f"|  {Player_B}", align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bang.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 340) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 45):  # and ball.xcor() < 350
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 45):  # and ball.xcor() > -350
        ball.setx(-340)
        ball.dx *= -1


