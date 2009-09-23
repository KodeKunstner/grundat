import pygame
import random
class lightcycle(object):
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.retning = random.randint(0,3)

    def move(self):
        if self.retning == 0:
            self.x = self.x + 1
        elif self.retning == 1:
            self.y = self.y + 1
        elif self.retning == 2:
            self.x = self.x - 1
        else:
            self.y = self.y - 1

        print self.screen.get_at((self.x, self.y))
        if self.screen.get_at((self.x, self.y)) == (0,0,0,255):
            self.screen.set_at((self.x, self.y), self.color)
            return True
        else:
            return False
            

pygame.init()
surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
for x in range(640):
    for y in range(480):
        surface.set_at((x, y), (0, 0, 0))
        

l1 = lightcycle(surface, 200,200,(255,0,0))
while l1.move():
    pygame.display.flip()
    pygame.time.wait(100)
    
pygame.quit()




# pygame.event.get() 
# event.type pygame.KEYDOWN:
# event.key pygame.K_a pygame.K_LEFT:
# pygame.display.flip()
# pygame.time.wait(10)

