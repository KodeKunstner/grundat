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

############
## Possible to refactor, but forgetting the existence of copyInto function
##
#def drawImageAtBottom(src, dst, targetX):
#  """Draw draw the source image, src, in the bottom
#     of the destination image, dst, starting at
#     a given x position"""
#  for sourceX in range(1,getWidth(src)):
#    targetY=getHeight(dst)-getHeight(src)-5
#    for sourceY in range(1,getHeight(src)):
#      px=getPixel(src,sourceX,sourceY)
#      cx=getPixel(dst,targetX,targetY)
#      setColor(cx,getColor(px))
#      targetY=targetY + 1
#    targetX=targetX + 1

# Refactored with copyInto
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
