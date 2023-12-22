import pygame
import button as b
import sprite as s
from config import SCREEN_WIDTH , SCREEN_HEIGHT
import time
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


def main_menu():
    pygame.display.set_caption("Main Menu")
    #Title
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Space Impact Remake",False,"white")

    # Buttons
    credit_button = pygame.image.load("assets/chest.png")
    credit_button = pygame.transform.scale(credit_button,(100 ,100))

    play_button = pygame.image.load('assets/play.png')
    play_button = pygame.transform.scale(play_button,(250 ,100))

    quit_button = pygame.image.load('assets/quit.png')
    quit_button = pygame.transform.scale(quit_button,(250 ,100))
   
    cbutton = b.Button(credit_button,200,400)
    pbutton = b.Button(play_button,SCREEN_WIDTH/2 , 400)
    qbutton = b.Button(quit_button,SCREEN_WIDTH/2 , 520)

    #BACKGROUND
    bgx = -1000
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    # MENU LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if pbutton.checkforinput():
                game()
            if qbutton.checkforinput():
                pygame.QUIT()
            if cbutton.checkforinput():
                credit()

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0

        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(150,50))

        cbutton.update()
        qbutton.update()      
        pbutton.update()
        pygame.display.update()

def credit():
    pygame.display.set_caption("Credits")
    
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Made by:Irwin lai",False,"white")
    asset_surface = test_font.render("Assets by:Zai ndn",False,"white")
     
    back_button = pygame.image.load("assets/back.png")
    back_button = pygame.transform.scale(back_button,(100 ,100))

    bbutton = b.Button(back_button,70,50)

    bgx = -SCREEN_WIDTH
    
    second_bgx = 0

    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if bbutton.checkforinput():
                main_menu()
            

        bgx += 0.1
        second_bgx +=0.1

        if bgx > -1:
            bgx = -SCREEN_WIDTH
        if second_bgx > SCREEN_WIDTH:
            second_bgx = 0
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        screen.blit(text_surface,(200,250))
        screen.blit(asset_surface,(190,350))  
        bbutton.update()
        
        pygame.display.update()


main_menu()