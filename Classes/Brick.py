import pygame
import random

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

    def is_powerUp(self):
        x = random.random()
        if x<=0.1:
            x = 0
            return True
        return False

    def pick_powerUp(self):
        x = random.randint(1,4)
        return x

