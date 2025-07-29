
import pgzrun
import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Space Invader Game!!!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
#border of the game 
BORDER = pygame.Rect(WIDTH//2 - 5,0,10,  HEIGHT)
HEATLH_FONT = pygame.font.SysFont('Roboto',40)
WINNER_FONT = pygame.font.SysFont('comicsans',40)
FPS  = 60  #60 frame per second 
MAX_BULLETS = 3 #maximum number of bulltes
VEL = 5 #player movement speed 
BULLETS_VEL  = 7 # bullet speed 
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,50

red_ship_image = pygame.image.load(
    os.path.join('Pro-GameDeveloper/Assets/spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_ship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
yellow_ship_image =  pygame.image.load(
    os.path.join('Pro-GameDeveloper/Assets/spaceship_yellow.png'))
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(
    yellow_ship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
space_bg_image = pygame.image.load('Pro-GameDeveloper/background.png')
#custom events 
yellow_hit = pygame.USEREVENT + 1
red_red = pygame.USEREVENT +2
#function to add everything together  
def draw_Window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(space_bg_image,(0,0))
    pygame.Rect(WIN, BLACK,BORDER)
    red_health_text = HEATLH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEATLH_FONT.render("Health: " + str(red_health), 1, WHITE)
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10 ,10))
    WIN.blit(yellow_health_text,(10 ,10))

    #code to place the spaceships
    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(red_spaceship, (red.x, red.y))
    #code for bullets.
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    pygame.display.update()
#code to handle the movement
def yellow_handle_movements(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x -VEL >0:
        yellow.x -=VEL
    if key_pressed[pygame.K_d] and yellow.x +VEL+ yellow.width < BORDER.x:
        yellow.x +=VEL
    if key_pressed[pygame.K_w] and yellow.y -VEL>0:
        yellow.y -=VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height -15:
        yellow.y += VEL
















#pgzrun.go()
 



    








