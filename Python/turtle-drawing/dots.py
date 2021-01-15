import turtle 

t = turtle.Turtle()

dot_distance = 25
width = 8
height = 4

t.speed(1)
t.penup()

for y in range(height):
    t.dot()
    for i in range(width):
        t.forward(dot_distance)
        t.dot()
    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)
    
turtle.done()