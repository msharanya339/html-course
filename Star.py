import turtle

def draw_triangle(pen, length):
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

turtle.Screen().bgcolor('red')
pen = turtle.Turtle()
draw_triangle(pen, 100)
pen.penup()
pen.forward(100)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.pendown()
draw_triangle(pen, 100)
turtle.dane()
