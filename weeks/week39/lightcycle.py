import pygame
import random

def lightcycle_game():
    """ Lightcycle game. Two players steer lightcycles,
        and the goal is to avoid running into each other or the wall,
        as long as possible..."""
    # Initialise pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

    # Draw the level, i.e. fill the screen with black, 
    # and add a white border
    screen.fill((0, 0, 0))
    w = screen.get_width()
    h = screen.get_height()
    
    for x in range(w):
        screen.set_at((x, 0), (255, 255, 255))
        screen.set_at((x, h - 1), (255, 255, 255))
    for y in range(h):
        screen.set_at((0, y), (255, 255, 255))
        screen.set_at((w - 1, y), (255, 255, 255))

    # Create two lightcycles
    l1 = lightcycle(screen, w/3, h/2, (255, 0, 0))
    l2 = lightcycle(screen, 2*w/3, h/2, (0, 0, 255))

    # Mainloop
    while l1.move() and l2.move():
        # Handle events: change direction of the lightcycles
        # in key a/d and left/right
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    l1.left()
                elif event.key == pygame.K_d:
                    l1.right()
                elif event.key == pygame.K_LEFT:
                    l2.left()
                elif event.key == pygame.K_RIGHT:
                    l2.right()

        # Update the screen, and wait a bit to keep the speed
        # of the lightcycles down.
        pygame.display.flip()
        pygame.time.wait(10)

    # Clean up, and exit
    pygame.quit()

class lightcycle:
    """Lightcycle class, - a single point at the screen,
    which moves until it runs into something.
    The object has the following properties: color, x and y coordinates, 
    direction which is an integer where 0 means left, 
    1 means down, 2 means right and 3 means up, 
    and a reference to the screen where it is drawn"""

    def __init__(self, screen, x, y, color):
        """Create the object"""
        self.direction = random.randint(0, 3)
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color

    def left(self):
        """Turn left"""
        self.direction = self.direction - 1
        if self.direction < 0:
            self.direction = 3

    def right(self):
        """Turn right"""
        self.direction = self.direction + 1
        if self.direction > 3:
            self.direction = 0

    def move(self):
        """Try moving the lightcycle one pixel in the current direction,
            returns false if it runs into something - where "something"
            means a pixel which is not black"""
        # Change the x and y coordinate for the point
        if self.direction == 0:
            self.x = self.x + 1
        elif self.direction == 1:
            self.y = self.y + 1
        elif self.direction == 2:
            self.x = self.x - 1
        else:
            self.y = self.y - 1

        # if the current point is on a black background,
        # change the color else return an error.
        # (The (0,0,0,255) is due to that we also get alpha component).
        if self.screen.get_at((self.x, self.y)) == (0, 0, 0, 255):
            self.screen.set_at((self.x, self.y), self.color)
            return True
        else:
            return False

lightcycle_game()
