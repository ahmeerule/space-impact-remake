import pygame
import button as b
import classes.sprite as s
from config import SCREEN_WIDTH , SCREEN_HEIGHT , BACKGROUND_IMAGE_FILE_PATH , BACK_BUTTON_IMAGE_FILE_PATH
import time
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# BACKGROUND|
background = Background(
    image_file_path = BACKGROUND_IMAGE_FILE_PATH, 
    screen_width = SCREEN_WIDTH,
    screen_height = SCREEN_HEIGHT,
    screen_initial_x = 0 
)
second_background = Background(
    image_file_path = BACKGROUND_IMAGE_FILE_PATH, 
    screen_width = SCREEN_WIDTH,
    screen_height = SCREEN_HEIGHT,
    screen_initial_x = -SCREEN_WIDTH
)

# BUTTONS
back_button = b.Button(
    image_file_path = "assets/back.png", 
    image_x_pos=30, 
    image_y_pos=30,
    scale_height=50,
    scale_width=50
)

play_button = b.Button(
    image_file_path = 'assets/play.png',
    image_x_pos = SCREEN_WIDTH/2,
    image_y_pos = 400,
    scale_height = 100,
    scale_width = 200
)

credit_button = b.Button(
    image_file_path = 'assets/chest.png',
    image_x_pos = 200,
    image_y_pos = 400
)

quit_button = b.Button(
    image_file_path = 'assets/quit.png',
    image_x_pos = SCREEN_WIDTH/2,
    image_y_pos = 520,
    scale_height = 100,
    scale_width = 200
)


def main_menu():
    pygame.display.set_caption("Main Menu")
    #Title
    test_font = pygame.font.Font("freesansbold.ttf",70)
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

    
    
    

    # MENU LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if play_button.checkforinput():
                game()
            if quit_button.checkforinput():
                pygame.QUIT()
            if credit_button.checkforinput():
                credit()

        
        background.update(screen)
        second_background.update(screen)        
        screen.blit(text_surface,(150,50))

        credit_button.update(screen)
        quit_button.update(screen)      
        play_button.update(screen)
        pygame.display.update()


def credit():
    pygame.display.set_caption("Credits")
    
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Made by:Irwin lai",False,"white")
    asset_surface = test_font.render("Assets by:Zai ndn",False,"white")
     
  
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if back_button.checkforinput():
                main_menu()
            

        
        background.update(screen)
        second_background.update(screen)     
        screen.blit(text_surface,(200,250))
        screen.blit(asset_surface,(190,350))  
        back_button.update(screen)
        
        pygame.display.update()

def gameover():
    pygame.display.set_caption("Credits")
    
    test_font = pygame.font.Font(None,100)
    text_surface = test_font.render("Game Over",False,"white")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()
            if back_button.checkforinput():
                main_menu()
            
        
        background.update(screen)
        second_background.update(screen)     
        screen.blit(text_surface,(300,250))  
        back_button.update(screen)
        
        pygame.display.update()

def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    # setting frame rate cap tp run stabily
    clock = pygame.time.Clock()
    
    # setting screen title
    pygame.display.set_caption("Space Impact Remake")

    # all text
    score = 0
    score_text = t.text(f"Score: {score}","white", 70)
    
    
    # sprites
    all_sprite_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_sprite_group = pygame.sprite.Group()

    player = s.Player()
    all_sprite_group.add(player)

    # controls
    cooldown = 0
    shoot = False
    
    spawn_timer = 100
    total_enemy = 1

    t0 = time.time()
    timeout_seconds = 30    
    while player.alive():
        # for every event check that if user click on cross of the screen
        # then quit the game
        if time.time()-t0 > timeout_seconds:
            break
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                exit()

            # event handler 
            # KEY DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot = True
                    
            # KEY UP        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shoot = False

            if shoot:
                if cooldown == 0:
                    bullet_group.add(s.Bullets(player.rect.centerx+45,player.rect.centery+2))
                    cooldown = 3
                else:
                    cooldown -= 1
        # enemy spawn
        if spawn_timer == 0 and total_enemy <= 100:
            enemy_sprite_group.add(s.Enemy(1))
            spawn_timer = 100 
            total_enemy += 1
            
        spawn_timer -= 1                          
        
        # collsion 
        
        
        for bullet in bullet_group:
            collided_enemies_list = pygame.sprite.spritecollide(bullet,enemy_sprite_group,True)

            # if bullet hit any enemies in the enemy_sprite_group collided_enemies_list will increase in len
            if len(collided_enemies_list) > 0 :
                score += 10
                score_text = t.text(f"Score: {score}","white", 70)
                bullet.kill()
                
        
         
            
        if pygame.sprite.spritecollide(player,enemy_sprite_group,False):
            player.reset()  
        

        # background logic
        background.update(screen,0.5)
        second_background.update(screen,0.5)     

        
        bullet_group.draw(screen)
        bullet_group.update()
        enemy_sprite_group.draw(screen)
        enemy_sprite_group.update()
        all_sprite_group.draw(screen)
        all_sprite_group.update()
        score_text.update(screen,650,10)
        # constanly update gameboard 
       
        pygame.display.update()
    gameover()

if __name__=="__main__":

    main_menu()
