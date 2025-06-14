import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

class Rectangle:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = screen

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))

    def grow(self, m):
        self.width += m
        self.height += m
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            Rectangle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            Rectangle.grow(20)
            pygame.display.update()