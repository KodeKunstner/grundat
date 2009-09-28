import pygame
import random

pygame.init()
surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

x = 100
y = 100
for _ in range(10000):
    for __ in range(1000):
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x >= 640:
            x = 639 
        if y >= 480:
            y = 479 
        c = surface.get_at((x,y))
        c = (c[0]+1, c[1]+1, c[2]+1)
        surface.set_at((x,y),c )
    pygame.display.flip()

    
pygame.quit()

