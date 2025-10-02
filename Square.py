import turtle

screen = turtle.Screen()
screen.bgcolor('blue')
screen.setup(400,300)

pen = turtle.Turtle()

for i in range(4):
    pen.forward(100)
    pen.left(90)

turtle.done()

