import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000,600))
test_font = pygame.font.Font(None,50)


bgy = 0
second_bgx = 0

bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
bg = pygame.transform.scale(bg,(1000,600))

second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
second_bg = pygame.transform.scale(bg,(1000,600))

while True:
    # for every event check that if user click on cross of the screen
    #then quit the game
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
    bgx += 0.5
    second_bgx +=0.5

    if bgx > -1:
        bgx = -1000
    if second_bgx > 1000:
        second_bgx = 0
    screen.blit(bg,(bgx,0))
    screen.blit(second_bg,(second_bgx,0))
    pygame.display.update()