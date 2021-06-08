import turtle

def stjerne(størrelse):
    for i in range(24):
        turtle.forward(størrelse)
        turtle.backward(størrelse)
        turtle.right(15)
    turtle.penup()
    turtle.forward(180)
    turtle.pendown()

if __name__ == "__main__":
    stjerne(30)
    stjerne(60)
    stjerne(90)
    input()