import pygame
from pygame.locals import *

pygame.init()

# Set up screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Player Movement")

# Load images (make sure paths are correct)
player = pygame.image.load("Pro-GameDeveloper/character.png")
background = pygame.image.load("Pro-GameDeveloper/Assets/background.png")

# Player starting position
player_x = 200
player_y = 200
keys = [False, False, False, False]

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while player_y < 600 and running:
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        
        # Key release
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0] = False
            elif event.key == K_LEFT:
                keys[1] = False
            elif event.key == K_DOWN:
                keys[2] = False
            elif event.key == K_RIGHT:
                keys[3] = False

    # Movement logic
    if keys[0] and player_y > 0:
        player_y -= 7
    elif keys[2] and player_y < 536:
        player_y += 7
    if keys[1] and player_x > 0:
        player_x -= 2
    elif keys[3] and player_x < 536:
        player_x += 2

    # Gravity or auto-fall
    player_y += 5

    # Control frame rate (20 FPS)
    clock.tick(20)

print("Game Over")
pygame.quit()
