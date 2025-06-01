import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)

# Rectangle class
class CustomRect:
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):
        pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

# Create instances
greenRect = CustomRect(green, (50, 20, 100, 100))
redRect = CustomRect(red, (150, 200, 150, 150))
blueRect = CustomRect(blue, (300, 400, 200, 200))

# Draw them
greenRect.draw()
blueRect.draw()
redRect.draw()

pygame.display.update()

# Game loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
