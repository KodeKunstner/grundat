import random
pict = makeEmptyPicture(500, 500)
x = getWidth(pict) / 2
y = getHeight(pict) / 2

show(pict)
while 0 < x and x < getWidth(pict) and 0 < y and y < getHeight(pict):
   pixel = getPixelAt(pict, x, y)
   setColor(pixel, makeColor(col2, col, col))
   x = x + random.randint(-1, 1)
   y = y + random.randint(-1, 1)
   repaint(pict)
