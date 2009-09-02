################
# Small example with functions
##

picture = makeEmptyPicture(300, 400)

def centeredCircle(x, y, radius):
    """Draw a circle with center in x, y, and the given radius"""
    addOvalFilled(picture, x-radius, y-radius, radius*2, radius*2)
    
def smiley(x, y, size, color):
    """Draw a smiley onto the default picture, at the given position, size and color"""
    # draw face
    addOvalFilled(picture, x, y, size, size, color)
    # x-positions of eyes and mouth
    left = x + size/4
    right = left+size/2
    # draw eyes
    centeredCircle(left, y + size / 3, size/10)
    centeredCircle(right, y + size / 3, size/10)
    # draw mouth
    addArc(picture, left, y + size / 2, right - left, size / 3, 180, 180)


# Draw some smiley across the image
smiley(190, 90, 70, red)
smiley(100, 40, 80, green)
smiley(150, 220, 150, cyan)
smiley(200, 140, 100, blue)
smiley(10, 100, 200, yellow)
smiley(90, 190, 40, white)

# Show it
show(picture)
