# A Simple Pong Game
# Franoll Fnatu
# September 13th, 2023


import turtle 




# Setting up the Main Screen
wn = turtle.Screen()
wn.title("Pong by Franoll Fantu")
wn.bgcolor("Black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 4
ball.dy = 4

# Pen for the Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-10, 260)
pen.write(f"Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y += -20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y += -20
    pad_b.sety(y)
    
# Setting the movement Keys
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")


# Main loop
while True:
    wn.update()

    # How the Ball moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Setting up the Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Win Message
    if score_a  == 7:
        wina = turtle.Turtle()
        wina.speed(0)
        wina.color("white")
        wina.penup()
        wina.hideturtle()
        wina.goto(-10, 260)
        pen.clear()
        wina.write(f"Congratulations! Player A Wins!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = 0
        ball.dy = 0
        pena = turtle.Turtle()

    # Drawing a Blue "A" for the winner IF Player A wins
        pena.goto(-90,0)
        pena.pensize(20)
        pena.forward(30)
        pena.color("Blue")
        pena.forward(130)
        pena.right(45)
        pena.forward(50)
        pena.back(150)
        pena.right(90)
        pena.forward(150)

    if score_b  == 7:
        winb = turtle.Turtle()
        winb.speed(0)
        winb.color("white")
        winb.penup()
        winb.hideturtle()
        winb.goto(-10, 260)
        pen.clear()
        winb.write(f"Congratulations! Player B Wins!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx = 0
        ball.dy = 0
        


# Paddle V.S. Ball
    
    # Basically, if the ball x and y cord matches up with either paddle a or paddle b make it bounce off
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


   
