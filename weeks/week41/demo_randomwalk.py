import random
import pygame
pygame.init()
surface = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

x = 100
y = 100


for t in range(1000):
   x = x + random.randint(-1, 1)
   if x >= 640:
       x = 639
   if y >= 480:
       y = 479
   if x < 0:
       x = 0
   if y < 0:
       y = 0

       
   y = y + random.randint(-1, 1)

   surface.set_at((x,y), (255, 255, 255))
   pygame.display.flip()

pygame.quit()

