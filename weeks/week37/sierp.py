p = makeEmptyPicture(500,500)

def sierp(p, x, y, size):
    if size < 3:
      addRect(p, x, y, size, size)
    else:
      size = size / 3
      sierp(p, x, y, size)
      sierp(p, x + 2 * size, y, size)
      sierp(p, x, y + 2 * size, size)
      sierp(p, x + 2 * size, y + 2 * size, size)

sierp(p, 10, 10, 200)
show(p)