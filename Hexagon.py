import turtle

def draw_hexagon(pen, length):
    for _ in range(6):
        pen.forward(length)
        pen.left(60)

turtle.Screen().bgcolor('red')
pen = turtle.Turtle()
draw_hexagon(pen, 100)
pen.penup()
pen.forward(120)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.pendown()
draw_hexagon(pen, 100)
turtle.done()