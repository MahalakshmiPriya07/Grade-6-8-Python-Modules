import turtle  # Importing the turtle library

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color of the window

turtle.speed(1)  # Set the turtle speed to maximum
turtle.width(2)  # Set the pen width

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']  # Define a list of colors

# Draw a colorful spiral
for i in range(100):
    turtle.pencolor(colors[i % len(colors)])  # Change the pen color
    turtle.circle(5 * i)  # Draw a circle with radius 5*i
    turtle.circle(-5 * i)  # Draw a circle with radius -5*i
    turtle.left(i)  # Turn the turtle left by i degrees

# Wait for a click to close the window
turtle.exitonclick()
