import turtle

turtle.speed("fastest")
str = "frrfrrf"
for _ in range(5):
    str = str.replace('f', 'flfrrflf')

for l in str:
    if l == 'r':
        turtle.right(60)
    elif l == 'l':
        turtle.left(60)
    elif l == 'f':
        turtle.forward(2)

turtle.done()
