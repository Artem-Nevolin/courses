import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen,(225, 225, 225), (0, 0, 400, 400))
# face
circle(screen, (225, 225, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
# left eye
circle(screen, (250, 0, 0), (150, 175), 25)
circle(screen, (0, 0, 0), (150, 175), 25, 1)
circle(screen, (0, 0, 0), (150, 175), 10)
# left brow eye
polygon(screen, (0, 0, 0), [(100, 110), (185, 170), (191, 160), (106, 100)])
# right eye
circle(screen, (250, 0, 0), (250, 175), 20)
circle(screen, (0, 0, 0), (250, 175), 20, 1)
circle(screen, (0, 0, 0), (250, 175), 10)
# right brow eye
polygon(screen, (0, 0, 0), [(220, 168), (300, 125), (294, 115), (214, 158)])
# mouth
rect(screen,(0, 0, 0), (150, 250, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

