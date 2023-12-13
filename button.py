import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000,600))
test_font = pygame.font.Font(None,50)


class Button():
    def __init__(self, image , x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        
        
    def update(self):
        screen.blit(self.image,self.rect)
        
    def checkforinput(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False :
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 
        return action
    

