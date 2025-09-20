import pygame
pygame.init() 
#setting up the screen 
screen_width=500
screen_height=500
pygame.display.set_mode([screen_width,screen_height])
#add caption 
pygame.display.set_caption("Rocket In Space")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Pro-GameDeveloper/Assets/character.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5) #in place
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rec.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        #keep the sprite within the screen 
        if self.rect.left <0:
            self.rect.left0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <0:
            self.rect.top =0 
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
#sprites group \

#create group container for the sprites
# and this group will let us draw and update  multiple sprites 
sprites = pygame.sprite.Group()     

def start_game():
    player=Player()
    sprites.add(player)

        


        



