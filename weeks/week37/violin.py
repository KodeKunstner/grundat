basepath = "/home/voel/grundat/weeks/week37/"
def saveInvert(filename):
   picture = makePicture(filename + ".jpg")
   for pixel in getPixels(picture):
       setRed(pixel, 255 - getRed(pixel))
       setGreen(pixel, 255 - getGreen(pixel))
       setBlue(pixel, 255 - getBlue(pixel))
   writePictureTo(picture, filename + "inv.jpg")
       
#saveInvert(basepath + "violin1")
#saveInvert(basepath + "violin1zoom")

#mov = makeMovie()
addFrameToMovie(basepath + "violin1.jpg", mov)
addFrameToMovie(basepath + "violin1zoom.jpg", mov)
addFrameToMovie(basepath + "violin1inv.jpg", mov)
addFrameToMovie(basepath + "violin1zoominv.jpg", mov)
