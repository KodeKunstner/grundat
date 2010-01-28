import pygame
import math

class Turtle(object):
    """Simple turtle graphics class, that can be used for drawing on the screen with pygame."""
    def __init__(self, surface):
        # The properties of the turtle we are drawing with
        self.x = surface.get_width() / 2
        self.y = surface.get_height() / 2
        self.direction = 0.0
        self.color = (100,100,100)
        self.surface = surface
        self.slowdown = True

    def forward(self, len):
        start = (self.x, self.y)
        self.x = self.x + len * math.cos(self.direction * math.pi / 180)
        self.y = self.y + len * math.sin(self.direction * math.pi / 180)
        end = (self.x, self.y)
        pygame.draw.aaline(self.surface, self.color, start, end)
        if self.slowdown:
            pygame.display.flip()
            pygame.time.wait(int(len))

    def right(self, degrees):
        self.direction += degrees

    def left(self, degrees):
        self.direction -= degrees

# Demo
if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    
    def koch(turtle, len):
        if len < 4:
            turtle.forward(len)
        else:
            len = len / 3.0
            koch(turtle, len)
            turtle.left(60)
            koch(turtle, len)
            turtle.right(120)
            koch(turtle, len)
            turtle.left(60)
            koch(turtle, len)

    # The following is an example of how to use the turtle graphics object
    # on a pygame surface
    turtle = Turtle(surface)

    turtle.slowdown = True

    turtle.color = (255, 0, 0)
    for i in xrange(100):
        turtle.left(95)
        turtle.forward(i)

    turtle.color = (0, 255, 0)
    for i in xrange(720):
        turtle.left(i)
        turtle.forward(10)

    turtle.color = (0, 0, 255)
    for i in xrange(100):
        turtle.left(91)
        turtle.forward(100)

    turtle.color = (255,255,255)
    koch(turtle, 200)
    turtle.right(120)
    koch(turtle, 200)
    turtle.right(120)
    koch(turtle, 200)

    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
