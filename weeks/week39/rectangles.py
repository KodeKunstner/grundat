import pygame
import random

def draw_rect(screen, x0, y0, x1, y1):
    if x0 > x1:
        x0,x1 = x1,x0

    if y0 > y1:
        y0,y1 = y1,y0

    for x in range(x0, x1):
        screen.set_at((x, y0), (0,0,0))
        screen.set_at((x, y1), (0,0,0))
    for y in range(y0, y1):
        screen.set_at((x0, y), (0,0,0))
        screen.set_at((x1, y), (0,0,0))
    for x in range(x0 + 1, x1 - 1):
        for y in range(y0 + 1, y1 - 1):
            screen.set_at((x, y), (100,100,100))

pygame.init()
surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

for _ in range(100):
    draw_rect(surface, random.randint(0, 639), random.randint(0, 479), random.randint(0, 639), random.randint(0, 479))
    pygame.display.flip()

    
pygame.quit()

