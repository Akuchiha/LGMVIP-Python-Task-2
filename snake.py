import turtle
import time
import random

# Set up the screen with retro colors and resolution
wn = turtle.Screen()
wn.title("Retro Snake Game")
wn.bgcolor("#6B8E23")  # Dark olive green, for that retro monochrome look
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates for better animation

# Snake Head
head = turtle.Turtle()
head.shape("square")
head.color("black")  # Black color for the snake's head to mimic old Nokia pixel snake
head.shapesize(stretch_wid=1.2, stretch_len=1.2)  # Slightly bigger, more pixelated look
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.shape("square")
food.color("black")  # Same color to match the aesthetic
food.shapesize(stretch_wid=1.2, stretch_len=1.2)  # Larger, blocky appearance
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []

# Score variables
score = 0
high_score = 0

# Pen for score display (simplified, basic font for retro feel)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    # Border wrapping logic
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)


# Control functions
def go_up():
    if head.direction != "down":  # Prevent reversing direction
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")


# Function to reset the game
def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    # Reset the score
    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))


# Game loop
while True:
    wn.update()

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random spot (aligned with the 20x20 grid)
        x = random.randint(-290, 290) // 20 * 20
        y = random.randint(-290, 290) // 20 * 20
        food.goto(x, y)

        # Add a segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("black")  # Same retro black color for snake segments
        new_segment.shapesize(stretch_wid=1.2, stretch_len=1.2)  # Pixelated look
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score

        # Update the score display
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to the position of the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(0.1)  # Control the speed of the game

wn.mainloop()
