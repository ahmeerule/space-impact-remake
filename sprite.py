import sys, pygame


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
        self.rect.x += self.speedx
        self.rect.y += self.speedy