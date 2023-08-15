#WAPP to create indian flag.
import turtle

# First Set up the screen

screen = turtle.Screen()

screen.setup(width=580, height=550)
#Name of the Flag
screen.title("Indian Flag")

# Create a turtle object

flag = turtle.Turtle()

# Set the speed and starting position
#flag.begin_fill()
flag.speed(11)
flag.penup()
 #flag.forward(600)
flag.goto(-300, 250)

flag.pendown()
#flag.end_fill()
# Draw the saffron color

# Saffron color
flag.color("#FF9933")  

flag.begin_fill()
#flag.end_fill()
for _ in range(2):
    flag.forward(600)

    flag.right(90)
    flag.forward(100)
    flag.right(90)

flag.end_fill()

# Move to draw the white stripe

flag.penup()

flag.goto(-300, 150)

flag.pendown()

# Draw the white stripe

flag.color("white")
flag.begin_fill()

for _ in range(2):

    flag.forward(600)

    flag.right(90)
    flag.forward(100)

    flag.right(90)
flag.end_fill()

# Move to draw the green stripe


flag.penup()

flag.goto(-300, 50)
flag.pendown()

# Draw the green stripe
# Green color


flag.color("#138808")  
#flag.penup()
flag.begin_fill()
for _ in range(2):
    flag.forward(600)

    flag.right(90)
    flag.forward(100)
    flag.right(90)
flag.end_fill()

# Draw the Ashoka Chakra (Navy Blue Circle)

flag.penup()

flag.goto(0, 50)
flag.pendown()

# Navy Blue color
flag.color("#000080")  
flag.pensize(2)

flag.begin_fill()
flag.circle(50)

#flag.end_fill()

# Draw the 24 spokes of the Ashoka Chakra
for _ in range(24):
    flag.penup()
    flag.goto(0, 100)
    flag.pendown()
    flag.forward(50)
    flag.backward(50)
    flag.left(15)

# Hide the turtle
flag.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()
