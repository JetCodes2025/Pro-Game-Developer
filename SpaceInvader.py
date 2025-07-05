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

red_ship_image = pygame.image.load('Pro-GameDeveloper/Assets/spaceship_red.png')
yellow_ship_image =  pygame.image.load('Pro-GameDeveloper/Assets/spaceship_yellow.png')
space_bg_image = pygame.image.load('Pro-GameDeveloper/background.png')
#custom events 
yellow_hit = pygame.USEREVENT + 1
red_red = pygame.USEREVENT +2
#function to add everything together  
def draw_Window(RED,YELLOW,red_bullets,yellow_bulltes,red_health, yellow_health):
    WIN.blit(space_bg_image,(0,0))
    pygame.Rect(WIN, BLACK,BORDER)
    red_health_text = HEATLH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEATLH_FONT.render("Health: " + str(red_health), 1, WHITE)
    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width() - 10 ,10))
    WIN.blit(yellow_health_text,(10 ,10))



    








