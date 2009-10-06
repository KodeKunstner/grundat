import pygame
import random
import sys

def lightcycle_game(antal_spillere):
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

    # Create lightcycles
    l = []
    for n in range(antal_spillere):
        l.append(Lightcycle(screen, random.randint(50,590), random.randint(50,430), (random.randint(50, 255), random.randint(50, 255), random.randint(50,255))))

    # Mainloop
    alive_count = antal_spillere 

    while alive_count > 1:
        # move those who are alive
        alive_count = 0
        for lightcycle in l:
            if lightcycle.is_alive:
                lightcycle.move()
                alive_count = alive_count + 1

        # Handle events: change direction of the lightcycles
        # in key a/d and left/right
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    l[0].left()
                elif event.key == pygame.K_d:
                    l[0].right()
                if antal_spillere > 1:
                    if event.key == pygame.K_LEFT:
                        l[1].left()
                    elif event.key == pygame.K_RIGHT:
                        l[1].right()
                if antal_spillere > 2:
                    if event.key == pygame.K_h:
                        l[2].left()
                    elif event.key == pygame.K_j:
                        l[2].right()
                if antal_spillere > 3:
                    if event.key == pygame.K_k:
                        l[3].left()
                    elif event.key == pygame.K_l:
                        l[3].right()
                if antal_spillere > 4:
                    if event.key == pygame.K_d:
                        l[4].left()
                    elif event.key == pygame.K_f:
                        l[4].right()
                if antal_spillere > 5:
                    if event.key == pygame.K_x:
                        l[5].left()
                    elif event.key == pygame.K_c:
                        l[5].right()

        # Update the screen, and wait a bit to keep the speed
        # of the lightcycles down.
        pygame.display.flip()
        pygame.time.wait(10)

    for i in range(antal_spillere):
        if l[i].is_alive:
            winner = i

    # Clean up, and exit
    pygame.quit()
    return winner

class Lightcycle:
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
        self.is_alive = True

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
            self.is_alive = True
            return True
        else:
            self.is_alive = False
            return False


antal_spillere = int(raw_input("Antal spillere: "))
if antal_spillere > 6:
    print "Fejl: der kan ikke vaere flere end 6 spillere omkring tastaturet"
    sys.exit()

antal_omgange =  int(raw_input("Antal omgange: "))

winners = [0] * antal_spillere

for omgang in range(antal_omgange):
    winners[lightcycle_game(antal_spillere)] += 1

print "Scores:"
for i in range(antal_spillere):
    print "spiller "+ str(i) + ": " + str(winners[i]);
