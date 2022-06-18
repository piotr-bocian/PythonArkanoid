import pygame


class Brick:
    def __init__(self, x, y) -> object:
        self.x = x
        self.y = y
        self.width = 80
        self.height = 16
        self.color = (255, 0, 0)
        self.points = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
