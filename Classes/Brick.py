import pygame


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 12
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
