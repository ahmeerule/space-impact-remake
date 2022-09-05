
import sys, pygame
pygame.init()

width = 1000
height = 600
## convert_alpha()## convert image file to help pygame load faster
#setting screen size
screen = pygame.display.set_mode((1000,600))

#setting frame rate cap tp run stabily
clock = pygame.time.Clock()


#loading image to surface
test_surface = pygame.image.load("rpgsprites1/bg/bg.png").convert_alpha()
test_surf = pygame.transform.scale(test_surface,(width,height) )
#get the rectangle of the surface to further control ht position
test_surface_rect = test_surf.get_rect(topleft =(0,0))

#font
test_font = pygame.font.Font(None,50)
text_surface = test_font.render("welcome",False,"white")



#setting screen title
pygame.display.set_caption("assignment")
while True:
    # for every event check that if user click on cross of the screen
    #then quit the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
    
    screen.blit(test_surf,test_surface_rect)
    screen.blit(text_surface,(400,100))

    # constanly update gameboard        
    pygame.display.update()
   
    clock.tick(60)



