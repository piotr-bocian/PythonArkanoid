import pygame


class Shield:
    def __init__(self, y):
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(180, self.y, 1100, 2))
