import pygame

class PowerUp:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 18
        self.speed = .3

    def fall(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)