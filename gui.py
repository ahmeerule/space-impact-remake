

import sys, pygame
pygame.init()

width = 1000

height = 600
## convert_alpha()## convert image file to help pygame load faster
#setting screen size
screen = pygame.display.set_mode((1000,600))

#setting frame rate cap tp run stabily
clock = pygame.time.Clock()

bgx = 750
#loading image to surface
first_bg_surface = pygame.image.load("assets/bgg.jpeg").convert_alpha()
first_bg_surf = pygame.transform.scale(first_bg_surface,(1000,600) )
#get the rectangle of the surface to further control ht position
first_bg_surface_rect = first_bg_surf.get_rect(topleft =(0,0))

second_bg_surface = pygame.image.load("assets/bgg.jpeg").convert_alpha()
second_bg_surf = pygame.transform.scale(second_bg_surface,(1000,600) )
#get the rectangle of the surface to further control ht position
second_bg_surface_rect = second_bg_surf.get_rect(topleft =(bgx,0))

#font
test_font = pygame.font.Font(None,50)
text_surface = test_font.render("Space Impact Remake",False,"white")

x = 0
twox = 1000
#setting screen title
pygame.display.set_caption("Space Impact Remake")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/player.png")
        self.resize =  pygame.transform.scale(self.image,(100,60))
        self.rect = self.resize.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 300
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.speedx = 0
        self.speedy = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speedx = -4
        if key_state[pygame.K_RIGHT]:
            self.speedx = + 4
        if key_state[pygame.K_UP]:
            self.speedy = - 4
        if key_state[pygame.K_DOWN]:
            self.speedy = + 4        
        if key_state[pygame.K_SPACE]:
            pass
        self.rect.x += self.speedx
        self.rect.y += self.speedy

all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
while True:
    # for every event check that if user click on cross of the screen
    #then quit the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
    all_sprite.update()
    #scrolling back ground 
    x -= 2
    twox -= 2
    if x <= -1000:
        x = 0
    if twox <=0:
        twox = 1000
    
    screen.blit(first_bg_surf,(x,0))
    screen.blit(second_bg_surf,(twox,0))
    screen.blit(text_surface,(300,100))
    screen.blit(player.resize,player.rect)
    

    # constanly update gameboard        
    pygame.display.update()
   
    clock.tick(60)



