# Sierpinskis trekant
import turtle

def triangle(t, size):
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)

def sierp_triangle(t, size):
    if(size <= 10.0):
        triangle(t, size)
    else:
        sierp_triangle(t, size/2.0)
        t.backward(size)
        sierp_triangle(t, size/2.0)
        t.backward(size)
        sierp_triangle(t, size/2.0)
        t.backward(size)
        t.right(120)


turtle.tracer(False)
sierp_triangle(turtle, 200)
