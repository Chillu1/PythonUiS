from turtle import Turtle
import turtle

rotation = True
myTurtle = Turtle()
myTurtle.pensize(3)

# Read file
# We use with to automatically close file when done
with open("Oving3/tegne_eksempel.txt") as dataFile:
    while True:
        info = dataFile.readline().strip()  # Remove whitespace
        if not info: # End of file
            break

        if info.isalpha(): # Is a color
            myTurtle.color(info)
            continue

        infoNumber = int(info)
        if rotation:
            myTurtle.right(infoNumber)
            rotation = False
        else:
            if infoNumber < 0:
                myTurtle.penup()
            else:
                myTurtle.pendown()

            myTurtle.forward(infoNumber)
            rotation = True

    turtle.done()