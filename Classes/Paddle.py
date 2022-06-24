import pygame


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 12
        self.speed = .7

    def move_right(self):
        if self.x + self.width < 1280:
            self.x += self.speed
        return self.x

    def move_left(self):
        if self.x > 180:
            self.x -= self.speed
        return self.x

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
