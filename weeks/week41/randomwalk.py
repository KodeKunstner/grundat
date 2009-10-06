import pygame
import random

pygame.init()
surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

x = 320
y = 240
for _ in range(10000):
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
    surface.set_at((x, y), (255, 255, 255))
    pygame.display.flip()

pygame.quit()

