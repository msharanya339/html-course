import turtle 

pen = turtle.Turtle()
turtle.Screen().bgcolor('black') 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
pen.speed('fastest')
pen.hideturtle()

for x in range(200): 
    pen.pencolor(colors[x%len(colors)])
    pen.width(x/100 + 1)
    pen.forward(x) 
    pen.left(59)
  
turtle.done()  