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
ellipse(screen, (180, 180, 180), (-150, 50, 600, 150))
ellipse(screen, (180, 180, 180), (-250, 350, 600, 150))
rect(screen, (165, 165, 165), (10, 15, 120, 510))
rect(screen, (165, 165, 165), (150, 35, 120, 510))
rect(screen, (238, 238, 238), (460, 15, 120, 510))
rect(screen, (215, 215, 215), (100, 75, 120, 510))
rect(screen, (66, 127, 76), (400, 95, 120, 510))
ellipse(screen, (210, 210, 210), (-50, 650, 900, 350)) # fild

ellipse(screen, (0, 0, 0), (228, 703, 40, 8))# рисуем машину
rect(screen, (25, 225, 225), (250, 675, 240, 50))
rect(screen, (25, 225, 225), (300, 645, 115, 30))
circle(screen, (0, 0, 0), (300, 720), 25) # колеса
circle(screen, (0, 0, 0), (450, 720), 25)
rect(screen, (255, 255, 255), (310, 655, 40, 23)) # окна
rect(screen, (255, 255, 255), (363, 652, 40, 23))

surface1 = screen.convert_alpha() # сделаем прозрачные облака
surface1.fill([0, 0, 0, 0])
ellipse(surface1, (165, 165, 165, 128), (200, 10, 600, 150))
ellipse(surface1, (165, 165, 165, 128), (150, 200, 600, 150)) # облако
ellipse(surface1, (165, 165, 165, 128), (-110, 550, 200, 50)) # дым
ellipse(surface1, (165, 165, 165, 128), (10, 600, 200, 50)) # дым
ellipse(surface1, (165, 165, 165, 128), (10, 660, 200, 50)) # дым
screen.blit(surface1, (0,0))

#screen.fill([255, 255, 255]) # заполнить весь экран цветом
#pygame.display.flip()



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()