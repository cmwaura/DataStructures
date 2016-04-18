import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def draw_spiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        draw_spiral(myTurtle, lineLen-5)
draw_spiral(myTurtle, 200)
myWin.exitonclick()
