import turtle
turtle.speed("fastest")

def polyspi(v):
    for n in range(200):
        turtle.forward(n)
        turtle.left(v)

polyspi(94)
turtle.done()
