def grayscaleImage(picture):
    """Convert a picture to black/white"""
    for pixel in getPixels(picture):
        # intensity is the lightness in the picture, 
        # and is the average of the color components
        intensity = (getRed(pixel) + getGreen(pixel) + getBlue(pixel))/3
        setRed(pixel, intensity)
        setGreen(pixel, intensity)
        setBlue(pixel, intensity)

def invertImage(picture):
    """Make the picture negative"""
    for pixel in getPixels(picture):
       # 255 is the maximum intensity of the color,
       # so if we subtract the color intensity from this value
       # we again get a value between 0 and 255
       setRed(pixel, 255 - getRed(pixel))
       setGreen(pixel, 255 - getGreen(pixel))
       setBlue(pixel, 255 - getBlue(pixel))

def addRectWide(picture, x, y, width, height, thickness, color):
    """Draw a rectangle on a picture, with a specified thickness
       and color of the drawn lines in the rectangle."""
    addRectFilled(picture, x, y, width, thickness, color)
    addRectFilled(picture, x, y, thickness, height, color)
    addRectFilled(picture, x + width - thickness, y, thickness, height, color)
    addRectFilled(picture, x, y + height - thickness, width, thickness, color)

def addFrame(picture, x, y, width, height):
    """Draw a picture-frame on an image"""
    frameColor = makeColor(110, 100, 0)
    addRectWide(picture, x, y, width, height, 4, frameColor)   
    addRectWide(picture, x + 5, y + 5, width - 10, height - 10, 2, frameColor)
