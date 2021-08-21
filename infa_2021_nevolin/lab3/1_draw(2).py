import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
# background
rect(screen, (255, 255, 255), (0, 0, 600, 800))
rect(screen, (205, 205, 205), (0, 0, 600, 500))
rect(screen, (48, 95, 56), (0, 505, 600, 800))
# rectangle
rect(screen, (165, 165, 165), (10, 15, 120, 510))
rect(screen, (165, 165, 165), (150, 35, 120, 510))
rect(screen, (238, 238, 238), (460, 15, 120, 510))
rect(screen, (215, 215, 215), (100, 75, 120, 510))
rect(screen, (66, 127, 76), (400, 95, 120, 510))






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()