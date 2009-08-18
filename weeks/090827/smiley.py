###################
# Create a picture of a Smiley,
##

picture = makeEmptyPicture(100,100)

# Let the user select the color of the face
# and draw it.
color = pickAColor()
addOvalFilled(picture, 10, 10, 80, 80, color)

# Add two eyes, and a mouth
addOvalFilled(picture, 30, 30, 10, 10)
addOvalFilled(picture, 60, 30, 10, 10)
addArc(picture, 20, 30, 60, 50, 180, 180)

show(picture)
