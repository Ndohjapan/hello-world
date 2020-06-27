import turtle
from tkinter import *
import winsound

name = Tk()
name.geometry("400x120")

def destroy():
    names = player1_name.get(), player2_name.get()
    name.destroy()
    win = turtle.Screen()  # This is done make the window
    win.title("DUAL PAD")
    win.setup(width=800, height=600)
    win.bgcolor('yellow')
    win.tracer(0)  # This is to speed up the game a bit by preventing automatic update

    # Pad L

    paddle_a = turtle.Turtle()  # To make a turtle object
    paddle_a.speed(0)
    paddle_a.shape('square')
    paddle_a.color('orange')
    paddle_a.shapesize(stretch_len=1, stretch_wid=5)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Pad R

    paddle_b = turtle.Turtle()  # To make a turtle object
    paddle_b.speed(0)
    paddle_b.shape('square')
    paddle_b.color('blue')
    paddle_b.shapesize(stretch_len=1, stretch_wid=5)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('orange')
    ball.shapesize(stretch_wid=1)
    ball.penup()
    ball.dx = 0.3  # THis is to set the rate of change in position of the ball ini the x-coordinate
    ball.dy = 0.3 #This will set the rate of change in position of ball in the y-coordinate

    # Score Board
    score_a = 0
    score_b = 0
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.color("black")
    score.hideturtle()
    score.goto(0, 260)
    score.write(f"{names[0]}:{score_a} {names[1]}:{score_b}", align="center", font=("Courier", 24, "bold"))

    # y movement
    def paddle_a_path_up():
        y = paddle_a.ycor()
        if paddle_a.ycor() + 20 > 260:
            paddle_a.goto(-350, 0)
        # The above will collect the y coordinate of paddle_a
        else:
            y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        if paddle_a.ycor() - 20 < -250:
            paddle_a.goto(-350, 0)
        else:
            y -= 20
        paddle_a.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        if paddle_b.ycor() - 20 < -250:
            paddle_b.goto(350, 0)
        # The above will collect the y coordinate of paddle_a
        else:
            y -= 20
        paddle_b.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        if paddle_b.ycor() + 20 > 260:
            paddle_b.goto(350, 0)
        # The above will collect the y coordinate of paddle_a
        else:
            y += 20
        paddle_b.sety(y)

    # keyboard binding
    win.listen()
    win.onkeypress(paddle_a_path_up, 'w')
    win.onkeypress(paddle_a_down, 's')
    win.onkeypress(paddle_b_up, 'Up')
    win.onkeypress(paddle_b_down, 'Down')
    while True:
        # Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking to see what happens when the ball hits the border
        if ball.ycor() > 280:
            ball.sety(280)
            ball.dy *= -1

        if ball.xcor() > 372:
            ball.goto(0, 0)
            ball.dx *= -1
            score.clear()
            score_a += 1
            score.write(f"{names[0]}:{score_a} {names[1]}:{score_b}", align="center", font=("Courier", 24, "bold"))

        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1

        if ball.xcor() < -372:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            score.clear()
            score.write(f"{names[0]}:{score_a} {names[1]}:{score_b}", align="center", font=("Courier", 24, "bold"))


        # Hitting the paddle_a
        if (-320 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
            ball.dx *= -1
            """winsound.PlaySound("Soft-lounge-background-track.mp3", winsound.SND_ASYNC)
                The above will play the sound in the folder when the ball hits the paddle
                """
            winsound.Beep(2000, 100)

            # Hitting the paddle_b
        if (320 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
            ball.dx *= -1
            winsound.Beep(2000, 100)
        win.update()


player_name = Label(name, text="Enter Your Name", font=("Consolas", 16, "bold"))
player_name.grid(row=0, column=1, columnspan=2)
player1 = Label(name, text="Player1", font=("Consolas", 16, "bold"))
player1.grid(row=1, column=0, padx=10)
player1_name = Entry(name, font=("Courier", 16))
player1_name.grid(row=1, column=1)
player1_name.focus()
player2 = Label(name, text="Player2", font=("Consolas", 16, "bold"))
player2.grid(row=2, column=0)
player2_name = Entry(name, font=("Courier", 16))
player2_name.grid(row=2, column=1)
ok_btn = Button(name, text="OK", command=destroy, padx=12)
ok_btn.grid(row=3, column=1, columnspan=2, ipadx=100)
name.mainloop()
