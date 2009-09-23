picture = makePicture(pickAFile())
picture2 = makePicture(pickAFile())

show(picture)
bgColor = makeColor(50, 200, 0)
for pixel in getPixels(picture):
  dist = distance(getColor(pixel), bgColor)
  if dist < 70:
     otherPixel = getPixelAt(picture2, getX(pixel), getY(pixel))
     setColor(pixel, getColor(otherPixel))
repaint(picture)
