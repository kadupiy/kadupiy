import turtle

def draw_attractive_design3():
    color = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    pen = turtle.Turtle()
    pen.speed(1000000)
    turtle.bgcolor('black')
    pen.pensize(5)

    for i in range(190):
        pen.color(color[i % 6])
        pen.forward(100)
        pen.left(59)
        pen.forward(50)
        pen.left(91)
        pen.forward(50)
        pen.left(59)
        pen.forward(100)
        pen.right(121)

    pen.hideturtle()

draw_attractive_design3()

turtle.done()


