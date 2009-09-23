def createCollageNIH():
  """Create and show a picture, with five flower stiched on to it"""
  flower1 = openImage("flower1.jpg")
  flower2 = openImage("flower2.jpg")
  canvas = openImage("640x480.jpg")

  drawImageAtBottom(flower1, canvas, 1)

  drawImageAtBottom(flower2, canvas, 100)

  alterColor(flower1, invert)
  drawImageAtBottom(flower1, canvas, 200)

  alterColor(flower2, noBlue)
  drawImageAtBottom(flower2, canvas, 300)

  #notice the flower1 is already inverted
  alterColor(flower1, reduceRed) 
  drawImageAtBottom(flower1, canvas, 400)

  show(canvas)
  return canvas

def openImage(imagename):
  """Open and print a picture"""
  picture = makePicture(getMediaPath(imagename))
  print picture
  return picture

def drawImageAtBottom(src, dst, x):
  """Draw draw the source image, in the bottom
     of the destination image"""
  copyInto(src, dst, x, getHeight(dst)-getHeight(src)-5)

def alterColor(picture, colorFunction):
  """Change the colors of a picture by apply the colorFunction
     to the colors of the picture"""
  for px in getPixels(picture):
    setColor(px,colorFunction(getRed(px), getGreen(px), getBlue(px)))

def noBlue(red, green, blue):
  """Color without blue component"""
  return makeColor(red,green,0)

def invert(red, green, blue):
  """Inverted color"""
  return makeColor( 255-red, 255-green, 255-blue)

def reduceRed(red, green, blue):
  """Color with red component reduced to 50%"""
  return makeColor( red / 2, green, blue)
