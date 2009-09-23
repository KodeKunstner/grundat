def createCollageGuzdial():
  flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
  flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
  canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas
  #First picture, at left edge
  targetX=1
  for sourceX in range(1,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(1,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Second picture, 100 pixels over
  targetX=100
  for sourceX in range(1,getWidth(flower2)):
    targetY=getHeight(canvas)-getHeight(flower2)-5
    for sourceY in range(1,getHeight(flower2)):
      px=getPixel(flower2,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Third picture, flower1 negated
  negative(flower1)
  targetX=200
  for sourceX in range(1,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(1,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  targetX=300
  for sourceX in range(1,getWidth(flower2)):
    targetY=getHeight(canvas)-getHeight(flower2)-5
    for sourceY in range(1,getHeight(flower2)):
      px=getPixel(flower2,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  #Fifth picture, flower1, negated with decreased red
  decreaseRed(flower1)
  targetX=400
  for sourceX in range(1,getWidth(flower1)):
    targetY=getHeight(canvas)-getHeight(flower1)-5
    for sourceY in range(1,getHeight(flower1)):
      px=getPixel(flower1,sourceX,sourceY)
      cx=getPixel(canvas,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1
  show(canvas)
  return(canvas)

def clearBlue(picture):
  for p in getPixels(picture):
    setBlue(p,0)

def negative(picture):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(px,negColor)

def decreaseRed(picture):
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p,value*0.5)



##################################
# Refactored version, 
# DRY - Dont Repeat Yourself
# docstrings added
##

####
# Utility functions
#

def clearBlue(picture):
  """Set the blue component of an entire picture to 0"""
  for p in getPixels(picture):
    setBlue(p,0)

def negative(picture):
  """Invert a picture"""
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor(px,negColor)

def decreaseRed(picture):
  """Reduce the red component of a picture by 50%"""
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p,value*0.5)


def drawImageAtBottom(src, dst, targetX):
  """Draw draw the source image, src, in the bottom
     of the destination image, dst, starting at
     a given x position"""
  for sourceX in range(1,getWidth(src)):
    targetY=getHeight(dst)-getHeight(src)-5
    for sourceY in range(1,getHeight(src)):
      px=getPixel(src,sourceX,sourceY)
      cx=getPixel(dst,targetX,targetY)
      setColor(cx,getColor(px))
      targetY=targetY + 1
    targetX=targetX + 1

####
# The main example

def createCollageDRY():
  """Create and show a picture, with five flower stiched on to it"""
  flower1=makePicture(getMediaPath("flower1.jpg"))
  print flower1
  flower2=makePicture(getMediaPath("flower2.jpg"))
  print flower2
  canvas=makePicture(getMediaPath("640x480.jpg"))
  print canvas

  #First picture, at left edge
  drawImageAtBottom(flower1, canvas, 1)

  #Second picture, 100 pixels over
  drawImageAtBottom(flower2, canvas, 100)

  #Third picture, flower1 negated
  negative(flower1)
  drawImageAtBottom(flower1, canvas, 200)

  #Fourth picture, flower2 with no blue
  clearBlue(flower2)
  drawImageAtBottom(flower2, canvas, 300)

  #Fifth picture, flower1, negated with decreased red
  decreaseRed(flower1)
  drawImageAtBottom(flower1, canvas, 400)

  show(canvas)
  return(canvas)






##################################
# Further refactored version, 
# Smarter color alteration functions (advanced stuff)
# NIH - Not Invented Here - using existing copyInto function
# instead of rewriting it ourselves


#####
# Color functions, used for making a new color based on the current red,
# green and blue color components. These functions are meant to be 
# applied to the colors of all the pixels in a picture.
 
def noBlue(red, green, blue):
  """Color without blue component"""
  return makeColor(red,green,0)

def invert(red, green, blue):
  """Inverted color"""
  return makeColor( 255-red, 255-green, 255-blue)

def reduceRed(red, green, blue):
  """Color with red component reduced to 50%"""
  return makeColor( red / 2, green, blue)

#####
# Function to apply a color function to all of the pixels in a picture
def alterColor(picture, colorFunction):
  """Change the colors of a picture by apply the colorFunction
     to the colors of the picture"""
  for px in getPixels(picture):
    setColor(px,colorFunction(getRed(px), getGreen(px), getBlue(px)))

#####
# Other utility functions

def drawImageAtBottom(src, dst, targetX):
  """Draw draw the source image, in the bottom
     of the destination image"""
  copyInto(src, dst, targetX, getHeight(dst)-getHeight(src)-5)

def openImage(imagename):
  """Open and print a picture"""
  picture = makePicture(getMediaPath(imagename))
  print picture
  return picture

#####
# The create collage function itself,
# refactored
def createCollageNIH():
  """Create and show a picture, with five flower stiched on to it"""

  flower1 = openImage("flower1.jpg")
  flower2 = openImage("flower2.jpg")
  canvas = openImage("640x480.jpg")

  #First picture, at left edge
  drawImageAtBottom(flower1, canvas, 1)

  #Second picture, 100 pixels over
  drawImageAtBottom(flower2, canvas, 100)

  #Third picture, flower1 negated
  alterColor(flower1, invert)
  drawImageAtBottom(flower1, canvas, 200)

  #Fourth picture, flower2 with no blue
  alterColor(flower2, noBlue)
  drawImageAtBottom(flower2, canvas, 300)

  #Fifth picture, flower1, negated with decreased red
  alterColor(flower1, reduceRed) #notice the flower1 is already inverted
  drawImageAtBottom(flower1, canvas, 400)

  show(canvas)
  return canvas
