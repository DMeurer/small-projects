import turtle

t=turtle.Pen()
t.hideturtle()
t.turtlesize(10)
t.speed(0)

count = 0
a = 1
x = 10
while count < 23:
    count=count+1
    a = 1
    x = x + 5
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    while a < 80:
        t.forward(8)
        t.right(a)
        a = 1.02 * a

turtle.done()