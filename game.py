import sprite as s
import menu as m
import sys, pygame
pygame.init()
screen = pygame.display.set_mode((1000,600))

#setting frame rate cap tp run stabily
clock = pygame.time.Clock()

#setting screen title
pygame.display.set_caption("Space Impact Remake")

#BACKGROUND
def game():
    #BACKGROUND
    bgx = -1000

    second_bgx = 0
    bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    bg = pygame.transform.scale(bg,(1000,600))
    second_bg = pygame.image.load("assets/bgg.jpeg").convert_alpha()
    second_bg = pygame.transform.scale(bg,(1000,600))

    #player sprite
    all_sprite = pygame.sprite.Group()
    player = s.Player()
    all_sprite.add(player)
    
    
    
    while True:
        # for every event check that if user click on cross of the screen
        #then quit the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
        all_sprite.update()
        
    

        #background logic
        bgx += 0.5
        second_bgx +=0.5

        if bgx > -1:
            bgx = -1000
        if second_bgx > 1000:
            second_bgx = 0

        # display 
     
        screen.blit(bg,(bgx,0))
        screen.blit(second_bg,(second_bgx,0))
        # constanly update gameboard        
        pygame.display.update()
    
        clock.tick(60)



m.main()