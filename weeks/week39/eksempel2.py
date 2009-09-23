import turtle
turtle.tracer(False)
def spiral_rek(n):
    if n < 200:
        turtle.forward(n * 2)
        turtle.left(90)
        spiral_rek(n + 1)

        
    
spiral_rek(1)
turtle.done()
