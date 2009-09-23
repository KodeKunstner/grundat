def mirror_diagonal(pict):
    """Mirror af picture across the line x=y"""
    size = min(getWidth(pict), getHeight(pict))
    for x in range(size):
        for y in range(x):
            src = getPixelAt(pict, x, y)
            dst = getPixelAt(pict, y, x)
            setColor(dst, getColor(src))
            
picture = makePicture(pickAFile())
mirror_diagonal(picture)
show(picture)