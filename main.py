


import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Balls")


ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = -2
ball.dy = 0

gravity = 0.1

while True:

  ball.dy -= gravity
  ball.sety(ball.ycor() + ball.dy)

  #check for a bounch
  if ball.ycor() < -300:
    ball.dy *= -1
