import turtle

def stjerne(størrelse):
    for i in range(24):
        turtle.forward(størrelse)
        turtle.backward(størrelse)
        turtle.right(15)

def tegn_stjerner(stjerner):
    turtle.speed(0)
    for i in range(4):

        for i in range(stjerner-1):#Ramme
            stjerne(10)
            turtle.penup()
            turtle.forward(30)
            turtle.pendown()


        turtle.right(90)
    turtle.penup()
    turtle.right(45)
    turtle.forward(((stjerner / 2) - 1) * 30*2.1)
    #turtle.forward(stjerner**2 * (3.75**(stjerner/10)))

    turtle.pendown()
    stjerne(((stjerner / 2) - 1) * 30)


if __name__ == "__main__":
    turtle.tracer(0, 0)
    tegn_stjerner(7)
    turtle.update()
    turtle.mainloop()
    input()